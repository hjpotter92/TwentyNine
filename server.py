import socket
from select import select
from random import shuffle
from card import card
from score import score

suites, faces = [
	'S',			# Spades
	'H',			# Hearts
	'D',			# Diamonds
	'C'				# Clubs
], [
	# List with faces and corresponding score points
	['7', 0],
	['8', 0],
	['9', 2],
	['10', 1],
	['J', 3],
	['Q', 0],
	['K', 0],
	['A', 1]
]

class server:
	def __init__( self, ip = "", port = 0 ):
		self.SetAddress( ip, port )
		self.__SetSocket()
		self.__bid = 16				# Minimum bid is 16
		self.__trump_suite = None
		self.__deck = []
		for i in suites:
			for j in faces:
				x = card( j[0], i, j[1] )
				self.__deck.append( x )

	def __SetSocket( self, blocking = 0, queue = 4 ):
		self.__listener = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.__listener.bind( self.GetAddress() )
		self.__listener.setblocking( blocking )
		self.__listener.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
		self.__listener.listen( queue )

	def GetIP( self ):
		return self.__ip

	def GetPort( self ):
		return self.__port

	def GetAddress( self ):
		return self.__address

	def SetAddress( self, ip, port ):
		self.__address = self.__ip, self.__port = ip, port

	def CreatePile( self ):
		deck_copy = list( self.__deck )
		shuffle( deck_copy )
		return zip( *[iter(deck_copy)] * 4 )

	def forward( self, source, msg, readlist ):
		for s in readlist:
			if s != self.__listener and s != source:
				s.send( msg )

	def run( self ):
		self.__SetSocket( 0, 4 )
		read, write, error = [ self.__listener ], [], []
		listening = True
		while listening:
			r, w, x = select( read, write, error, 0 )
			for s in r:
				if s is self.__listener:
					c, a = s.accept()
					read.append( c )
					print a, "Connection established"
				else:
					try:
						data = s.recv( 32 )
						if data:
							print data.strip()
							if data.strip() == "quit":
								s.close()
								read.remove()
							self.forward( s, data, read )
					except socket.timeout, e:
						print e
						continue
					except:
						print a, c
						s.close()
						read.remove( s )
						continue
		self.__listener.close()

if __name__ == "__main__":
	pass
