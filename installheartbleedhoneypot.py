import os
import sys
import commands

print""
print"Nohidy heartbleed honey pot installer "
print"downloads perl script that u have to run "
print""
installh =raw_input("Do you want me to download the honeypot?yes/no: ")
if installh == "yes":
			os.system("wget https://packetstormsecurity.com/files/126068/hb_honeypot.pl.txt ")
			print"heartbleed honeypot downloaded!"

else:
	print"okey i am exiting "
