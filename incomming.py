import socket

ip_address_machine='127.0.0.1'
port_1=3389
port_2=3306
port_3=31337
port_4=1337
port_5=4444

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip_address_machine, port_1))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip_address_machine, port_2))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip_address_machine, port_3))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip_address_machine, port_4))   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip_address_machine, port_5))
    s.close()     
    if(result == 0) :
        print ("Port ",port_to_try, "is open on machine ", ip_address_machine)
    else:
        print ("Port ",port_to_try, "is not open on machine ", ip_address_machine)
except:
    print("Machine is off")