from random import shuffle
from card import card
from score import score

suits = [
	'S',			# Spades
	'H',			# Hearts
	'D',			# Diamonds
	'C'				# Clubs
]
faces = [			# List with faces and corresponding score points
	['7', 0],
	['8', 0],
	['9', 2],
	['10', 1],
	['J', 3],
	['Q', 0],
	['K', 0],
	['A', 1]
]

class server:
	def __init__( self ):
		self.__deck = []
		for i in suits:
			for j in faces:
				x = card(j[0], i, j[1])
				self.__deck.append( x )

	def CreatePile( self ):
		deck_copy = list( self.__deck )
		shuffle( deck_copy )
		return zip( *[iter(deck_copy)] * 4 )

if __name__ == "__main__":
	pass
