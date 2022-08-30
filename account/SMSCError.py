#!/usr/bin/env python
# coding: utf-8

# In[6]:

from django.conf import settings as django_settings
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.backends.backend_pdf import PdfPages
import paramiko
import os
import csv
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import matplotlib.dates as mdates

descerr = {0:'Succeed', 1:'Unknown Subscriber',2:'Undefined Subscriber', 3:'Unauthorized subscriber', 4:'Telecommunication service not Supported',
           5:'Call barred', 7:'Equipment Not supported', 8:'Out of service area', 10:'SM sending Failure', 11:'Full HLR Message Waiting Queue',
           14:'Invalid Data', 15:'MS error', 16:'The MS Supports No SMs', 17:'Full MS Memory', 18:'Congested SMApp', 20:'Invalid Address',
           21:'Unknown SMApp', 22:'Illegal Equipment', 23:'Busy Subscriber', 24:'MS Switched Off', 34:'Unexpected Data from the HLR',
           35:'Unexpected Data from the MSC', 40:'No Response to Route Query Request Returned from HLR', 41:'No MS Status Notification Response Returned from HLR',
           48:'No Response from MSC', 51:'Rejected by MSC', 52:'Rejected by HLR', 53:'Rejected by the Signaling Gateway',
           56:'HLR System Error', 57:'MSC System Error', 61:'MAPProxy Rejects MT Deliver Request', 62:'MTI Server Failed to Deliver an SM Due to Traffic Control',
           65:'The Signaling Gateway Has Not Responded Within the Timeout Interval', 66:'Temporary ESME Interface Error', 67:'Invalid Interface',
           75:'STP Failed to Transmit SMs', 100:'SMS Not Supported', 155:'Dual-Mode Subscriber of CDMA Network Roamed to GSM Network',
           156:'MDN and MIN Not Contained in MT SM', 214:'SS7 Subsystem Failure', 216:'SS7 Network Failure/MTP Failure',
           218:'SS7 Unqualified', 254:'Delivery Failed', 255:'Undefined Error'}
lst = []

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.111.30.204', username="taskmng", password="Atae_123")
sftp = ssh.open_sftp()
file_remote = "/home/taskmng/OMA/HSM/statres/statErreurParJour.csv"
file_local = str(os.getcwd()+"/statErreurParJour.csv")
sftp.get(file_remote, file_local)
sftp.close()
ssh.close()

plt.style.use('ggplot')
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)
plt.rcParams['figure.figsize'] = (15, 5)
#fig, axes = plt.subplots(nrows=10, ncols=10)

with open(file_local,newline='') as f:
    r = csv.reader(f)
    lines = list(r)

lines[0] = ['date;errorcode;nb']

with open(file_local,'w',newline='') as f:
    w = csv.writer(f)
    w.writerows(lines)
    
stat = pd.read_csv(str(os.getcwd()+"/statErreurParJour.csv"), sep=';',dtype=str, converters = {'errorcode': int, 'nb': int})
#str(stat['date'])
#stat
#print(stat.dtypes

stat['date'] = pd.to_datetime(stat['date'], format='%d%m%Y')
stat.set_index('date', inplace=True)


# In[7]:


stat
#print(descerr.get(0))


# In[8]:


for i in stat['errorcode']:
    if i not in lst:
        lst.append(i)


# In[9]:


#for v in range(0,1):
lst.sort()
pp = PdfPages(str(os.getcwd()+"/SMSCDailyError.pdf"))
for x in lst:
#print(x)
 stat_x = stat[stat['errorcode']==x]
 stat_x['nb']
#stat_x['nb'].plot(figsize=(50, 50), label=x)
#fig,ax = plt.subplots(nrows=1, ncols=1, figsize=(18, 5))
 fig,axs = plt.subplots(1, figsize=(18, 5))
 axs.plot(stat_x['nb'], label=x)
 axs.text(mdates.date2num(stat_x.index[-1]), stat_x['nb'][-1], '({}, {})'.format(stat_x.index[-1].strftime('%Y-%m-%d'), stat_x['nb'][-1]))
 axs.set_title(str(x)+" " +str(descerr.get(x)))
 #plt.savefig("C:/Users\hsm\Desktop\plots.pdf")
 pp.savefig(fig)
pp.close()
 #stat_x['nb'].plot()


# In[10]:


"""
os.chdir("C:/Users/hsm/Desktop/")


sender = 'stat SMSC error Code'
#receivers = ['henintsoa.rajaonarivony@orange.com','michael.kharma@orange.com','elie.tendriniombonana@orange.com','rija.rakotoarindrazaka@orange.com']
receivers = ['henintsoa.rajaonarivony@orange.com']
fileToSend = "SMSCDailyError.pdf"
body = "Hello, find on attached SMS per error code stats.\n\nRegards,\nHenintsoa"

SUBJECT = 'SMS error code'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = ';'.join(receivers)
msg['Subject'] = SUBJECT
msg.preamble = "Hello, find on attached SMS per error code stats."

part = MIMEBase('application', "octet-stream")
part.set_payload(open("SMSCDailyError.pdf", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename="SMSCDailyError.pdf")
msg.attach(part)
msg.attach(MIMEText(body, "plain"))

smtpObj = smtplib.SMTP('192.168.19.102')
smtpObj.sendmail(sender, receivers, msg.as_string())
print ("Successfully sent email")


# In[ ]:
"""



