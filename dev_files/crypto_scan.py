import random,
from base64 import *
from hashlib import *
from Crypto import *
import bz2
#

filen==raw_input('file?: ')
if not filen:
	dii = raw_input('dir?: ')
else:
	filepath = 
	pass



#rc4
def rc4crypt(data, key):
    """RC4 algorithm"""
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

def rc4decrypt(data, key, decode=b64decode, salt_length=16):
    """RC4 decryption of encoded data"""
    if decode:
        data = decode(data)
    salt = data[:salt_length]
    return rc4crypt(data[salt_length:], sha1(key + salt).digest())



#encodements
def b64d(st):
	return b64decode(st)

def bz2(st):
	return bz2.decompress(st)

#

#

#

#hail-mary run em all 
print 'giveing em hell'
