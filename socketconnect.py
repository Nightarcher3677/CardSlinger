import socket
import sys
from time import sleep

class s_func:
    def send(data, HOST, PORT):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if data:
            try:
                sock.connect((HOST, PORT))
                sock.send(bytes(data, "utf-8"))
                received = sock.recv(1024)

                sleep(1)

                sock.send(bytes(data, "utf-8"))
                received = sock.recv(1024)

                sleep(1)

                sock.send(bytes(data, "utf-8"))
                received = sock.recv(1024)

            finally:
                sock.close()
s_func.send('test', '127.0.0.1', 1235)
