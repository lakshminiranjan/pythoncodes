#!/bin/python3
#port scanner like nmap.
import sys
import socket
from datetime import datetime
#Define your target
if len(sys.argv) == 2:#argv is like $(n) where here we are assigning the n as 2
    target = socket.gethostbyname(sys.argv[1])#Translating a hostname to ipv4(With the help of this we can even give the hostnames
else:
    print("Invalid amount of arguments")
    print("To run: python3 scanner.py <ip>") 
    
#Addding a banner
print("-" * 50)
print("Scanning target : "+target)
print("Time started : "+str(datetime.now()))
print("-" * 50)

#Exceptions
try:
    for port in range(50,85):#trying to cnnect to a port b/w 50-85,if nothing is open wait for 1 sec and moving on
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))#returns an error indicator.(if port is not open it results 1 as o/p.
        if(result == 0):
            print("POrt {} is open".format(port))
        s.close()
        
except KeyboardInterrupt:#catch the exception(catch block in java)
    print("\nExiting program.")
    sys.exit()#clean exit of the program
    
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("\nCouldn't connect to the server.")#print comes into the attack only after a method or function get finishes.
    sys.exit()
        
