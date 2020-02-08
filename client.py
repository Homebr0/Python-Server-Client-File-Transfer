#!/usr/bin/env python3
import sys
import socket
from struct import pack

HOST = sys.argv[1]  # The server's hostname or IP address
PORT = int(sys.argv[2])  # The port used by the server
FILENAME = sys.argv[3]

if __name__ == '__main__':

    with open(FILENAME, 'rb') as readData:
        outData = readData.read()
    
    assert(len(outData))


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.settimeout(10)
            s.connect((HOST, PORT))
            s.settimeout(None)

            length = pack('>Q', len(outData))

            s.sendall(length)
            s.sendall(outData)
            
            s.close()
            s = None

        except:
            sys.stderr.write("ERROR: Connection not established\n")
            s.close()
            exit(1)