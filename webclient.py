import socket
import sys

s = socket.socket()
s.settimeout(5)


def clt(host, port):
    s.connect((host, port))
    request = b"GET /home/mihir/netbasics/nyan-cat.gif HTTP/1.1\r\nHost: " + \
        host.encode() + b"\r\n\r\n"
    s.sendall(request)
    response = b""
    while 1:
        try:
            d = s.recv(4096)
            if not d:
                break
            response += d
        except socket.timeout:
            break
    s.close()
    return response.decode('utf-8')


host = sys.argv[1]
port = int(sys.argv[2])
response = clt(host, port)
print(response)
