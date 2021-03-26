import os
import socket
import struct

#convert 32-bit address to IP address
def int2ip(addr):
	return socket.inet_ntoa(struct.pack("!I", addr))

def downloadfile(dataString):
	filename = dataString[0].replace(' ', '_')
	remote_address = dataString[1]
	remote_port = dataString[2]
	filesize = dataString[3]

	dcc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dcc.settimeout(120)

	intip = int(remote_address)
	server = int2ip(intip) #we need IP address not 32-bit

	dcc.connect((server, int(remote_port)))
	bytes_received = 0
	total_bytes = int(filesize)

	with open(filename, 'w') as out:
		print 'Downloading %s..' % os.path.basename(filename)
		data = dcc.recv(4096)
		while True:
			bytes_received += len(data)
			out.write(data)
			if bytes_received == total_bytes:
				dcc.close()
				print 'Done file download'
				break