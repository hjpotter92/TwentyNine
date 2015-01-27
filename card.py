class card:
	def __init__( self, face, suit, value ):
		self.face = face
		self.suit = suit
		self.value = value

	def __str__( self ):
		return "%s%-2s (%d)" % ( self.suit, self.face, self.value )

if __name__ == "__main__":
	pass
