from card import card

class server:
	def __init__( self ):
		suits = [
			'S',			# Spades
			'H',			# Hearts
			'D',			# Diamonds
			'C'				# Clubs
		]
		faces = [
			['7', 0],
			['8', 0],
			['9', 2],
			['10', 1],
			['J', 3],
			['Q', 0],
			['K', 0],
			['A', 1]
		]
		self.deck = []
		for i in suits:
			for j in faces:
				x = card(j[0], i, j[1])
				print x
				self.deck.append( x )

if __name__ == "__main__":
	s = server()
