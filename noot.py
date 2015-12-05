#!/usr/bin/env python
"""Module for the Nohidy framework
"""

import notify2
import os, sys

os.system("bash cooo.sh")
conr = 'connections.txt'
f = open(conr)

#netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n >> connections.txt'
#>>> tf = 'connections.txt'
#>>> f = open(tf)
#>>> f.read()
#'      1 176.34.135.167\n      1 176.34.155.23\n      1 188.121.36.239\n      1 54.152.180.212\n      1 64.233.165.95\n      1 Address\n      1 servers)\n      2 127.0.0.1\n      2 54.230.96.77\n'
#>>> print(_)
#    1 176.34.135.167
#    1 176.34.155.23
#    1 188.121.36.239
#    1 54.152.180.212
#    1 64.233.165.95
#    1 Address
#    1 servers)
#    2 127.0.0.1
#    2 54.230.96.77

# This must be called before using notify2
notify2.init("Nohidy")

# A number of stock 
n = notify2.Notification("Connection established from: ", f.read(), " ") # A stock icon name. For more icon
                    # options, see icon.py in this folder.
n.show()
