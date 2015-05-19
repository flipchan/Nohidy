import os
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

print"Hello master"
print"printing the connections the system is waiting for"
os.system("netstat -an | grep LISTEN ")

establishedportsmayybe =raw_input("Do you want me to show you the established connections on your system?Yes/No: ")
if establishedportsmayybe=="Yes":
    print"Master i am printing established connections to your system"
    os.system("netstat -an | grep ESTABLISHED ")
else:
    print"Master i am exiting"
    
print"remeber that if u have a weird port open you can allways use the port lookup tool to find out what it is"
print"and block the port to stop the attacker from using your system for bad stuff"
