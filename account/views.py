from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, HealthCheckCbioForm, HealthCheckUssdForm, HealthCheckSmscForm, CdrSMSCForm, ReactSIMForm, OrangeDetForm
from django.contrib.auth.decorators import login_required
from .models import Profile, SessionCbio
from django.contrib import messages
from django.http import FileResponse, Http404
from account import HealthCheck, GetCdrSmsc, ReactivationSIM, OrangeDet
import pandas as pd
import os
from account.models import SessionCbio, SessionMyriad, SessionSmsc
from datetime import datetime, timedelta
from django.core.paginator import Paginator
import mimetypes

CURRENT_DIRECTORY = os.getcwd()

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def vas(request):
    return render(request,'account/vas.html',{'section': 'VAS'})

def smsc(request):
    return render(request, 'account/smsc.html', {'section': 'VAS'})

def ussd(request):
    return render(request, 'account/ussd.html', {'section': 'VAS'})

@login_required
def pdf_view(request):
    exec(open(os.getcwd()+"/account/SMSCError.py").read())
    try:
        return FileResponse(open(os.getcwd()+"/SMSCDailyError.pdf", 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    #return render(request,'account/dashboard.html',{'section': 'Showpdf'})


@login_required
def HC_SMSC(request):
    resp1 = ""
    resp2 = ""
    mydata  = ""
    healthchecksmsc_form = HealthCheckSmscForm(request.POST)
    if request.POST:
        if healthchecksmsc_form.is_valid():

            mydata = healthchecksmsc_form.cleaned_data.get("data")
            myIP = SessionSmsc.objects.get(servername=mydata).serverIP
            myusername = SessionSmsc.objects.get(servername=mydata).serverUsername
            mypassword = SessionSmsc.objects.get(servername=mydata).password
            resp1 = HealthCheck.health_check(myIP, myusername, mypassword)
            resp2 = HealthCheck.health_check2(myIP, myusername, mypassword)

            #print(resp1)

        else :
            #return HttpResponseRedirect('/')
            print("hello")

    return render(request,'account/HC_smsc.html',{'section': 'VAS', 'healthchecksmsc_form': healthchecksmsc_form, 'table': resp1, 'table2': resp2, 'servername': mydata })

def IN(request):
    return render(request, 'account/IN.html', {'section': 'IN'})

@login_required
def HC_IN(request):
    resp1 = ""
    resp2 = ""
    mydata = ""

    healthcheckcbio_form = HealthCheckCbioForm(request.POST)
    if request.POST:
        if healthcheckcbio_form.is_valid():

            mydata = healthcheckcbio_form.cleaned_data.get("data")
            myIP = SessionCbio.objects.get(servername=mydata).serverIP
            myusername = SessionCbio.objects.get(servername=mydata).serverUsername
            mypassword = SessionCbio.objects.get(servername=mydata).password
            print(myIP)
            if myIP == "10.110.5.115" or myIP == "10.110.5.117" or myIP == "10.110.5.142" or myIP == "10.110.5.57" or myIP == "10.110.5.106":
                resp1 = HealthCheck.health_checkIVR(myIP,myusername,mypassword)
                resp2 = HealthCheck.health_checkIVR_Inodes(myIP, myusername, mypassword)
            else:
                resp1 = HealthCheck.health_check3(myIP,myusername,mypassword)
                resp2 = HealthCheck.health_check4(myIP, myusername, mypassword)
            #print(resp1["Use"])
            #print(resp2)

        else:
            # return HttpResponseRedirect('/')
            print("hello")

    return render(request,'account/HC_IN.html',{'section': 'IN', 'healthcheckcbio_form': healthcheckcbio_form, 'table': resp1, 'table2': resp2, 'servername': mydata })

def HC_USSD(request):
    resp1 = ""
    resp2 = ""
    mydata = ""

    healthcheckussd_form = HealthCheckUssdForm(request.POST)
    if request.POST:
        if healthcheckussd_form.is_valid():

            mydata = healthcheckussd_form.cleaned_data.get("data")
            myIP = SessionMyriad.objects.get(servername=mydata).serverIP
            myusername = SessionMyriad.objects.get(servername=mydata).serverUsername
            mypassword = SessionMyriad.objects.get(servername=mydata).password
            resp1 = HealthCheck.health_checkUSSD(myIP, myusername, mypassword)
            resp2 = HealthCheck.health_checkUSSD_Inodes(myIP, myusername, mypassword)

        else:
            # return HttpResponseRedirect('/')
            print("hello")

    return render(request, 'account/HC_ussd.html', {'section': 'VAS', 'healthcheckussd_form': healthcheckussd_form, 'table': resp1, 'table2': resp2,'servername': mydata})

def CDR_SMSC(request):
    resp1 = ""
    nbrows = ""
    if request.method == 'POST':
        cdrsmsc_form = CdrSMSCForm(request.POST)
        if cdrsmsc_form.is_valid():
            sender = cdrsmsc_form.cleaned_data.get("sender")
            receiver = cdrsmsc_form.cleaned_data.get("receiver")
            mydata = (datetime.strftime(cdrsmsc_form.cleaned_data.get("startdate"), '%Y%m%d'))
            mydata1 = (datetime.strftime(cdrsmsc_form.cleaned_data.get("enddate"), '%Y%m%d'))
            SMtype =  cdrsmsc_form.cleaned_data.get("SMType")
            resp1 = GetCdrSmsc.search(sender,receiver,mydata,mydata1,SMtype)
            resp1.to_csv('C:/mycdr.csv')
            nbrows = len(resp1.index)


        else:
            print("Hello")
    else:
        cdrsmsc_form = CdrSMSCForm()
    return render(request, 'account/CDR_smsc.html', {'section': 'VAS', 'cdrsmsc_form': cdrsmsc_form, 'table':resp1, 'nbrows': nbrows})

def React_SIM(request):
    resp = ""
    resp1 = ""
    resp2 = ""
    resp3 = ""
    resp4 = ""
    if request.method == 'POST':
        reactSIM_form = ReactSIMForm(request.POST)
        if reactSIM_form.is_valid():
            msisdn = reactSIM_form.cleaned_data.get("msisdn")
            sc = reactSIM_form.cleaned_data.get("serviceClass")
            ReactType = reactSIM_form.cleaned_data.get("ReactType")
            if ReactType == "newSIM":
                resp1, resp2, resp3 = ReactivationSIM.NewSIM(msisdn, sc)
            else:
                resp1, resp2, resp3, resp4 = ReactivationSIM.ReactFrais(msisdn, sc)
        else :
            print("hello")
    else:
        reactSIM_form = ReactSIMForm()
    return render(request, 'account/React_SIM.html', {'section': 'IN', 'reactSIM_form': reactSIM_form, 'resp1': resp1,
                                                      'resp2': resp2, 'resp3': resp3, 'resp4': resp4})

def Orange_Det(request):
    for f in os.listdir(CURRENT_DIRECTORY+"/account/file"):
        os.remove(os.path.join(CURRENT_DIRECTORY+"/account/file", f))
    resp1=""
    res = []
    if request.method == 'POST':
        orangeDet_form = OrangeDetForm(request.POST)
        if orangeDet_form.is_valid():
            msisdn = orangeDet_form.cleaned_data.get("msisdn")
            paramtype = orangeDet_form.cleaned_data.get("ParamType")
            
            resp = OrangeDet.barring(msisdn,paramtype)
            for path in os.listdir(CURRENT_DIRECTORY+"/account/file"):
                res.append(path)
            print(res)
        else:
            print("hello")
    else:
        orangeDet_form = OrangeDetForm()
    return render(request, 'account/Orange_Det.html', {'section': 'IN', 'orangeDet_form': orangeDet_form, 'res': res})


def down_bar(request,filename):
    # Define Django project base directory
        # Define the full file path
        filepath = CURRENT_DIRECTORY+"/account/file/" + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response