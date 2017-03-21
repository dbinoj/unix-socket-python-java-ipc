import os
import socketserver
import socket
# import time

sock_file = "/tmp/hello_model.sock"


class HelloModel(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        data_str = bytes.decode(self.data)
        # for i in range(5):
        #     time.sleep(1)
        #     print(i)
        resp_str = "Hello, {}".format(data_str)
        self.request.sendall(str.encode(resp_str))


class ThreadingUnixStreamServer(
    socketserver.ThreadingMixIn, socketserver.UnixStreamServer
):
    socket_type = socket.SOCK_SEQPACKET

if __name__ == "__main__":
    if os.path.exists(sock_file):
        os.remove(sock_file)

    server = ThreadingUnixStreamServer(sock_file, HelloModel)
    server.serve_forever()
    # server_thread = threading.Thread(target=server.serve_forever)
    # server_thread.daemon = True
    # server_thread.start()
    # print("Server running in thread: ", server_thread.name)
