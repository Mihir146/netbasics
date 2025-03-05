import socket
import sys


s = socket.socket()


def nwebserver(portnum):

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind('', portnum)
    s.listen()
    new_conn = s.accept()
    new_sock = new_conn[0]
    request = b""
    while 1:
        request = new_sock.recv(4096)


portnum = sys.argv[1]
nwebserver(portnum)
