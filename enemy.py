class Enemy:

	@staticmethod
	def get_sprite(type_enemy):
		# dans dictionnaire : icone,nb_images_anim, taille_sprite,PV
		sprites = {'slime-blue': ('slime-blue.png',4,16,10)}
		if  (type_enemy in sprites):
			return sprites[type_enemy]
		else:
			print("Erreur sprite")


	def __init__(self,zoom_ecran,type_enemy):
		self.zoom = zoom_ecran
		self.enemy = Enemy.get_sprite(type_enemy)
		self.nb_images_anim = self.enemy[1]
		self.icon = pygame.transform.scale(pygame.image.load('rpg-pack/mobs/'+self.enemy[0]),(16*self.zoom*self.nb_images_anim,16*self.zoom)).convert_alpha()
		self.sprite_size = self.enemy[2]
		self.PV = self.enemy[3]
		self.x = 10.2
		self.y  = 12.1
		self.visible = True
		self.loop_animate = 0

	def draw(self,screen):
		if (self.visible):
			
			self.loop_animate += 1
