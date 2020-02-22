import socket

class c:
    hp = 50
    def client_program(message):
        global hp
        host = input('please enter the hostname: \n')  # as both code is running on same pc
        port = int(input('please enter the port: \n'))  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server

        #message = input(" -> ")  # take input

        while message.lower().strip() != 'bye':
            client_socket.send(message.encode("utf-8"))  # send message
            data = client_socket.recv(1024).decode("utf-8")  # receive response
            if 'dmg' in data:
                dmg_received = data.split(' ')[-1].strip()
                print('damage received:', dmg_received)
                hp -= int(dmg_received)
                print('hp: ', hp)
                data2 = 'enemyhp ' + str(hp)
                conn.send(bytes(data2, "utf-8"))

            elif 'hp' in data and not 'ehp':
                hp_received = data.split(' ')[-1].strip()
                print('hp:', hp_received)

            elif 'ehp' in data:
                ehp_received = data.split(' ')[-1].strip()
                print('enemy hp:', ehp_received)

            print('Received from server: ' + data)  # show in terminal
            #message = ''
            #message = input(" -> ")  # again take input

        client_socket.close()  # close the connection


if __name__ == '__main__':
    c.client_program('dmg 567')
