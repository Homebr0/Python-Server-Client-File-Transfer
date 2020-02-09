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
    
    with open(fileName, 'wb') as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
        
    conn.close()
    
            
             

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
            
    

