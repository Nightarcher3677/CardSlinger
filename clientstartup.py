import socket #now for the client. once again, we import socket, since this is a new script and is seperate from the server.py script
import os, sys
IP = input("Please enter the host's IP (you will have to do this twice): ") #this asks the user for the ip address. in this case, it's 127.0.0.1, but we want to have some flexibility
PORT = input("Please enter the port of the host:") #this does the same thing, but this time with the port instead. in this case it's 9999
from client import clientpy


class s_client:
    def client(IP, PORT, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((IP, int(PORT))) #this connects us to our chosen IP and PORT
            s.sendall(bytes(message, "utf-8")) #this encodes our message, then sends it to our client
            data = s.recv(1024) #once again, our buffer size is 1024, and the data that we receive is encoded, so we need to decode it and print it

        print('received', data.decode("utf-8")) #we do that here, and then print out (onto the console) the result. it should give us our typed in message

#running code below
message = 'startup'
clientpy.startup(IP, PORT)
s_client.client(IP, PORT, message)
os.system('exit')
