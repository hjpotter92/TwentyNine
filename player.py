class player:
	def __init__( self, alias, IP = '' ):
		self.__alias = alias
		self.__ip = IP

	def GetIP( self ):
		return self.__ip

	def GetNick( self ):
		return self.__alias
