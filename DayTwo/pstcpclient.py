import socket

try:
    server_addr = 'localhost', 9999
    sock = socket.socket()
    sock.connect(server_addr)
    payload = sock.recv(1024)
    print(payload)
    print(payload.decode('ascii'))
finally:
    sock.close()