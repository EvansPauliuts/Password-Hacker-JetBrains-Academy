# write your code here
import sys
import socket


class PasswordHacker:
    def __init__(self):
        self.ip_address = ''
        self.port = 0
        self.send_message = ''
        self.args_value = []

    def args_module(self):
        args = sys.argv

        try:
            if len(args) != 4:
                print('The script should be called with three arguments')
            else:
                host = str(args[1])
                port = int(args[2])
                passwd = str(args[3])
                self.args_value = [host, port, passwd]
        except IndexError:
            print('The script should be called with three arguments')

    def create_socket(self):
        self.args_module()

        with socket.socket() as client_socket:
            hostname = self.args_value[0]
            port = self.args_value[1]

            try:
                client_socket.connect((hostname, port))
                client_socket.send(self.args_value[2].encode())

                response = client_socket.recv(1024)
                print(response.decode())
            except ConnectionRefusedError:
                print(response.decode())


password_hacker = PasswordHacker()
password_hacker.create_socket()
