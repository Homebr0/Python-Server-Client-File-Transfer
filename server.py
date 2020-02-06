#!/usr/bin/env python3
import socket
import sys
import os
from _thread import start_new_thread
import threading

HOST = "localhost"
PORT = int(sys.argv[1])  # The port used by the server
FILEPATH = str(sys.argv[2])
MIB = 13107200
count = 0
FileNum = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    if (PORT <= 1023):
        sys.stderr.write("Invalid port number\n")
        exit(1)

    sock.bind((HOST, PORT))
    sock.listen(10)
    print('Waiting for incoming connections on', sock)
    
    while True:
        conn, addr = sock.accept()
        count = count + 1
        print('Connected to ', addr)
