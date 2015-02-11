import socket
from pygame.locals import *
from pygame import font, event as pyevent, display, draw
from player import player
from config import *

def GetKey():
	while True:
		event = pyevent.poll()
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
	def __init__( self, name, srvIP ):
		ip = socket.gethostbyname( socket.gethostname() )
		self.__gamer = player( name, ip )
		self.__server_ip = srvIP

if __name__ == "__main__":
	window = display.set_mode( (600, 400) )
	alias = AskQuestion( window, "Your nickname" )
	server_ip = AskQuestion( window, "Server IP" )
	c = client( alias.strip(), server_ip.strip() )
