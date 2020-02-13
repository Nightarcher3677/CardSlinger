import socket
import time
import random

randport = random.randint(1000, 9999)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), randport))
s.listen(5)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('Server Online')
print('Hostname: ', host_name)
print('IP: ', host_ip)
print('Port: ', randport)
print('')
while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established!")
    clientsocket.send(bytes('Welcome to the server!', "utf-8"))
    #reset = open('availableconnections.txt', 'w')
    #reset.write(str(address))
    #ips = open('availableconnections.txt', 'r')
    #print('Available IPs ', ips.read())
