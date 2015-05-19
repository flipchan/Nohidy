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

#unix n linux logfile catcher

print"Checks your unix n linux logs and runs the rkhunter and chkrootkit"
print"U need rkhunter plus chkrootkit for this"



viewlastlog =raw_input("Wanna check the quick recent log Yes/No?: ")
if viewlastlog=="No":
        print"Oki dokey"
else:
        os.system("lastlog")

print"lets copy the kernal logfile in to this dir so we could upload it later"        
print"for exampel enter the folder of nohidy"
kernallogz =raw_input("Enter current directory: ")
print"fetching kernal logfile"
os.system("cp /var/log/kern.log " + kernallogz)

print"moving to authentication logfile master"
authlogfilee =raw_input("Master do you want me to send my mens to get the authentication logfile Yes/No: ")      
if authlogfilee=="Yes":
                os.system("cp /var/log/auth.log " + kernallogz) 

rkhunter =raw_input("Do you want me to go and get rkhunter master?Yes/No: ")
if rkhunter=="Yes":
        print"I am updateing and running rkhunter master"
        os.system("rkhunter --update && rkhunter --check")
else:
        print"procceding to next stage"

chkrootkit= raw_input("Master do you want me make an check?Yes/No: ")
if chkrootkit=="Yes":
        print"Running chkrootkit master"
        os.system("chkrootkit")
else:
        print"i am exiting master"
        
