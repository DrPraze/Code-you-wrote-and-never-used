import pygame, webbrowser

class Main:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((900, 650))
		pygame.display.set_caption("Star Fuzz")
		self.font = pygame.font.SysFont('comicsansms', 52)
		self.title = pygame.font.SysFont('magneto', 100)
		self.font1 = pygame.font.SysFont('informalroman', 60)
		self.font2 = pygame.font.SysFont('comicsansms', 32)
		# print(pygame.font.get_fonts())
		self.screen.fill((0, 0, 255))
		self.scene = 'MAINMENU'
		self.draw()
		self.n = 0
		self.ships = ['ship1.png', 'Spaceship_tut.png']

	def Text(self, text, color, x, y):self.screen.blit(self.font.render(text, 1, color), (x, y))
	def Title(self, text, color, x, y):self.screen.blit(self.title.render(text, 1, color), (x, y))
	def Text1(self, text, color, x, y):self.screen.blit(self.font1.render(text, 1, color), (x, y))
	def Text2(self, text, color, x, y):self.screen.blit(self.font2.render(text, 1, color), (x, y))

	def draw(self):
		bg = pygame.image.load('imgs/menu.jpg')
		self.screen.blit(bg, (0, 0))
		pygame.mixer.music.load('sound/bensound-scifi.mp3')
		pygame.mixer.music.play()
		
		menu = pygame.Surface((300, 300))
		menu.fill((0,0,0))
		menu.set_alpha(50)
		self.screen.blit(menu, (10, 140))
		self.Title("Star Fuzz", (255, 255, 255), 330, 10)
		self.Text("Play", (255, 255, 255), 20, 150)
		self.Text("About", (255, 255, 255), 20, 250)
		self.Text("Quit", (255, 255, 255), 20, 350)

	def match_coord(self, x, y, w, h):
		if self.pos[0]>x and self.pos[0]<x+w:
			if self.pos[1]>y and self.pos[1]<y+h:
				return True

	def menu(self):
		self.scene = "SELECTMENU"
		self.screen.fill((0, 0, 0))
		pygame.mixer.music.load('sound/bensound-epic.mp3')
		pygame.mixer.music.play()
		bg = pygame.image.load('imgs/select.jpg')
		self.screen.blit(bg, (0, 0))
		self.Title("Selections", (255, 255, 255), 300, 10)
		pygame.draw.rect(self.screen, (62, 62, 255), (30, 150, 300, 10))
		pygame.draw.rect(self.screen, (30, 30, 255), (30, 160, 300, 25))
		pygame.draw.rect(self.screen, (0, 0, 255), (30, 175, 300, 30))
		self.Text("<", (255, 255, 255), 33, 140)
		self.Text(">", (255, 255, 255), 305, 140)

		view = pygame.Surface((250, 200))
		view.fill((0, 0, 255))
		view.set_alpha(128)
		self.screen.blit(view, (53, 230))
		pygame.draw.rect(self.screen, (0, 0, 255), (51, 228, 250, 200), 3)

		pygame.draw.rect(self.screen, (62, 62, 255), (430, 150, 300, 10))
		pygame.draw.rect(self.screen, (30, 30, 255), (430, 160, 300, 25))
		pygame.draw.rect(self.screen, (0, 0, 255), (430, 175, 300, 30))
		view = pygame.Surface((250, 200))
		view.fill((0, 0, 255))
		view.set_alpha(128)
		self.screen.blit(view, (453, 230))
		pygame.draw.rect(self.screen, (0, 0, 255), (452, 228, 250, 200), 3)
		self.Text("<", (255, 255, 255), 433, 140)
		self.Text(">", (255, 255, 255), 707, 140)

	def about(self):
		self.scene = 'ABOUTSCENE'
		self.screen.blit(pygame.image.load('imgs\\about.jpg'), [0, 0])
		self.Text1('ABOUTS AND CREDITS', (255, 255, 255), 30, 30) 
		self.Text2("This program was created by Praise James.", (255, 255, 255), 30, 150)
		self.Text2("The developer didn't do all this alone, so he", (255, 255, 255), 30, 200)
		self.Text2("would like to give credit to where is due", (255, 255, 255), 30, 250)
		self.Text1("GRAPHICS:", (255, 255, 255), 30, 300);self.Text2("opengameart.org", (255,255,255), 300, 320)
		self.Text1("SOUND:", (255, 255, 255), 30, 400);self.Text2("bensound.com", (255, 255, 255), 260, 420)

		y = 330
		for i in range(2):
			pygame.draw.rect(self.screen, (255,255,255), (580, y, 80, 40),2)
			self.Text2("Visit", (255, 255, 255), 590, y)
			y+=100
		pygame.draw.rect(self.screen, (255, 255, 255), (100, 600, 110, 40), 2)
		self.Text2('<<Back', (255,255,255), 110, 600)
	
	def loop(self):
		while True:
			self.pos = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				if event.type == pygame.MOUSEMOTION:
					if self.scene == 'MAINMENU':
						if self.match_coord(10, 140, 300, 100):
							pygame.draw.rect(self.screen, (255, 255, 255), (310, 140, 3, 100))
						else:
							pygame.draw.rect(self.screen, (0, 0, 255), (310, 140, 3, 100))
						if self.match_coord(10, 240, 300, 100):
							pygame.draw.rect(self.screen, (255, 255, 255), (310, 240, 3, 100))
						else:
							pygame.draw.rect(self.screen, (0, 0, 255), (310, 240, 3, 100))
						if self.match_coord(10, 340, 300, 100):
							pygame.draw.rect(self.screen, (255, 255, 255), (310, 340, 3, 100))
						else:
							pygame.draw.rect(self.screen, (0, 0, 255), (310, 340, 3, 100))
					elif self.scene == 'SELECTMENU':
						if self.match_coord(33, 140, 50, 160):
							self.Text("<", (0, 255, 0), 33, 140)
						else:
							self.Text("<", (255, 255, 255), 33, 140)
						if self.match_coord(287, 140, 50, 160):
							self.Text(">", (0, 255, 0), 305, 140)
						else:
							self.Text(">", (255, 255, 255), 305, 140)
					elif self.scene == 'ABOUTSCENE':
						if self.match_coord(580, 330, 80, 40):
							pygame.draw.rect(self.screen, (0,255,0), (580, 330, 80, 40),2)
							self.Text2("Visit", (0, 255, 0), 590, 330)
						else:
							pygame.draw.rect(self.screen, (255,255,255), (580, 330, 80, 40),2)
							self.Text2("Visit", (255, 255, 255), 590, 330)
						if self.match_coord(580, 430, 80, 40):
							pygame.draw.rect(self.screen, (0,255,0), (580, 430, 80, 40),2)
							self.Text2("Visit", (0, 255, 0), 590, 430)
						else:
							pygame.draw.rect(self.screen, (255,255,255), (580, 430, 80, 40),2)
							self.Text2("Visit", (255, 255, 255), 590, 430)
						if self.match_coord(100, 600, 110, 40):
							pygame.draw.rect(self.screen, (0, 255, 0), (100, 600, 110, 40), 2)
							self.Text2('<<Back', (0,255,0), 110, 600)
						else:
							pygame.draw.rect(self.screen, (255, 255, 255), (100, 600, 110, 40), 2)
							self.Text2('<<Back', (255,255,255), 110, 600)

				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.scene == 'MAINMENU':
						if self.match_coord(10, 140, 300, 100):
							self.menu()
						if self.match_coord(10, 240, 300, 100):
							self.about()
						if self.match_coord(10, 340, 300, 100):
							quit()
					elif self.scene == 'ABOUTSCENE':
						if self.match_coord(580, 330, 80, 40):
							webbrowser.open('opengameart.org')
						elif self.match_coord(580, 430, 80, 40):
							webbrowser.open('bensound.com')
						elif self.match_coord(100, 600, 110, 40):
							self.scene = 'MAINMENU'
							self.draw()
						elif self.scene == 'SELECTMENU':
							if self.match_coord(33, 140, 50, 160):
								# self.Text("<", (0, 255, 0), 33, 140)
								if self.n>=0:
									self.n -= 1
								self.screen.blit(pygame.image.load(self.ships(self.n)), (33, 140))
							else:
								self.Text("<", (255, 255, 255), 33, 140)
							if self.match_coord(287, 140, 50, 160):
								self.Text(">", (0, 255, 0), 305, 140)
							else:
								self.Text(">", (255, 255, 255), 305, 140)
			pygame.display.update()

if __name__ == '__main__':
	Main().loop()