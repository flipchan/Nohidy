import os
import sys
import commands

print"Nohidy's honey pot installer "
print""
print"An normal good honeypot for your servers costs around  $599USD "
print"Nohidy have searched and found 2 great opensources ones"
print""
print"Enter 1 to install heartbleed honeypot"
print""
print"Enter 2 to install trustedsec's artillery"
print""
print""

whichone =raw_input("Master which one do you which me to install?1/2: ")
if whichone == "1":
			print"installing heartbleed honeypot"
			os.system("python installheartbleedhoneypot.py")	

if whichone == "2":
			print"installing trustedsec's artillery"
			os.system("python trustedsechoneypot.py")
else:
	print"exiting.."
