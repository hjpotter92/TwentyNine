from json import dumps, loads

def send( channel, message ):
	try:
		channel.send( dumps(message) )
		return True
	except OSError as e:
		print e
		return False

def receive( channel, packet_size = 1024 ):
	try:
		data = channel.recv( int(packet_size) )
		if not data:
			return None
		return loads( data.strip() )
	except OSError as e:
		print e
		return False
