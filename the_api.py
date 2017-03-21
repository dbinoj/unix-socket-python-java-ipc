import socket
import sys

s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)

sock_file = "/tmp/hello_model.sock"

name = str.encode(sys.argv[1])
length = str(len(sys.argv[1])).encode()

s.connect(sock_file)

s.send(name)

data = s.recv(1024)
s.close()

print('Received ' + repr(data))
