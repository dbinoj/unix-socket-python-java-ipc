import socket
import sys

s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)

sock_file = "/tmp/hello_model.sock"

name = sys.stdin.read().encode()

s.connect(sock_file)

s.send(name)

data = s.recv(5242880)
s.close()

print('Received ' + data.decode())
