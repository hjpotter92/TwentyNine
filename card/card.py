from template import template

def Generate( s ):
	return card( *s.split() )

class card:
	def __init__( self, face, suit, value = 0 ):
		self.__face = face
		self.__suit = suit
		self.__value = int( value )

	def __str__( self ):
		return "%s%-2s (%d)" % ( self.GetSuit(), self.GetFace(), self.GetValue() )

	def GetValue( self ):
		return self.__value

	def GetFace( self ):
		return self.__face

	def GetSuit( self ):
		return self.__suit

	def CreateFromTemplate( self ):
		self.__piece = template( suit, face )

	def Compile( self ):
		return "%s %s %d" % ( self.GetFace(), self.GetSuit(), self.GetValue() )

if __name__ == "__main__":
	pass
