import sys
import socket
import time
from Utils import challenge_parser

import do_calc

host = "trackthesat.satellitesabove.me"
port = 5031
ticket = b"ticket{sierra76499foxtrot:GPGqaO4Dv2OiJ0iK_8J5FRLjpG-Yk3PPYQHo7NZd3iR9lrkL02eVHfMXnunozCIjdA}"

class MySocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

def netcats(host, port, content):
    my_sock = MySocket()
    my_sock.connect(host, port)

    my_sock.mysend(content)
    response = my_sock.myreceive()
    response = response.decode()

    print(response)

    response = ''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data.decode()

    print(response)

    
    # grab values to calculate
    sat, lat, lng, timeer = challenge_parser.parse(response)
    
    response_string = do_calc.solve_things(sat, lat, lng, float(timeer))

    # sock.connect((host, port))

    print('Closing connection...')
    sock.close()

netcats(host, port, ticket)

