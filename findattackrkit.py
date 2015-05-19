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

print""
print"if u think ur apart of a botnet or have malware on your system i will try to find it!"
print"if u have an established connection to an unknown server you might be apart of someones botnet"
print"1 for shellfinder or 2 if i should find out what kind of botnet ur apart of "
print""
whatsup =raw_input("Do you want me to do find shell or locate the botnet?1 or 2: ")
if whatsup=="1":
    print"Getting shellfinder program"
    os.system("perl shellfinder.pl")
    
if whatsup=="2":
    print"using google dorks to find what part of botnet your apart of"
    #dorks intitle:login etc etc
    os.system("python botnetsearch.py")
else:
    print"I am exiting the mission master"