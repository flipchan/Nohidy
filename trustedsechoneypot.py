import os 
import commands
import sys

print"Nohidy"
print"installs honeypot: trustedsec's artillery"
print"The Artillery Project is an open-source blue team tool designed to protect Linux and Windows operating systems through multiple methods. "
print"Supported on Windows and Linux"
print""
print"if u got mac u need to install git (http://git-scm.com/downloads)"

installart =raw_input("Do you want me to install artillery?yes/no: ")
if installart == "yes":
	print"creates dir and clones it in to artillery"
	os.system("git clone https://github.com/trustedsec/artillery.git ")

else:
	print"exiting.."
