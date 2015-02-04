import socket
from player import player

class client:
	def __init__( self ):
		name = raw_input( "Enter a nickname: " )
		ip = socket.gethostbyname( socket.gethostname() )
		self.__gamer = player( name, ip )
