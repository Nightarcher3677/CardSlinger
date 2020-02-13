import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

chooseport = (input('Enter Port:'))
#choosehostname = input('Enter IP: ')

s.connect((socket.gethostbyname(socket.gethostname()), int(chooseport)))

while True:
    msg = s.recv(1028)
    print(msg.decode("utf-8"))
