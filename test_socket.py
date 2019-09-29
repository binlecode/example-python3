# Open a file, read each line, and print it out

import socket

print(socket.gethostbyname("www.google.com"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen(5)
