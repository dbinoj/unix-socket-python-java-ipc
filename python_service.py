import os
import socketserver
import socket
import time

sock_file = "/tmp/hello_model.sock"


class HelloModel(socketserver.BaseRequestHandler):
    def handle(self):
        t1 = time.time()
        self.data = self.request.recv(5242880).strip()
        data_str = bytes.decode(self.data)
        # Processing starts
        resp_str = "Hello, {}!".format(data_str)
        # Processing ends
        self.request.sendall(str.encode(resp_str))
        t2 = time.time()
        print("{}s".format(t2-t1))


class ThreadingUnixStreamServer(
    socketserver.ThreadingMixIn, socketserver.UnixStreamServer
):
    socket_type = socket.SOCK_STREAM

if __name__ == "__main__":
    if os.path.exists(sock_file):
        os.remove(sock_file)

    server = ThreadingUnixStreamServer(sock_file, HelloModel)
    server.serve_forever()
