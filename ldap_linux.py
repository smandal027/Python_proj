import paramiko
import socket
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = "something.net"
port = 22
username = "test"
password = "password"
ssh.connect(host, port, username, password)
ssh.exec_command('sudo yum install sssd sssd-tools')
ssh.exec_command('cp /etc/ldap.conf /etc/ldap_orig')
sftp = ssh.open_sftp()
fileObject = sftp.file('/etc/ldap.conf','a')
ldap_line='ldap://server-fqdn:389'
fileObject.write(ldap_line)
ssh.exec_command('mv /etc/nsswitch.conf /etc/nsswitch_orig')
fileObject_nss = sftp.file('/etc/nsswitch.conf','w')
nss_line=['passwd: files sss\n','group: files sss\n','shadow = files sss\n']
fileObject_nss.write(nss_line)
ssh.exec_command('sudo systemctl start sssd')
