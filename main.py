import os
import thread
import threading
import time 
import cmd
import commands
from update import Updater


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


#botnetdorks find out what botnet i am apart of

print"Welcome nohidy auditing system for windows,unix and linux auditing and managment"
print""
print"                 ~~~~~~~~~~Coded by flipchan~~~~~~~~~~"
print"                          Nohidy  version 1.0"
print"        this version is in command line interface, gui is coming soon! "
#print"bs text"

#def check():
#   bstest =raw_input("sssdfsdfsdf: ")
#    print"bs"
#except KeyboardInterrupt:
#   print "\n\nC " + bcolors.RED+"ya" + bcolors.ENDC+" next time cowboy.\n"
#bcolors.RED for flipchan
#temperature
#this toolkit is so u can check ur servers quick then go n do fun stuff like code^^

print""
print"I am Nohidy coded by flipchan here to serve you master"
print""
print"Select from the meny:"
print"1 to see my connections"
print"2 log file managment/rootkitfinding"
print"3 configuring PuTTY for win and send a copy of the log file to your email"
print"4 launch linux firewall to block ports"#gufw
print"5 for port look up test"#portiinng
print"6 for tracing ip"#whois 
print"7 for packet sniffing/arp poisoning (still in beta testing not 100%working)"
print"8 for extra trix for the little extra"
print"9 find shells and botnets, if u think u r in a botnet find out what botnet!"
print"10 update me"
print"11 for Help,donateing and About"
print""
picaprogramtorun =raw_input("What do you want me to do master?: ")

print""

if picaprogramtorun=="1":
    print"viewing your connections"
    os.system("python yowhoisonemysystem.py")
    
if picaprogramtorun=="2":
    print"Goin to log file managments and rootkit finding"
    os.system("python unix-linuxlogs.py")
    
if picaprogramtorun=="3":
    print"Config Putty for windows and sending a copie of "
    os.system("python gmailsmtp.py")
    
if picaprogramtorun=="4":
    print"Launching Linux firewall master"
    os.system("python linuxfirewall.py")
    
if picaprogramtorun=="5":
    print"Launching portlookup tool"
    os.system("cd ports && python portinggg.py")
    
if picaprogramtorun=="6":
    print"Traceing ip address of attacker!"
    os.system("python lookuptest.py")

if picaprogramtorun=="7":
    print"starting packet sniffing/arp spoofing"
    os.system("python arp.py")

if picaprogramtorun=="8":
    print"opening trix folder master"
opentrix =os.system("gnome-open trix")
      if opentrix=False                                     #fix
try:
            os.system("explorer trix")              #windows open

if picaprogramtorun=="9":                                   #change botnet dorks
    print"Time to find shells and botnets master"
    os.system("python findattackrkit.py")
    
if picaprogramtorun=="10":
    print"checking for updates master"
    os.system("python update.py")

if picaprogramtorun=="11":
    print"Getting help master"
openhelp =os.system("gnome-open Help")
     if openhelp=False
try:
    os.system("explorer Help")                        #windows open 

#else: 
#    print"i am sorry master i did not get that"