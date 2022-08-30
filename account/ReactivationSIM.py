import requests
from datetime import datetime, timedelta
import os
url="http://10.110.4.24:10011/Air"
headers = {'content-type': 'text/xml','User-Agent':'IVR/5.0/1.0','Authorization':'Basic b21hX2hzbTpIYWxlQExvaWEyMEAyMQ=='}



def NewSIM(msisdn,sc):
    my_date = datetime.now().strftime('%Y%m%dT%H:%M:')
    body1 = """<?xml version="1.0"?>
<methodCall>
<methodName>DeleteSubscriber</methodName>
<params>
<param>
<value>
<struct>
<member>
<name>originNodeType</name>
<value>
<string>OMCBIO</string>
</value>
</member>
<member>
<name>originHostName</name>
<value>
<string>HSM</string>
</value>
</member>
<member>
<name>originTransactionID</name>
<value>
<string>12345</string>
</value>
</member>
<member>
<name>originTimeStamp</name>
<value>
<dateTime.iso8601>{date}00+0300</dateTime.iso8601>
</value>
</member>
<member>
<name>subscriberNumber</name>
<value>
<string>{msisdn}</string>
</value>
</member>
<member>
<name>barring</name>
<value><boolean>0</boolean></value>
</member>
<member>
<name>originOperatorID</name>
<value>
<string>PAG</string>
</value>
</member>
</struct>
</value>
</param>
</params>
</methodCall>\n""".format(msisdn=msisdn, date=my_date)

    body2="""<?xml version="1.0"?>
<methodCall>
<methodName>InstallSubscriber</methodName>
<params>
<param>
<value>
<struct>
                <member>
                               <name>originNodeType</name>
                               <value><string>OMCBIO</string></value>
                </member>
                <member>
                               <name>originHostName</name>
                               <value><string>HSM</string></value>
                </member>
                <member>
                               <name>originTransactionID</name>
                               <value><string>12345</string></value>
                </member>
                <member>
                               <name>originTimeStamp</name>
                               <value><dateTime.iso8601>{date}00+0100</dateTime.iso8601></value>
                </member>
                <member>
                               <name>subscriberNumber</name>
                               <value><string>261{msisdn}</string></value>
                </member>
                <member>                 
                               <name>serviceClassNew</name>
                               <value><int>{sc}</int></value>
                </member>
                <member>
                               <name>accountGroupID</name>
                               <value><int>1</int></value>  
                </member>
                <member>
                               <name>subscriberNumberNAI</name>
                               <value><int>1</int></value>
                </member>
</struct>
</value>
</param>
</params>
</methodCall>\n""".format(msisdn = msisdn, date=my_date, sc = sc)

    body3="""<?xml version="1.0" encoding="utf-8"?>
<methodCall>
<methodName>Refill</methodName>
<params>
<param>
<value>
<struct>
     <member>
        <name>originHostName</name>
        <value><string>HSM</string></value>
     </member>
     <member>
        <name>originNodeType</name>
        <value><string>OMCBIO</string></value>
     </member>
     <member>
        <name>originTimeStamp</name>
        <value><dateTime.iso8601>{date}00+0300</dateTime.iso8601></value>
     </member>
     <member>
        <name>originTransactionID</name>
        <value><string>12345</string></value>
     </member>
     <member>
        <name>subscriberNumber</name>
        <value><string>{msisdn}</string></value>
     </member>
     <member>
        <name>transactionCode</name>
        <value><string>ADJ</string></value>
     </member>
     <member>
        <name>transactionType</name>
        <value><string>TEST</string></value>
     </member>
     <member>
        <name>transactionAmount</name>
        <value><string>0</string></value>
     </member>
     <member>
        <name>transactionCurrency</name>
        <value><string>MGA</string></value>
     </member>
     <member>
        <name>refillProfileID</name>
        <value><string>ZZ</string></value>
     </member>
</struct>
</value>
</param>
</params>
</methodCall>\n\n\n""".format(msisdn = msisdn, date=my_date)

    response1 = requests.post(url, data=body1, headers=headers)  # print(body1)
    response2 = requests.post(url, data=body2, headers=headers)  # print(body2)
    response3 = requests.post(url, data=body3, headers=headers)  # print(body3)
    #response = response1.text +"\n\n\n"+ response2.text +"\n\n\n"+ response3.text
    return response1.text, response2.text, response3.text

def ReactFrais(msisdn,sc):
    my_date = datetime.now().strftime('%Y%m%dT%H:%M:')
    body1 = """<?xml version="1.0"?>
    <methodCall>
    <methodName>DeleteSubscriber</methodName>
    <params>
    <param>
    <value>
    <struct>
    <member>
    <name>originNodeType</name>
    <value>
    <string>OMCBIO</string>
    </value>
    </member>
    <member>
    <name>originHostName</name>
    <value>
    <string>HSM</string>
    </value>
    </member>
    <member>
    <name>originTransactionID</name>
    <value>
    <string>12345</string>
    </value>
    </member>
    <member>
    <name>originTimeStamp</name>
    <value>
    <dateTime.iso8601>{date}00+0300</dateTime.iso8601>
    </value>
    </member>
    <member>
    <name>subscriberNumber</name>
    <value>
    <string>{msisdn}</string>
    </value>
    </member>
    <member>
    <name>barring</name>
    <value><boolean>0</boolean></value>
    </member>
    <member>
    <name>originOperatorID</name>
    <value>
    <string>PAG</string>
    </value>
    </member>
    </struct>
    </value>
    </param>
    </params>
    </methodCall>\n""".format(msisdn=msisdn, date=my_date)

    body2 = """<?xml version="1.0"?>
    <methodCall>
    <methodName>InstallSubscriber</methodName>
    <params>
    <param>
    <value>
    <struct>
                    <member>
                                   <name>originNodeType</name>
                                   <value><string>OMCBIO</string></value>
                    </member>
                    <member>
                                   <name>originHostName</name>
                                   <value><string>HSM</string></value>
                    </member>
                    <member>
                                   <name>originTransactionID</name>
                                   <value><string>12345</string></value>
                    </member>
                    <member>
                                   <name>originTimeStamp</name>
                                   <value><dateTime.iso8601>{date}00+0100</dateTime.iso8601></value>
                    </member>
                    <member>
                                   <name>subscriberNumber</name>
                                   <value><string>261{msisdn}</string></value>
                    </member>
                    <member>                 
                                   <name>serviceClassNew</name>
                                   <value><int>{sc}</int></value>
                    </member>
                    <member>
                                   <name>accountGroupID</name>
                                   <value><int>1</int></value>  
                    </member>
                    <member>
                                   <name>subscriberNumberNAI</name>
                                   <value><int>1</int></value>
                    </member>
    </struct>
    </value>
    </param>
    </params>
    </methodCall>\n""".format(msisdn=msisdn, date=my_date, sc=sc)

    body3 = """<?xml version="1.0" encoding="utf-8"?>
    <methodCall>
    <methodName>Refill</methodName>
    <params>
    <param>
    <value>
    <struct>
         <member>
            <name>originHostName</name>
            <value><string>HSM</string></value>
         </member>
         <member>
            <name>originNodeType</name>
            <value><string>OMCBIO</string></value>
         </member>
         <member>
            <name>originTimeStamp</name>
            <value><dateTime.iso8601>{date}00+0300</dateTime.iso8601></value>
         </member>
         <member>
            <name>originTransactionID</name>
            <value><string>12345</string></value>
         </member>
         <member>
            <name>subscriberNumber</name>
            <value><string>{msisdn}</string></value>
         </member>
         <member>
            <name>transactionCode</name>
            <value><string>ADJ</string></value>
         </member>
         <member>
            <name>transactionType</name>
            <value><string>TEST</string></value>
         </member>
         <member>
            <name>transactionAmount</name>
            <value><string>0</string></value>
         </member>
         <member>
            <name>transactionCurrency</name>
            <value><string>MGA</string></value>
         </member>
         <member>
            <name>refillProfileID</name>
            <value><string>ZZ</string></value>
         </member>
    </struct>
    </value>
    </param>
    </params>
    </methodCall>\n\n\n""".format(msisdn=msisdn, date=my_date)

    body4 = """<?xml version="1.0" ?>
    <methodCall>
    <methodName>UpdateBalanceAndDate</methodName>
    <params>
    <param>
    <value>
    <struct>
        <member>
                                   <name>originNodeType</name>
                                   <value><string>EXT</string></value>
        </member>
        <member>
                                   <name>subscriberNumber</name>
                                   <value><string>{msisdn}</string></value>
        </member>
        <member>
                                   <name>originTransactionID</name>
                                   <value><string>18</string></value>
        </member>
        <member>
                                   <name>originTimeStamp</name>
                                   <value><dateTime.iso8601>{date}00+0300</dateTime.iso8601></value>
        </member>
        <member>
                                   <name>transactionCurrency</name>
                                   <value><string>MGA</string></value>
        </member>
        <member>
                                   <name>adjustmentAmountRelative</name>
                                   <value><string>0</string></value>
        </member>
        <member>
                                   <name>originHostName</name>
                                   <value><string>VASP</string></value>
        </member>
        <member>
                                   <name>dedicatedAccountUpdateInformation</name>
                                   <value>
                                   <array>
                                   <data>
            <value>
            <struct>
                                                   <member>
                                                                   <name>dedicatedAccountID</name>
                                                                   <value><i4>998</i4></value>
                                                   </member>
                                                   <member>
                                                                   <name>dedicatedAccountValueNew</name>
                                                                   <value><string>200000</string></value>
                                                   </member>
                                                   <member>
                                                                   <name>dedicatedAccountUnitType</name>
                                                                   <value><int>1</int></value>
                                                   </member>
            </struct>
            </value>
                                   </data>
                                   </array>
                                   </value>
        </member>
        <member>
                                   <name>negotiatedCapabilities</name>
                                   <value>
                                   <array>
                                   <data>
                                                   <value><i4>64</i4></value>
                                   </data>
                                   </array>
                                   </value>
        </member>
    </struct>
    </value>
    </param>
    </params>
    </methodCall>\n\n""".format(msisdn=msisdn, date=my_date)

    response1 = requests.post(url, data=body1, headers=headers)  # print(body1)
    response2 = requests.post(url, data=body2, headers=headers)  # print(body2)
    response3 = requests.post(url, data=body3, headers=headers)  # print(body3)
    response4 = requests.post(url, data=body4, headers=headers)  # print(body3)
    #response = response1.text + "\n\n\n" + response2.text + "\n\n\n" + response3.text + "\n\n\n" + response4.text
    return response1.text, response2.text, response3.text, response4.text
