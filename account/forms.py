from django import forms
from django.contrib.auth.models import User
from .models import Profile, SessionCbio, SessionMyriad, SessionSmsc
from account import HealthCheck
import datetime


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'first_name', 'email'}

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class HealthCheckCbioForm(forms.Form):
    """class Meta:
        model = SessionCbio
        fields = ('servername', 'serverIP', 'serverUsername', 'password')"""


    data = forms.ModelChoiceField(label='What is the server to check ', queryset=SessionCbio.objects.only('servername'), required=True)

class HealthCheckUssdForm(forms.Form):
    """class Meta:
        model = SessionCbio
        fields = ('servername', 'serverIP', 'serverUsername', 'password')"""


    data = forms.ModelChoiceField(label='What is the server to check ', queryset=SessionMyriad.objects.only('servername'), required=True)


class HealthCheckSmscForm(forms.Form):
    """class Meta:
        model = SessionCbio
        fields = ('servername', 'serverIP', 'serverUsername', 'password')"""


    data = forms.ModelChoiceField(label='What is the server to check ', queryset=SessionSmsc.objects.only('servername'), required=True)

class CdrSMSCForm(forms.Form):
    sender = forms.CharField()
    receiver = forms.CharField(required=False)
    startdate = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    enddate = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    CHOICES = [('Mo', 'Mo'),
               ('Mt', 'Mt'),
               ('CheckBill', 'Checkbill'),]
    SMType = forms.ChoiceField(choices=CHOICES, widget=forms.Select)

class ReactSIMForm(forms.Form):
    msisdn = forms.CharField()
    serviceClass = forms.CharField()

    CHOICES = [('newSIM', 'newSIM'),
               ('avecFrais','avecFrais'),]
    ReactType = forms.ChoiceField(label= "Type of Reactivation ", choices=CHOICES, widget=forms.Select)

class OrangeDetForm(forms.Form):
    #msisdn = forms.CharField()
    msisdn = forms.CharField(widget= forms.Textarea, label="msisdn+imsi", required=True)
    CHOICES = [('STKB', 'STKB'),
               ('STKA', 'STKA'),
               ('no_subs', 'no_subs'),]
    ParamType = forms.ChoiceField(label="Type of paramétrage", choices=CHOICES, widget=forms.Select)