#part of the Nohidy toolkit
import requests
import notify2, time

#script to notife check if vpn brakes

public_ip = ''

notify2.init("Nohidy")

while 1:
	if not hidden_ip == requests.get('https://canihazip.com/s').text:
		n = notify2.Notification("IP has changed")
		n.show()
	time.sleep(10)
