import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))

while True:
    data,addr = sock.recvfrom(4096)
    print(str(data))
    msg = bytes('Hello i"m manoCode UDP server').encode('utf-8')
    sock.sendto(msg,addr)
