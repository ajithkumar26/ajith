import socket
udp_ip_address="127.0.0.1"
udp_port_no=5555
serversock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversock.bind((udp_ip_address,udp_port_no)) 
print("system waiting")                                         
while True:
	 data,addr=serversock.recvfrom(1024)
	 print("Message:",data)
	 serversock.sendto(data,addr)
	
