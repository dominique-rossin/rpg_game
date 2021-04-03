import pygame

class player:
	def __init__(self):
		self.health = 20
		self.hunger = 0
		self.x = 0
		self.y = 0

	def draw(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					haut = True

				if event.key == pygame.K_DOWN:
					bas = True

				if event.key == pygame.K_LEFT:
					gauche = True

				if event.key == pygame.K_RIGHT:
					droite = True

			if event.type == pygame.KEYUP:

				if event.key == pygame.K_UP:
					haut = False

				if event.key == pygame.K_DOWN:
					bas = False

				if event.key == pygame.K_LEFT:
					gauche = False

				if event.key == pygame.K_RIGHT:
					droite = False
						
			if event.type == pygame.QUIT:
				pygame.quit()
				Fin = True


			if haut:
				self.y -= 0.5

			if bas:
				self.y += 0.5

			if gauche:
				self.x -= 0.5

			if droite:
				self.x += 0.5

