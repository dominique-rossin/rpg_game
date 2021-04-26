import pygame

class Player(pygame.sprite.Sprite):


	def __init__(self,z):
		pygame.sprite.Sprite.__init__(self)
		self.left = False
		self.up = False
		self.loop = 0
		self.zoom = z
		self.player_animation = [pygame.image.load('rpg-pack/chars/gabe/gabe-run1.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run2.png')
		,pygame.image.load('rpg-pack/chars/gabe/gabe-run3.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run4.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run5.png'),pygame.image.load('rpg-pack/chars/gabe/gabe-run6.png'),
		pygame.image.load('rpg-pack/chars/gabe/gabe-run7.png')]

		for i in range(len(self.player_animation)):
			self.player_animation[i] = pygame.transform.scale(self.player_animation[i],(16*self.zoom,16*self.zoom)).convert_alpha()
		self.rect = self.player_animation[0].get_rect()
		self.health = 20
		self.hunger = 0
		self.x = 0
		self.y = 0
		self.animation_speed = 150
		self.elapsed_time = 0

		



	def set_pos(self,x,y):
		self.x = x
		self.y = y

	def draw(self):
		pass

	def move(self,dx,dy):

		if dx < 0:
			self.left = True
		else:
			self.left = False

		if dy < 0:
			self.up = False
		else:
			self.up = True

		self.x += dx
		self.y += dy


		#print("joueur :",self.x," , ",self.y )


	def draw(self, screen,x,y):
		self.rect.x = 16*self.zoom*(self.x-x)
		self.rect.y = 16*self.zoom*(self.y-y)
		self.player_sprite_to_blit = self.player_animation[self.loop]

		if self.left:
			screen.blit(pygame.transform.flip(self.player_sprite_to_blit,True,False),(16*self.zoom*(self.x-x),16*self.zoom*(self.y-y)))
		else:
			#screen.blit(self.player_sprite_to_blit,(16*self.zoom*(self.x-x),16*self.zoom*(self.y-y)))
			screen.blit(self.player_sprite_to_blit,self.rect)
		

	def animate(self,elapsed_time):
		if (elapsed_time - self.elapsed_time > self.animation_speed):
			self.loop +=1
			if self.loop >= len(self.player_animation):
				self.loop = 0
			self.elapsed_time = elapsed_time

		#screen.blit(self.player_animation[self.loop],(player_x,player_y))



