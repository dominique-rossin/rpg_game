import pygame
import random

class Enemy(pygame.sprite.Sprite):

	@staticmethod
	def get_sprite(type_enemy):
		# dans dictionnaire : icone,nb_images_anim, taille_sprite,PV
		sprites = {'slime-blue': ('slime-blue.png',4,16,10),'slime-green': ('slime-green.png',4,16,10),
		'slime-orange': ('slime-orange.png',4,16,10),'worm-run-idle':('worm-run-idle.png',31,16,20)}
		if  (type_enemy in sprites):
			return sprites[type_enemy]
		else:
			print("Erreur sprite")


	def __init__(self,zoom_ecran,type_enemy,tile_size,groupe):
		pygame.sprite.Sprite.__init__(self,groupe)

		self.zoom = zoom_ecran
		self.tile_size = tile_size
		self.enemy = Enemy.get_sprite(type_enemy)
		self.nb_images_anim = self.enemy[1]
		self.spriteSheet = pygame.transform.scale(pygame.image.load('rpg-pack/mobs/'+self.enemy[0]),(16*self.zoom*self.nb_images_anim,16*self.zoom)).convert_alpha()
		self.sprite_size = self.enemy[2]*zoom_ecran
		self.sprite = self.spriteSheet.subsurface(pygame.Rect(0,0,self.sprite_size,self.sprite_size))
		self.rect = self.sprite.get_rect()
		self.PV = self.enemy[3]
		self.x = random.randrange(0,30)
		self.y  = random.randrange(0,20)
		#print(self.x,"   ",self.y)
		self.loop = 0
		self.visible = True
		self.animation_speed = 100
		self.elapsed_time = 0


	def animate(self,elapsed_time):
		if (elapsed_time - self.elapsed_time > self.animation_speed):
			self.loop +=1
			if self.loop >= self.nb_images_anim:
				self.loop = 0
			self.elapsed_time = elapsed_time
			self.sprite = self.spriteSheet.subsurface(pygame.Rect(self.loop*self.sprite_size,0,self.sprite_size,self.sprite_size))

	def draw(self, screen,x,y):
		self.rect.x = self.tile_size*self.zoom*(self.x-x)
		self.rect.y = self.tile_size*self.zoom*(self.y-y)
#		screen.blit(self.sprite,(self.tile_size*self.zoom*(self.x-x),self.tile_size*self.zoom*(self.y-y)))
		screen.blit(self.sprite,self.rect)
