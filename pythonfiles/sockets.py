#!/bin/python3
#Sockets-utilising sockets to connect from one node to other node.
import socket

HOST = '127.0.0.1'
PORT = 1111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#This line 8 syntax is very common for all sockets.(AF-IPV4,SOCK_Strm-Port)
s.connect((HOST,PORT))#Making a connection.
