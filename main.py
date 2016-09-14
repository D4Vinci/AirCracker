# Coded By SecFathy [ Mohamed K.Fathy ]
# Powerd Py Squnity Team 

print '''
  ___  _      _____                _             
 / _ \(_)    /  __ \              | |            
/ /_\ \_ _ __| /  \/_ __ __ _  ___| | _____ _ __ 
|  _  | | '__| |   | '__/ _` |/ __| |/ / _ \ '__|
| | | | | |  | \__/\ | | (_| | (__|   <  __/ |   
\_| |_/_|_|   \____/_|  \__,_|\___|_|\_\___|_|  

Basic Checker For AirDroid Users In Network  
                                               '''

import socket
import netaddr
import random

hosts = ["192.168.1.1"]
ports = [8888, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]
liveCounter = 0


for host in hosts:
    for port in ports:
        try:
            print "[+] Connecting to " + host + ":" + str(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, port))
            #banner = s.recv(1024) # Will cause a timeout w/o a response
            if result == 0:
                print "  [*] This User Is Using Airdroid On Port  " + str(port) + " Via Web!"
            s.close()
        except:
            pass
