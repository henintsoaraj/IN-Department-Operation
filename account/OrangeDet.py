import os


CURRENT_DIRECTORY = os.getcwd()

def barring(msisdn,paramtype):
    x = []
    if paramtype == "STKB":
        with open('account/file/unbarringB.csv','w') as file, open('account/file/barringB.csv','w') as file1, open('account/file/rateOrangeDetaillant.txt','w') as ordet:
            for line in msisdn.splitlines():
                text = line.replace('\t',',')
                text = "+261" + text[1:]
                file.write(text.split(',')[0]+",,acl_rp2p_grossiste\n")
                file1.write(text+",acl_rp2p_detaillant\n")
    elif paramtype == "STKA":
        with open('account/file/unbarringA.csv','w') as file, open('account/file/barringA.csv','w') as file1, open('account/file/rateOrangeDetaillant.txt','w') as ordet:
            for line in msisdn.splitlines():
                text = line.replace('\t',',')
                text = "+261" + text[1:]
                file.write(text.split(',')[0]+",,acl_rp2p_detaillant\n")
                file1.write(text+",acl_rp2p_grossiste\n")
    