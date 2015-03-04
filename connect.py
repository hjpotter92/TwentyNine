from json import dumps, loads
from struct import calcsize, pack, unpack

def send( channel, message ):
	try:
		msg = dumps( message )
		channel.send( pack("i", len(msg)) + msg )
		return True
	except OSError as e:
		print e
		return False

def receive( channel ):
	try:
		size = unpack( "i", channel.recv(calcsize("i")) )[0]
		data = ""
		while len(data) < size:
			msg = channel.recv( size - len(data) )
			if not msg:
				return None
			data += msg
		print data
		return loads( data.strip() )
	except OSError as e:
		print e
		return False
