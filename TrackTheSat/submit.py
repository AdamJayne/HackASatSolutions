import sys
import socket
import time
from Utils import challenge_parser

import do_calc

host = "trackthesat.satellitesabove.me"
port = 5031
ticket = b"ticket{sierra76499foxtrot:GPGqaO4Dv2OiJ0iK_8J5FRLjpG-Yk3PPYQHo7NZd3iR9lrkL02eVHfMXnunozCIjdA}"

def netcats(host, port, content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(content)
    time.sleep(1)
    sock.shutdown(socket.SHUT_WR)

    response = ''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data.decode()

    print(response)

    sock.listen()
    
    # grab values to calculate
    sat, lat, lng, timeer = challenge_parser.parse(response)
    
    response_string = do_calc.solve_things(sat, lat, lng, float(timeer))


    sock.sendall(response_string.encode("utf-8"))

    sock.shutdown(socket.SHUT_WR)
    
    response2 = ''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response2 += data.decode()
    
    print(response2)
    print('Closing connection...')
    sock.close()

netcats(host, port, ticket)

