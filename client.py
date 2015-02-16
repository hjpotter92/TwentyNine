import socket
from select import select
from pygame.locals import *
from pygame import font, event as pyevent, display, draw, Surface
from player import player
from config import *
from connect import send, receive

def GetKey():
	while True:
		event = pyevent.poll()
		if event.type == QUIT:
			return K_ESCAPE
		if event.type == KEYDOWN:
			if event.key in range( 256, 266 ):
				# For keys pressed in numberpad
				return event.key - 208
			return event.key

def BoxDisplay( scr, msg ):
	text, w, h = font.Font( None, 24 ), scr.get_width(), scr.get_height()
	pos_x, pos_y = w / 2 - 200, h / 2 - 30
	draw.rect( scr, COLOURS.get('GREY'), (pos_x, pos_y, 400, 60), 0 )
	draw.rect( scr, COLOURS.get('WHITE'), (pos_x - 2, pos_y - 2, 404, 64), 1 )
	if len( msg ) > 0:
		scr.blit( text.render(msg, 1, COLOURS.get('WHITE')), (pos_x + 20, pos_y + 18) )
	display.flip()

def AskQuestion( screen, question ):
	font.init()
	response = []
	display.set_caption( question )
	while True:
		BoxDisplay( screen, question + ": " + ''.join(response) )
		inp = GetKey()
		if inp == K_BACKSPACE:
			response = response[:-1]
		elif inp == K_ESCAPE:
			return ''
		elif inp == K_RETURN or inp == K_KP_ENTER:
			break
		elif inp == K_KP_PERIOD:
			response.append( '.' )
		elif inp <= 127:
			response.append( chr(inp) )
	return ''.join( response )

class client:
	def __init__( self, name, srvIP, srvPort ):
		ip = socket.gethostbyname( socket.gethostname() )
		self.__gamer = player( name, ip )
		self.__server_address = self.__server_ip, self.__server_port = srvIP, srvPort
		self.__ID = None
		self.__SetListener()

	def __SetListener( self ):
		self.__listener = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		self.__listener.settimeout( 5 )
		try:
			self.__listener.connect( self.__server_address )
		except Exception, e:
			print "Unable to connect", e
			raise e
		print "Connected to %s:%d." % self.__server_address
		send( self.__listener, ("Nick", self.__gamer.GetNick()) )

	def __Quit( self, readlist ):
		send( self.__listener, ("Quit", self.__ID) )
		readlist.remove( self.__listener )
		self.__listener.close()

	def run( self ):
		self.__window = display.set_mode( SIZE )
		display.set_caption( "Twenty Nine" )
		self.__window.fill( COLOURS.get('BOARD') )
		display.flip()
		self.__read, self.__write, self.__error = [ self.__listener ], [], []
		while True:
			r, w, x = select( self.__read, self.__write, self.__error, 0 )
			for f in r:
				if f is self.__listener:
					data = receive( f )
					if data:
						if data[0] == "ID":
							self.__ID = int( data[1] )
						print data
			event = pyevent.poll()
			if event.type == QUIT:
				self.__Quit( read )
				break
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.__Quit( read )
					break
				else:
					send( self.__listener, chr(event.key) )
			elif event.type == MOUSEBUTTONDOWN:
				print event

if __name__ == "__main__":
	pass
