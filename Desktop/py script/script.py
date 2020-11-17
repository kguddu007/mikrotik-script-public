import paramiko
import time
import pyfiglet 
 
result = pyfiglet.figlet_format("AIRJALDI") 
print(result)

ipaddress='192.168.55.1'
user='admin'
passwd='lbdlbdindia!@#$'
port=22

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(ipaddress, port, user, passwd)
stdin, stdout, stderr = ssh_client.exec_command('ip address add address=10.10.10.1/29 interface=bridge1')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip dns set server=1.1.1.1')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip address print')
output = stdout.readlines()
print('\n' .join(output))
ssh_client.close()