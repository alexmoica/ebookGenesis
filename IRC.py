import socket
import sys
import time

class IRC:
	irc = socket.socket()

	#define socket
	def __init__(self):
		self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#send data
	def send(self, ch, msg):
		self.irc.send(bytes("PRIVMSG " + ch + " " + msg + "\n"))

	def connect(self, server, port, ch, botnick):
		#connect to server
		print("connecting to " + server + "..")
		self.irc.connect((server, port))

		#user authentication
		self.irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :python\n"))
		self.irc.send(bytes("NICK " + botnick + "\n"))
		time.sleep(5)
		
		# join channel
		print("connecting to " + ch + "..")
		self.irc.send(bytes("JOIN " + ch + "\n"))
	
	#get server response
	def get_response(self):
		time.sleep(1)

		#get output of server
		BUFFER_SIZE = 2040
		r = self.irc.recv(BUFFER_SIZE).strip("\n\r")
 
 		#respond to PING requests to keep bot alive
		if r.find('PING') != -1:
			self.irc.send("PONG :{}\n".format(" ".join('still alive')))
		
		return r