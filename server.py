import socket
from select import select
from random import shuffle
from card.card import card, Generate
from score import score
from player import player
from connect import send, receive

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
		self.__players = {}
		self.__bid = 16				# Minimum bid is 16
		self.__trump_suite = None
		self.__pack = []
		for i in suites:
			for j in faces:
				x = card( j[0], i, j[1] )
				self.__pack.append( x )

	def __SetSocket( self, blocking = 0, queue = 4 ):
		self.__listener = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.__listener.bind( self.GetAddress() )
		self.__listener.setblocking( blocking )
		self.__listener.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
		self.__listener.listen( queue )
		self.__listener.settimeout( 5 )
		self.__read, self.__write, self.__error = [ self.__listener ], [], []

	def GetIP( self ):
		return self.__ip

	def GetPort( self ):
		return self.__port

	def GetAddress( self ):
		return self.__address

	def SetAddress( self, ip, port ):
		self.__address = self.__ip, self.__port = ip, port

	def CreatePile( self ):
		pack_copy = list( self.__pack )
		shuffle( pack_copy )
		return zip( *[iter(pack_copy)] * 8 )

	def __AddClient( self, source ):
		c, a = source.accept()
		c.settimeout( 5 )
		self.__read.append( c )
		send( c, ("text", "Welcome!") )
		return

	def __AddPlayer( self, source, nick ):
		num_players = len( self.__players ) or 0
		if num_players == 4:
			send( source, ('Error', "4 players already connected.") )
			self.__read.remove( source )
			source.close()
			return
		i = 0
		while self.__players.get( i ):
			i += 1
		gamer = player( nick, source.getpeername() )
		self.__players[i] = gamer
		send( source, ('ID', i) )

	def __RemovePlayer( self, source, gamer_id ):
		gamer = self.__players.pop( gamer_id )
		self.__read.remove( source )
		self.__Forward( source, ('Leave', gamer_id) )
		source.close()

	def __MaintainPlayers( self, source, data ):
		if data[0] == "Nick":
			self.__AddPlayer( source, data[1] )
			return True
		elif data[0] == "Quit":
			self.__RemovePlayer( source, data[1] )
			return True
		return False

	def __Forward( self, source, msg ):
		for s in self.__read:
			if s != self.__listener and s != source:
				send( s, msg )

	def __Connect( self ):
		joining = True
		while joining:
			r, w, x = select( self.__read, self.__write, self.__error, 0 )
			for s in r:
				if s is self.__listener:
					self.__AddClient( s )
				else:
					data = receive( s )
					if data:
						print data, s.getpeername()
						if self.__MaintainPlayers( s, data ):
							pass
			if len( self.__players ) == 4:
				joining = False
		players = []
		for player_id in self.__players:
			player = self.__players[player_id]
			players.append( (player_id, player.GetNick()) )
		print players
		self.__Forward( self.__listener, players )
		return

	def __Bidding( self ):
		piles, bids, bidding = self.CreatePile(), [], True
		for i in range( 1, 5 ):
			s, p = self.__read[i], piles.pop()
			x = [ y.Compile() for y in p ]
			print s.getpeername(), x
			send( s, ('Cards', x) )
		while bidding:
			r, w, x = select( self.__read, self.__write, self.__error, 0 )
			for s in r:
				if s is self.__listener:
					self.__AddClient( s )
				else:
					data = receive( s )
					if data:
						print data, s.getpeername()
						if self.__MaintainPlayers( s, data ):
							pass
			if len( bids ) == 4:
				bidding = False

	def run( self ):
		self.__SetSocket( 1, 4 )
		print "Waiting for players."
		self.__Connect()
		print "Players have joined. Bidding started."
		self.__Bidding()
		print "Round starts with max. bet: ", self.__bid
		listening = True
		while listening:
			r, w, x = select( self.__read, self.__write, self.__error, 0 )
			for s in r:
				if s is self.__listener:
					self.__AddClient( s )
				else:
					try:
						data = receive( s )
						if data:
							print data
							self.__Forward( s, data )
					except socket.timeout, e:
						print e
						continue
					except KeyboardInterrupt, e:
						print e
						break
		self.__listener.close()

if __name__ == "__main__":
	pass
