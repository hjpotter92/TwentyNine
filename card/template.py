from time import sleep
from pygame.locals import *
from pygame import init as pyinit, font, image, display, draw, transform, Surface

size = width, height = 70, 100
rows, cols = [ 12, 46 ], [ 11, 33, 55, 77 ]
positions = [ (a, b) for b in cols for a in rows ] + [ (29, 21), (29, 44), (29, 67) ]
cards = {
	'2': [0] * 8 + [ 1, 0, 1 ],
	'5': [ 1, 1 ] + [0] * 4 + [ 1, 1, 0, 1, 0 ],
	'7': [1] * 6 + [ 0, 0, 1, 0, 0 ],
	'8': [1] * 6 + [ 0, 0, 1, 1, 0 ],
	'9': [1] * 8 + [ 0, 1, 0 ],
	'10': [1] * 9 + [ 0, 1 ],
	'A': [0] * 9 + [ 1, 0 ]
}

class template:
	def __init__( self, suit, face ):
		pyinit()
		self.__font = font.Font( None, 20 )
		self.__card = Surface( size )
		self.__card.fill( (255, 255, 255) )
		self.__suit = image.load( 'card/images/' + suit + '.png' )
		self.__load_image = False
		self.__face = face
		self.__face_placements = cards[face]
		if not self.__face:
			self.__load_image = True
			self.__face = face
		self.__text_colour = (0, 0, 0) if suit in ['C', 'S'] else (255, 0, 0)

	def Generate( self ):
		draw.rect( self.__card, (0, 0, 0), (0, 0, 70, 100), 1 )
		if self.__load_image:
			print "Face not yet available"
			return
		self.__suit = transform.scale( self.__suit, (12, 12) )
		for x in xrange( len(self.__face_placements) ):
			if self.__face_placements[x] == 1:
				self.__card.blit( self.__suit, positions[x] )
		text = self.__font.render( self.__face, 1, self.__text_colour )
		text_size = self.__font.size( self.__face )
		self.__suit = transform.scale( self.__suit, (6, 6) )
		self.__card.blit( text, (2, 4) )
		self.__card.blit( self.__suit, (2, 15) )
		text = transform.rotate( text, 180 )
		self.__suit = transform.rotate( self.__suit, 180 )
		self.__card.blit( text, (68 - text_size[0], 84) )
		self.__card.blit( self.__suit, (64, 80) )

	def Place( self, screen, pos ):
		self.Generate()
		screen.blit( self.__card, pos )
		return

if __name__ == "__main__":
	pass
