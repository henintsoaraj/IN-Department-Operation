import paramiko
from datetime import datetime, timedelta
import os
import csv
import glob
import sys
import pandas as pd
import io
import re




def search(sender, receiver, startdate, enddate, smtype):
    host = "10.111.30.204"
    port = 22
    username = "taskmng"
    password = "Atae_123"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port, username, password)
    session = client.get_transport().open_session()
    x = ""
    p = 0
    liste = []
    liste2 = []

    if (sender != "" and receiver == ""):
        while (x != enddate):
            x = (datetime.strptime(startdate, '%Y%m%d') + timedelta(days=p)).strftime('%Y%m%d')
            liste.append(x)
            p = p + 1

        if smtype == "Mo":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/11/" + y + "/prm*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | awk -F\",\" \'{print$1\",\"$2\",\"$3\",\"$59\",\"$22\",\"$18\",\"$20\",\"$20\",\"$26\",\"$53}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 0), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['SM ID'])

            return x

        if smtype == "Mt":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/12/" + y + "/prm*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | awk -F\",\" \'{print$1\",\",$2\",\"$3\",\"$14\",\"$20\",\"$15\",\"$16\",\",$17\",\"$26\",\"$27\",\"$22}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account",
                                                                "Deliver Count"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 0), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['Start Time'])

            return x

        if smtype == "CheckBill":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/checkbill/" + y + "/SMC*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | awk -F\",\" \'{print$2\",\",$3\",\"$7\",\"$11\",\"$12\",\"$17\",\"$18\",\",$19\",\"$23\",\"$24\",\"$33}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account",
                                                                "Deliver Count"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 1), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['SM ID'])

            return x

    if (sender != "" and receiver != ""):
        while (x != enddate):
            x = (datetime.strptime(startdate, '%Y%m%d') + timedelta(days=p)).strftime('%Y%m%d')
            liste.append(x)
            p = p + 1

        if smtype == "Mo":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/11/" + y + "/prm*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | zgrep " + receiver + " | awk -F\",\" \'{print$1\",\"$2\",\"$3\",\"$59\",\"$22\",\"$18\",\"$20\",\"$20\",\"$26\",\"$53}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 0), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['SM ID'])

            return x

        if smtype == "Mt":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/12/" + y + "/prm*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | zgrep " + receiver + " | awk -F\",\" \'{print$1\",\",$2\",\"$3\",\"$14\",\"$20\",\"$15\",\"$16\",\",$17\",\"$26\",\"$27\",\"$22}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account",
                                                                "Deliver Count"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 0), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['SM ID'])

            return x

        if smtype == "CheckBill":
            for y in liste:
                com = "/home/taskmng/bill/backup/cursite/451/SMApp/checkbill/" + y + "/SMC*"
                liste2.append(com)
            cmd = "zgrep -h " + "\"" + sender + "\"" + " " + ' '.join(
                liste2) + " | zgrep " + receiver + " | awk -F\",\" \'{print$2\",\",$3\",\"$7\",\"$11\",\"$12\",\"$17\",\"$18\",\",$19\",\"$23\",\"$24\",\"$33}\'"
            stdin, stdout, stderr = client.exec_command(cmd)
            lines = stdout.read()
            client.close()
            text = lines.decode('utf-8')
            x = re.sub(' +', ',', text.strip())
            df = pd.read_csv(io.StringIO(text), sep=",", names=["SM ID", "Sender", "Receiver", "Start Time",
                                                                "Stop Time", "SM length", "SM status", "Error Code",
                                                                "Original Account", "Destination Account",
                                                                "Deliver Count"])

            # df = df.astype(str)
            df.loc[(df["SM status"] == 1), ('SM status')] = "Success"
            df.loc[(df["SM status"] != "Success"), ('SM status')] = "Failed"
            x = df.sort_values(by=['SM ID'])
            return x
