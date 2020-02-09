#!/usr/bin/env python3
import socket
import sys
import os
from _thread import *
from struct import unpack
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
    
    try:
        buffer = conn.recv(8)
        (length,) = unpack('>Q', buffer)
        data = b''
        print(fileName)
        while len(data) < length:
            to_read = length - len(data)
            data += conn.recv(4096 if to_read > 4096 else to_read)
            
    finally:
        conn.send(b'End')
        conn.close()

        with open(fileName, 'wb') as f:
            f.write(data)
            
             

if __name__ == '__main__':
    

    if (PORT <= 1023):
        sys.stderr.write("ERROR: Invalid port number\n")
        exit(1)

    sock.bind((HOST, PORT))
    sock.listen(5)
    
    
    while True:
        try:
            print('Waiting for incoming connections')
            conn, addr = sock.accept()
            
            
            count = count + 1
            print('Connected to ', addr)

            if (not os.path.exists(FILEPATH)):
                os.makedirs(FILEPATH)
            fileName = FILEPATH + '/' + str(count) + '.file'
            
            t = threading.Thread(target=sockThread, args=(conn,))
            
            t.start()
            t.join()

        except socket.timeout:
            sys.stderr.write('ERROR: Socket timeout\n')
            exit(1)

    sock.close()  
            
    

