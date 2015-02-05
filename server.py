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
		self.__bid = 16				# Minimum bid is 16
		self.__trump_suite = None
		self.__deck = []
		for i in suites:
			for j in faces:
				x = card( j[0], i, j[1] )
				self.__deck.append( x )

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

	def run( self ):
		self.__listener = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.__listener.bind( self.GetAddress() )
		listening = True
		try:
			while listening:
				r, w, x = select( [ self.__listener ], [], [], 0 )
				for x in r:
					print x
					print x, x.recvfrom( 1024 )
		except Exception, e:
			listening = False
			raise e
		self.__listener.close()

if __name__ == "__main__":
	pass
