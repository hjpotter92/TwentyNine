from server import server
from score import score

if __name__ == "__main__":
	s, c = server( '10.109.1.92', 7777 ), score()
	d = s.CreatePile()
	s.run()
