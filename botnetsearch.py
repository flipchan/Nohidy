import pycurl
import os
import commands
import libcurl

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
print"Botnet search tool / Botnet type finder by flipchan"

beforescan =raw_input("master do you want me to run an admin finder programm to help find the admin panel of botnet first?Yes/no: ")
      if beforescan=="Yes":
            try: 
                  os.system("python adminfind.py")
                  
