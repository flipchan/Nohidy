#!/usr/bin/python
# -*- coding: latin-1 -*-
import nmap
import sys, csv

#
#Wrote this with an broken arm^^
#

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
nm.scan(hosts=lehost, arguments='-O -F -sC -sV --data-length 23 ')
print nm.scaninfo() 
print '[*]scan done'

f = open('output.csv','a')
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
print '[*]running searches in csves and exploit archives..'
searchone = open('file1', 'r')
for line in searchone:
    if 'service here' in line: print line
else:
	print 'could not find it..'
print
print 'lookin in second archive to find more sploits..'
searchtwo = open('file2', 'r')
for line in searchtwo:
    if 'service here' in line: print line
print '[!]Done happy sploiting'
