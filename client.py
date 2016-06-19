# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while(1):
    message = raw_input("> ")
    if message == "END":
        break
    else:
        s.sendall(message)
        data = s.recv(1024)
        print '==', data
s.close()
