import socket
from select import select
from player import player

class client:
	def __init__( self ):
		name = raw_input( "Enter a nickname: " )
		ip = socket.gethostbyname( socket.gethostname() )
		self.__gamer = player( name, ip )

	def run( self ):
		playing = True
		while playing:
			choice = raw_input( "Press [y/Y] to keep playing, any other key to quit: " )
			playing = True if choice in "yY" else False
		return

if __name__ == "__main__":
	c = client()
	c.run()
	pass
