import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 9999))

data_recv=s.recvfrom(100)
print(data_recv)
rply="thanks for connecting"
s.sendto(rply.encode('ascii'), data_recv[1])
