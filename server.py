import socket


class s_func:

    def server_program(hp, data):
        # get the hostname

        host = socket.gethostname()
        port = 5000  # initiate port no above 1024
        hp = 50 #for testing

        print('IP: ', host)
        print('port: ', port)

        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode("utf-8")
            if not data:
                # if data is not received break
                break
            if 'dmg' in data:
                dmg_received = data.split(' ')[-1].strip()
                print('damage received:', dmg_received)
                hp -= int(dmg_received)
                return f'dmg {hp}'
                data2 = 'enemyhp ' + str(hp)
                conn.send(bytes(data2, "utf-8"))

            elif 'hp' in data and not 'ehp':
                hp_received = data.split(' ')[-1].strip()
                return f'ehp {hp_received}'

            elif 'ehp' in data:
                ehp_received = data.split(' ')[-1].strip()
                print('enemy hp:', ehp_received)
            print("from connected user: " + str(data))
            #data = input(' -> ')
            conn.send(bytes(data, "utf-8"))  # send data to the client

        conn.close()  # close the connection

    def client_program(message, hp, host, port):
        #host = input('please enter the hostname: \n')  # as both code is running on same pc
        #port = int(input('please enter the port: \n'))  # socket server port number


        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, int(port)))  # connect to the server



        #message = input(" -> ")  # take input


        client_socket.send(message.encode("utf-8"))  # send message
        data = client_socket.recv(1024).decode("utf-8")  # receive response
        if 'dmg' in data:
            dmg_received = data.split(' ')[-1].strip()
            print('damage received:', dmg_received)
            hp -= int(dmg_received)
            return f'dmg {hp}'
            data2 = 'enemyhp ' + str(hp)
            conn.send(bytes(data2, "utf-8"))

        elif 'hp' in data and not 'ehp':
            hp_received = data.split(' ')[-1].strip()
            return f'ehp {hp_received}'

        elif 'ehp' in data:
            ehp_received = data.split(' ')[-1].strip()
            print('enemy hp:', ehp_received)

        print('Received from server: ' + data)  # show in terminal
        #message = ''
        #message = input(" -> ")  # again take input

        #client_socket.close()  # close the connection


#if __name__ == '__main__':
#    server_program()
