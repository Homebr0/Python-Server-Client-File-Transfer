#!/usr/bin/env python3
import socket
import sys
import os
from _thread import *
import threading 

HOST = "localhost"
PORT = int(sys.argv[1])  # The port used by the server
FILEPATH = str(sys.argv[2])
MIB = 13107200
fileName = ''
count = 0

print_lock = threading.Lock()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sockThread(conn):
    while True:

        data = conn.recv(MIB)

        with open(fileName, 'wb') as f:
            f.write(data)
            data = conn.recv(MIB)

            if not data:
                conn.send(b'End')
                print_lock.release()
                break
            
    conn.close()



if __name__ == '__main__':
    

    if (PORT <= 1023):
        sys.stderr.write("ERROR: Invalid port number\n")
        exit(1)

    sock.bind((HOST, PORT))
    sock.listen()
    
    
    while True:
        try:
            print('Waiting for incoming connections')
            conn, addr = sock.accept()
            
            print_lock.acquire()
            count = count + 1
            print('Connected to ', addr)

            if (not os.path.exists(FILEPATH)):
                os.makedirs(FILEPATH)
            fileName = FILEPATH + '/' + str(count) + '.file'
            
            start_new_thread(sockThread, (conn,))

        except socket.timeout:
            sys.stderr.write('ERROR: Socket timeout\n')
            exit(1)

    sock.close()
    

