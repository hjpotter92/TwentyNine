from server import server
from score import score

if __name__ == "__main__":
	s, c = server(), score()
	d = s.CreatePile()
	for x in d:
		print [ str(t) for t in x ]
		print c.PileScore( x )
