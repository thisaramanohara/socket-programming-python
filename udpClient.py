import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = 'Hello im a client'
client_socket.sendto(msg.encode('utf-8'),('127.0.0.1',12345))
data,addr = client_socket.recvfrom(4096)
print(data.decode())
client_socket.close()
