import socket
udp_ip_address="127.0.0.1"
udp_port_no=5555
Message=("hello")
bytestosend=str.encode(Message)
clientsock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsock.sendto(bytestosend,(udp_ip_address,udp_port_no))
servermessage=clientsock.recvfrom(1024)
print(servermessage)
	 
