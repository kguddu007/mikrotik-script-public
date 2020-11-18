import paramiko
import time
import pyfiglet 
import json
from colorama import Fore, Back, Style 
 
creditBanner = pyfiglet.figlet_format("AIRJALDI") 
print(creditBanner)

ipaddress=open("ip-file.txt", "r")
user='admin'
passwd=''
port=22
ipList = ipaddress.readlines()
x=len(ipList)
if ipaddress and x>0:
    for ipVal in ipList:
        try:
            host = ipVal.strip()
            ssh_client=paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(host, port, user, passwd)
            stdin, stdout, stderr = ssh_client.exec_command('ip address add address=10.10.10.1/29 interface=bridge1')
            time.sleep(1)
            stdin, stdout, stderr = ssh_client.exec_command('ip dns set server=1.1.1.1')
            time.sleep(1)
            stdin, stdout, stderr = ssh_client.exec_command('ip address print')
            output = stdout.readlines()
            ssh_client.close()
            print(Fore.GREEN+"[SUCCESS]:"+ host)
            print(Style.RESET_ALL)  
            ipaddress.close()
        except:
            print(Fore.RED+"[FAILED]:"+ host)
            print(Style.RESET_ALL)
            ssh_client.close()  
else:
    print('INFO: Please add ip addresses in ip-file.txt')
