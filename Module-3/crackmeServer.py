#!/usr/bin/python

import SocketServer
import random

class EchoRequestHandler(SocketServer.BaseRequestHandler):
	def setup(self):
		#Server Message
		print 'Cient Details:'
		print 'IP: ' + self.client_address[0]
		print 'Remote Port: ' + str(self.client_address[1]) + '\n'

		#Client message
		self.request.send('\nHello ' + self.client_address[0] + '\n')
		self.request.send('Can you guess the password?!!' + '\n')
		self.request.send('(Type "bye" to disconnect...)' + '\n')

	def handle(self):
		while 1:
			data = self.request.recv(1024)
			rando = random.randrange(1,11)
			winner = str(int(self.client_address[1]) * rando)
			print 'Winner was: ' + winner

			if data.strip() == winner:
				self.request.send('Winner Winner Chicken dinner\n')
				return

			elif data.strip() == 'bye':
				return
			
			else:
				self.request.send('Muhaha, Try Harder!\n')

	def finish(self):
		print '\n' + str(self.client_address) + 'disconnected!'
		self.request.send('\nGoodbye ' + str(self.client_address[0]) + '\n')

SocketServer.TCPServer.allow_reuse_address = 1
server = SocketServer.ThreadingTCPServer(('0.0.0.0', 1337), EchoRequestHandler)
server.serve_forever()
