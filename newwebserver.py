import socket
import sys
# import string
import os


s = socket.socket()


def nwebserver(portnum):

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', portnum))
    s.listen()
    while 1:
        new_conn = s.accept()
        new_sock = new_conn[0]
        request = b""
        while 1:
            request = new_sock.recv(4096)
            if ((request.decode("ISO-8859-1")).find("\r\n\r\n") != -1):
                break
        # parse request header to get the file path
        lines = (request.decode("ISO-8859-1")).split("\r\n")
        getline = lines[0]
        path = getline.split()[1]
        # to get the file name to serve
        file = os.path.split(path)[-1]
        # determine the mime type
        extn = os.path.splitext(file)[-1]  # gives the extention of the file
        content_type = ""  # gives the mime type of file
        if (extn == ".html"):
            content_type = "text/html"
        if (extn == ".txt"):
            content_type = "/text/plain"
        if (extn == ".gif"):
            content_type = "/image/gif"
        # reading the file and getting content size and handling not found 404 error
        data = b""
        content_size = ""
        # new_sock.sendall(file.encode())
        try:
            with open(file, "rb") as fp:
                data = fp.read()
                # new_sock.sendall(data)
                content_size = str(os.path.getsize(file))
        except:
            new_sock.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")
            new_sock.close()
            break
        # putting together the http response!!
        response = b"HTTP/1.1 200 OK\r\nContent-Type: " + \
            content_type.encode() + b"\r\nContent-Length: " + \
            content_size.encode() + b"\r\n\r\n" + data
        new_sock.sendall(response)
        new_sock.close()


portnum = int(sys.argv[1])
nwebserver(portnum)
