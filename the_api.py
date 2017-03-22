import socket
import sys
import time

# t1 = time.time()
# s = socket.socket(socket.AF_UNIX, socket.SOCK_SEQPACKET)
# t2 = time.time()
# sock_file = "/tmp/hello_model.sock"
# t3 = time.time()
# name = sys.stdin.read().encode()
# t4 = time.time()
# s.connect(sock_file)
# t5 = time.time()
# s.send(name)
# t6 = time.time()
# data = s.recv(5242880)
# t7 = time.time()
# s.close()
# t8 = time.time()
# print(data.decode())
# print('Raw timers:', t1, t2, t3, t4, t5)
# print('Intervals:\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(t2-t1, t3-t2, t4-t3, t5-t4, t6-t5, t7-t6, t8-t7))
# print('Total:', t8-t1)

times = list()

for i in range(10000):
    t1 = time.time()
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    t2 = time.time()
    sock_file = "/tmp/hello_model.sock"
    t3 = time.time()
    name = sys.stdin.read().encode()
    t4 = time.time()
    s.connect(sock_file)
    t5 = time.time()
    s.send(name)
    t6 = time.time()
    data = s.recv(5242880)
    t7 = time.time()
    s.close()
    t8 = time.time()
    times.append(t8 - t1)

print(sum(times)/len(times))
