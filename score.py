class score:
	def __init__( self ):
		pass

	def HandScore( self, hand ):
		if len( hand ) != 4:
			raise Exception( "4 cards allowed in a hand!" )
		return sum( [x.GetValue() for x in hand] )

	def PileScore( self, pile ):
		if len( pile ) != 8:
			raise Exception( "Only 8 cards allowed in a pile!" )
		return sum( [x.GetValue() for x in pile] )
