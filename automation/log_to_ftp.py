#!/usr/bin/python
#auto upload logfiles to ftp server
import ftplib
import os
from datetime import date
import time

ip = ''
logfile = ''
user = ''
password = ''
logfile = ''
ftpdir = ''
localdir = ''

while 1:
	filename = logfile
	ftp = ftplib.FTP(ip)
	ftp.login(user, password)
	today = date.today()
	filename = str(today) + filename
	ftp.cwd(ftpdir)
	os.chdir(localdir)
	myfile = open(filename, 'r')
	ftp.storlines('STOR ' + filename, myfile)
	myfile.close()
	time.sleep(86000)
