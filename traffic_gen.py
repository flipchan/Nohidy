#
#created by flipchan to make it harder for people to 
#perform "timing attacks" where they try to timestamp the data to
#help deanonymize, traffic obfusication and simular systems, originally written
#for the layerprox project but feel free to hack it in anyway you want

import urllib2, httplib
import datetime, time
from random import randint #not great but this is only a beta version, i could mix it with the day gen in otw
from random_words import RandomWords #https://pypi.python.org/pypi/RandomWords/0.1.5
from otw import genday
rw = RandomWords()
#put it in a loop n run with sysd or something simular



def genip():
	f = randint(1,254)
	i = randint(1,254)
	r = randint(1,254)
	s = randint(1,254)
	t = str(f + '.' + i + '.' + r + '.'  + s)
	ip = int(t)
	return ip

while 1:
	host = genip()
	conn = httplib.HTTPConnection(host)
	where = str(rw.random_word() + '.html')#make it look legit with a "random" word
	conn.request("HEAD","/index.html")
	time.sleep(100)# make this a randomly-generated int

