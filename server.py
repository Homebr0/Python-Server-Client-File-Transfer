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
count = 1

print_lock = threading.Lock()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sockThread(conn):
    
    with open(fileName, 'wb') as f:
        while True:
            try:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
            except conn.timeout:
                print('ERROR: Socket timeout')
                with open(fileName, 'wb') as errFile:
                    errFile.write('ERROR')
                    break

    conn.close()
    
            
             

if __name__ == '__main__':
    

    if (PORT <= 1023):
        sys.stderr.write("ERROR: Invalid port number\n")
        exit(1)

    
    try:
        if (not os.path.exists(FILEPATH)):
            os.makedirs(FILEPATH)
        fileName = FILEPATH + '/' + str(count) + '.file'
        sock.settimeout(5)
        sock.bind((HOST, PORT))
        sock.listen(5)
        while True:
        
            print(sock)
            
            fileName = FILEPATH + '/' + str(count) + '.file'
            count = count + 1

            print('Waiting for incoming connections')
            conn, addr = sock.accept()
            conn.settimeout(10)
            
            
            print('Connected to ', addr)

            t = threading.Thread(target=sockThread, args=(conn,))

            t.start()

            t.join()

    except socket.timeout:
        sys.stderr.write('ERROR: Socket timeout\n')
        
        with open(fileName, 'wb') as errFile:
            errFile.write(b'ERROR')
        exit()

    sock.close()  
            
    

