import os 
import random
import commands
import cmd

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

print""
print"ports like 80(web),8080(web),21(ftp),22(ssh),23(telnet),25(smtp,email)"
print"if you want to add an port to the file just open portslookup.txt and paste it in"
print"this is not a 100% bulletproff port searching program" 
print"But its pretty got damm awesome one"
print""

whichportmaster =raw_input("Which port are you looking for master?:  ")


def check():
    datafile = file('portslookup.txt')
    found = False
    for line in datafile:
        if whichportmaster in line:
            found = True
            break

check()
if True:
    print "Yeah port " + whichportmaster + " is in my register "
else:
    print "false"    


searchforthep =raw_input("Do you want to view the port Yes/No? ")
if searchforthep=="Yes":
    os.system("grep -r " + whichportmaster)
else: print"sry master something went wrong"
 
 