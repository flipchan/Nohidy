import os
import commands
import cmd
import smtplib

'''
Nohidy is a free software you could redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the Free Software Foundation either version 3.0 of the License or any later version.
Nohidy is free of charge but we accept donations(it would help if you donated both 
to flipchan and the Free Software Foundation).
Nohidy is distributed  in the hope that it will be useful, but WITHOUT ANY WARRANTY : 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
PARTICULAR PURPOSE see the GNU General Public License along with Nohidy. if not see <http://www.gnu.org/licenses>.
__author__ = "Filip kalebo"
__copyright__ = "Free Software Foundation"
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = "Filip kalebo"
__email__ = "flipchan@riseup.net"
__status__ = "still in developing"
'''

print"How to setup your putty logfile and send it from an gmail account"
print"first start PuTTY go to sections>Logging and select the options "
print"SSH packets and raw data ,Always overwrite it , Flush log file frequently,Omit known password fields ,Omit session data"
print"name the logfile to .txt instead of .log to help the program work faster also save it in the same directory that this program is saved in"
print"remeber that the attacker is looking for logfiles so name it something creative"
print""

logfillee =raw_input("Enter name of logfile: ")

fromusr =raw_input("From which emailaddress do u want to send it from?: ")
fromaddr = fromusr
tooaddress =raw_input("To which address do you want me to send the file to?: ")
toaddrs  = tooaddress
msg = ' Master here is your log file '

print"time to login to your gmail account"
enteruname =raw_input("Enter your username: ")
enteryapaswd =raw_input("Enter your password: ")
# Credz (if needed)
username = enteruname
password = enteryapaswd

from email.mime.text import MIMEText

# crack open a plain text (our logfile)
# the text file contains only ASCII characters.
fp = open(logfillee, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % logfillee
msg['From'] = me
msg['To'] = you

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()





