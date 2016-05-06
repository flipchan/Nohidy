import nmap
import sys, csv

#
#Wrote this with an broken arm^^
#

csvFile = 'output.csv'
xmlFile = 'output.xml'


#banner
lehost = raw_input('Target?: ')
nm = nmap.PortScanner()
print 'Scan has started..'
nm.scan(lehost, '10-4000')
print 'scan done'

f = open('output.csv','a')
f.write(nm.csv())
print 'scan saved..'
print 'converting file ...'


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

print 'data converted to xml!'
print 'running searches in csves and exploit archives..'
