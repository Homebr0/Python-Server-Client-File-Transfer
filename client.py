#!/usr/bin/env python3
import sys
import socket

HOST = sys.argv[1]  # The server's hostname or IP address
PORT = int(sys.argv[2])  # The port used by the server
FILENAME = sys.argv[3]

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            s.settimeout(10)
            s.connect((HOST, PORT))
            s.settimeout(None)
            sendFile = open(FILENAME, 'rb')
            outData = sendFile.read(1024)
            while outData:
                s.send(outData)
                outData = sendFile.read(1024)
            sendFile.close()

        except:
            sys.stderr.write("ERROR: Connection not established\n")
            s.close()
            exit(1)