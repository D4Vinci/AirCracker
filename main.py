#!/usr/bin/env python
# Coded By SecFathy [ Mohamed K.Fathy ] and Developed By D4Vinci [ karim shoair ]
# Powerd Py Squnity Team
import socket, requests
from threading import *
global u
ports = [8888, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]
screenLock = Semaphore(value=1)
def Scan(host,port):
	global u
	try:
		u = requests.get("http://{}:{}".format( host, port ) )
		if u.status_code == 200 :
			screenLock.acquire()
			print "\n ------------------------"
			print "\n Found device "+str(host)
			print "\n Url -->> http://{0}:{1} ".format( host, port )
			print "\n Airdroid version -->> " + str(u.content.split("version: \"")[1].split("\"")[0].lower().replace("v",""))
		u.close()
	except:
		screenLock.acquire()
		#print "\n " + host + " Offline"
	finally:
		screenLock.release()

#Get Local ip
s = socket.socket()
s.connect(("gmail.com",80))
local = str(s.getsockname()[0])
s.close()
splited = local.split(".")

print '''
  ___  _      _____                _
 / _ \(_)    /  __ \              | |
/ /_\ \_ _ __| /  \/_ __ __ _  ___| | _____ _ __
|  _  | | '__| |   | '__/ _` |/ __| |/ / _ \ '__|
| | | | | |  | \__/\ | | (_| | (__|   <  __/ |
\_| |_/_|_|   \____/_|  \__,_|\___|_|\_\___|_|

Basic Checker For AirDroid Users In Network\n'''

print "--- --"*5
print "[*] Scanning.."
for port in ports :
	for i in range(2, 256):
		ip = str(splited[0]+"."+splited[1]+"."+splited[2]+"."+str(i))
		try:
			t = Thread(target=Scan, args=(ip ,port))
			t.start()
		except:
			Scan(ip ,port)
print "\n[*] Scan finished..\n"
