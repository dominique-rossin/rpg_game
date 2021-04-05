import pygame

class Player:


	def __init__(self):
		self.loop = 0
		self.player_animation = [pygame.image.load('rpg-pack/chars/gabe/gabe-run1.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run2.png')
		,pygame.image.load('rpg-pack/chars/gabe/gabe-run3.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run4.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run5.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run6.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run7.png')]
		self.health = 20
		self.hunger = 0
		self.x = 0
		self.y = 0



	def draw(self):
		pass

	

	def idle(self, screen,player_x,player_y):
		screen.blit(self.player_animation[self.loop],(player_x,player_y))

	def animate(self, screen,player_x,player_y):
		self.loop +=1
		if self.loop >= len(self.player_animation):
			self.loop = 0

		screen.blit(self.player_animation[self.loop],(player_x,player_y))



