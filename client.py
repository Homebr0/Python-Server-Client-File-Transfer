#!/usr/bin/env python3
import sys
import socket

HOST = sys.argv[1]  # The server's hostname or IP address
PORT = int(sys.argv[2])  # The port used by the server
FILENAME = sys.argv[3]

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #print(s)
        s.connect((HOST, PORT))
        #print(s)