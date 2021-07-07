import socket
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
recv_addr=(("3.17.143.64",9999))
while 2 > 1 :
    user_data=input("enter your message:-")
    newdata=user_data.encode('ascii')
    time.sleep(2)
    s.sendto(newdata, recv_addr)
    print("your message has been sent")
