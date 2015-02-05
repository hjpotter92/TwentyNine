import socket
from select import select
from player import player

class client:
	def __init__( self ):
		name = raw_input( "Enter a nickname: " )
		ip = socket.gethostbyname( socket.gethostname() )
		self.__gamer = player( name, ip )

	def run( self ):
		self.__connection = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.__connection.settimeout( 2 )
		self.__connection.connect( ('10.109.1.92', 7777) )
		read, write, error = [ self.__connection ], [], []
		playing = True
		i = 0
		while playing:
			r, w, x = select( read, write, error, 0 )
			for s in r:
				print s
				if s is self.__connection:
					data = s.recv( 32 )
					if data:
						print data
					else:
						print "Nothing received"
				else:
					choice = raw_input( "Press [y/Y] to keep listening: " )
					playing = True if choice in "yY" else False
					s.send( "some data " + i )
					i = i + 1
		return

if __name__ == "__main__":
	c = client()
	c.run()
	pass
