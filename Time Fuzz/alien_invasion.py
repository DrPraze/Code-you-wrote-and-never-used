import pygame

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((900, 650))
		pygame.display.set_caption("Star Fuzz")

	def ship(self):
		ship1 = pygame.image.load('alien_spaceship_invasion_1.png')
		

	def loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
			pygame.display.update()

if __name__=='__main__':
	Game().loop()