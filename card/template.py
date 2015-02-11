from pygame.locals import *
from pygame import image, display, draw, transform

size = width, height = 70, 100
rows, cols = [ 12, 46 ], [ 11, 33, 55, 77 ]
positions = [ (a, b) for b in cols for a in rows ] + [ (29, 21), (29, 44), (29, 67) ]
cards = {
	'7': [1] * 6 + [ 0, 0, 1, 0, 0 ],
	'8': [1] * 6 + [ 0, 0, 1, 1, 0 ],
	'9': [1] * 8 + [ 0, 1, 0 ],
	'10': [1] * 9 + [ 0, 1 ],
	'A': [0] * 9 + [ 1, 0 ]
}

class template:
	def __init__( self, suit, face ):
		self.__card = display.set_mode( size )
		self.__card.fill( (255, 255, 255) )
		self.__suit = image.load( 'card/images/' + suit + '.png' )
		self.__load_image = False
		self.__face = cards[face]
		if not self.__face:
			self.__load_image = True
			self.__face = face

	def Place( self, screen, pos ):
		if self.__load_image:
			print "Face not yet available"
			return
		self.__suit = transform.scale( self.__suit, (12, 12) )
		for x in xrange( len(self.__face) ):
			if self.__face[x] == 1:
				self.__card.blit( self.__suit, positions[x] )
		screen.blit( self.__card, pos )
		return

if __name__ == "__main__":
	pass
