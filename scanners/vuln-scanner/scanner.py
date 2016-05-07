#!/usr/bin/python
# -*- coding: latin-1 -*-
import nmap
import sys, csv, os

try:
    nm = nmap.PortScanner()         # nmap alive?
except nmap.PortScannerError:
    print('Nmap not found, run apt-get install python-nmap', sys.exc_info()[0])
    sys.exit(1)

#
#Wrote this with an broken arm^^
#A big thanks to the ppl who support us and make TCS TCS, you are all part of our team, also a big thanks to 
#my friend and co admin of Cyberlove Ratheesh Raveendran
#https://www.facebook.com/TijiNostalgia/
#thnks to all friends old and new //Filip kälebo aka Flipchan

csvFile = 'output.csv'
xmlFile = 'output.xml'

print '''

▄▄▄▄▄ ▄▄· .▄▄ · 
•██  ▐█ ▌▪▐█ ▀. 
 ▐█.▪██ ▄▄▄▀▀▀█▄
 ▐█▌·▐███▌▐█▄▪▐█
 ▀▀▀ ·▀▀▀  ▀▀▀▀ 
             Team Cyberlove Security

			vulnerablity scanner
▄▄▄ .▐▄• ▄  ▄▄▄·▄▄▌        ▪  ▄▄▄▄▄▪   ▐ ▄  ▄▄ • 
▀▄.▀· █▌█▌▪▐█ ▄███•  ▪     ██ •██  ██ •█▌▐█▐█ ▀ ▪
▐▀▀▪▄ ·██·  ██▀·██▪   ▄█▀▄ ▐█· ▐█.▪▐█·▐█▐▐▌▄█ ▀█▄
▐█▄▄▌▪▐█·█▌▐█▪·•▐█▌▐▌▐█▌.▐▌▐█▌ ▐█▌·▐█▌██▐█▌▐█▄▪▐█
 ▀▀▀ •▀▀ ▀▀.▀   .▀▀▀  ▀█▄▀▪▀▀▀ ▀▀▀ ▀▀▀▀▀ █▪·▀▀▀▀ 
	the system
'''

#banner


#target
lehost = raw_input('Target?: ')
nm = nmap.PortScanner()
print '[*]Scan has started..'
nm.scan(hosts=lehost, arguments=' -F -sC -sV --data-length 23 ')
#while nm.still_scanning():
#	print 'The scanner is online and scanning ' + lehost
print nm.scaninfo() 
print '[*]scan done'
print 'result i found '
print('----------------------------------------------------')
print 'csv:'
print(nm.csv())
print('----------------------------------------------------')
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
    print('State : {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))


print
print('----------------------------------------------------')
print 
print 'runnin os scan'
if (os.getuid() == 0): #root?
    print('----------------------------------------------------')
    # Os detection (need root privileges)
    nm.scan(lehost, arguments="-O")
    if 'osmatch' in nm[lehost]:
        for osmatch in nm[lehost]['osmatch']:
            print('OsMatch.name : {0}'.format(osmatch['name']))
            print('OsMatch.accuracy : {0}'.format(osmatch['accuracy']))
            print('OsMatch.line : {0}'.format(osmatch['line']))
            print('')

            if 'osclass' in osmatch:
                for osclass in osmatch['osclass']:
                    print('OsClass.type : {0}'.format(osclass['type']))
                    print('OsClass.vendor : {0}'.format(osclass['vendor']))
                    print('OsClass.osfamily : {0}'.format(osclass['osfamily']))
                    print('OsClass.osgen : {0}'.format(osclass['osgen']))
                    print('OsClass.accuracy : {0}'.format(osclass['accuracy']))
                    print('')

    if 'fingerprint' in nm[lehost]:
        print('Fingerprint : {0}'.format(nm['127.0.0.1']['fingerprint']))


    # Vendor list for MAC address
    print('scanning localnet')
    nm.scan(lehost, arguments='-O')
    for h in nm.all_hosts():
        print(h)
        if 'mac' in nm[h]['addresses']:
            print(nm[h]['addresses'], nm[h]['vendor'])



print('----------------------------------------------------')
  #  if 'fingerprint' in nm[lehost]:
 #       print('Fingerprint : {0}'.format(nm[lehost]['fingerprint']))
#
   # print('scanning localnet')
   # nm.scan(lehost, arguments='-O')
  #  for h in nm.all_hosts():
 #       print(h)
#        if 'mac' in nm[h]['addresses']:
#            print(nm[h]['addresses'], nm[h]['vendor'])

print('----------------------------------------------------')
             
print
f = open(lehost  + 'output.csv','a')
f.write(nm.csv())
print '[*]scan saved..'
print '[*]converting file ...'


csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
xmlData.write('<csv_data>' + "\n")
rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else: 
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")
            
    rowNum +=1

xmlData.write('</csv_data>' + "\n")
xmlData.close()



#To do get service from scan and define it so we can search it
print '[*]data converted to xml!'
print '''

Lets hunt some exploits!

example: if they are runnin nginx 1.4.2
type nginx 1.4.2
 '''
print
theservice = raw_input('What are we looking for today?: ')
print
print '[*]running searches in csves and exploit archives..'
searchone = open('file1', 'r')
for line in searchone:
    if theservice in line: print line
else:
	print 'could not find it..'
print
print 'lookin in second archive to find more sploits..'
searchtwo = open('file2', 'r')
for line in searchtwo:
    if theservice in line: print line
print '[!]Done happy sploiting'
