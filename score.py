class score:
	def __init__( self ):
		pass

	def PileScore( self, pile ):
		if len(pile) != 4:
			raise Exception( "More than 4 cards in pile!" )
		return sum( [x.GetValue() for x in pile] )
