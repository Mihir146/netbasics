import socket
import sys


s = socket.socket()


def srvr(portnum):
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', portnum))
    s.listen()
    while 1:
        fd, addr = s.accept()
        new_sock = fd
        request = b""
        while 1:
            # request += new_sock.recv(8)
            request = new_sock.recv(8)
#            if (request & ((1 << 33)-1).to_bytes(4096, 'big') == b"\r\n\r\n"):
#                break

            if (request == b"\r\n\r\n"):
                break
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\n\r\nHello!"
    s.sendall(response)
    new_sock.close()


portnum = int(sys.argv[1])
srvr(portnum)
