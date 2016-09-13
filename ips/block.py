import sys, os

f = open("ips.txt","r")
for line in f:
	strr = str('iptables -A INPUT -s ' + line + ' -j DROP')
	os.system(strr)
	st = str('iptables -A OUTPUT -s ' + line + ' -j DROP')
	os.system(st)
	print 'Blocked: ' + line

print 'done'
