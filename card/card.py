from template import template

class card:
	def __init__( self, face, suit, value ):
		self.__face = face
		self.__suit = suit
		self.__value = value
		self.__piece = template( suit, face )

	def __str__( self ):
		return "%s%-2s (%d)" % ( self.__suit, self.__face, self.__value )

	def GetValue( self ):
		return self.__value

	def GetFace( self ):
		return self.__face

	def GetSuit( self ):
		return self.__suit

if __name__ == "__main__":
	pass
