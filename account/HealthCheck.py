import paramiko
import pandas as pd
import io
import re

port = 22


def health_check(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -h"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'Use%': 'Use'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df
    #return lines.decode('utf-

def health_check2(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -i"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1,]], axis=1, inplace=True)
    df=df.rename(columns = {'IUse%':'IUse'})
    df=df.rename(columns = {'Mounted':'Mounted on'})
    df = df.astype(str)
    df['IUse'] = (df['IUse'].str.replace(r'\D', '')).astype(int)
    return df

"""def health_check3(server):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if server == "UAPUSAUPG01" or server == "UAPUSAUPG02":
        client.connect(serv.get(server), port, username_PG, password_PG)
    else:
        client.connect(serv.get(server), port, username, password)
    session = client.get_transport().open_session()
    cmd = "free -m"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    first_column = ['Mem:', '-/+', 'Swap:']
    df.insert(0, ' ', first_column)

    df = df.fillna(0)
    df['shared'] = df['shared'].astype(int).replace({0: ' '})
    df['buffers'] = df['buffers'].astype(int).replace({0: ' '})
    df['cached'] = df['cached'].astype(int).replace({0: ' '})
    return df"""

def health_check3(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -h"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'Use%': 'Use'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df


def health_checkIVR(myserver, myusername, mypassword):
    lst = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -h"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    for line in x.splitlines():
        lst.append(line)

    for i in lst:
        idx = lst.index(i)
        if i[0] == ",":
            lst[idx - 1] = lst[idx - 1] + lst[idx]
            del lst[idx]
    df = pd.DataFrame([sub.split(",") for sub in lst])
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'Use%': 'Use'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df

def health_check4(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -i"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'IUse%': 'IUse'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df = df.astype(str)
    #df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df


def health_checkIVR_Inodes(myserver, myusername, mypassword):
    lst = []
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -i"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    for line in x.splitlines():
        lst.append(line)

    for i in lst:
        idx = lst.index(i)
        if i[0] == ",":
            lst[idx - 1] = lst[idx - 1] + lst[idx]
            del lst[idx]
    df = pd.DataFrame([sub.split(",") for sub in lst])
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'IUse%': 'Use'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df = df.astype(str)
    df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df

def health_checkUSSD(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -h"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'Use%': 'Use'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df['Use'] = (df['Use'].str.replace(r'\D', '')).astype(int)
    return df

def health_checkUSSD_Inodes(myserver, myusername, mypassword):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(myserver, port, myusername, mypassword)
    session = client.get_transport().open_session()
    cmd = "df -i"
    stdin, stdout, stderr = client.exec_command(cmd)
    lines = stdout.read()
    client.close()
    text = lines.decode('utf-8')
    x = re.sub(' +', ',', text.strip())
    df = pd.read_csv(io.StringIO(x), sep=",")
    df.style.highlight_null(null_color='red')
    df.drop(df.columns[[-1, ]], axis=1, inplace=True)
    df = df.rename(columns={'IUse%': 'IUse'})
    df = df.rename(columns={'Mounted': 'Mounted on'})
    df = df.astype(str)
    df['IUse'] = (df['IUse'].str.replace(r'\D', '')).astype(int)
    return df