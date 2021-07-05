import pygame

class Inventory:
	def __init__(self,zoom_ecran):
		self.zoom = zoom_ecran
		self.isvisible = False
		object_size = 45
		self.empty_inventory = pygame.transform.scale(pygame.image.load('rpg-pack/UI/generic-rpg-ui-inventario.png'),(450*self.zoom,350*self.zoom)).convert_alpha()
		self.item_inventory = dict()
		self.right_arrow = pygame.transform.scale(pygame.image.load('rpg-pack/props n decorations/arrow_inventory.png'),(object_size*self.zoom,object_size*self.zoom)).convert_alpha()
		self.left_arrow = pygame.transform.flip(self.right_arrow,True,False)
		self.case_coordonnes = [(110,385), (260,385),(420,385),(110,530), (260,530),(420,530)]
		self.item_images = {"sword":pygame.transform.scale(pygame.image.load('rpg-pack/props n decorations/generic-rpg-loot01.png'),(object_size*self.zoom,object_size*self.zoom)).convert_alpha(),
		"shield":pygame.transform.scale(pygame.image.load('rpg-pack/props n decorations/generic-rpg-loot02.png'),(object_size*self.zoom,object_size*self.zoom)).convert_alpha(),
		"heal_potion":pygame.transform.scale(pygame.image.load('rpg-pack/props n decorations/generic-rpg-loot03.png'),(object_size*self.zoom,object_size*self.zoom)).convert_alpha(),
		"mana_potion":pygame.transform.scale(pygame.image.load('rpg-pack/props n decorations/generic-rpg-loot04.png'),(object_size*self.zoom,object_size*self.zoom)).convert_alpha()}
		self.inventory_start = 0

	def check_open(self):
		if self.isvisible:
			return True
		else:
			return False

	def appeal(self):
		if self.isvisible:
			self.isvisible = False
		else:
			self.isvisible = True
	def draw(self,screen):
		i = 0
		if self.isvisible:
			screen.blit(self.empty_inventory,(10*self.zoom,10*self.zoom))
			for item in self.item_inventory.keys():
				if item in self.item_images:
					screen.blit(self.item_images[item],self.case_coordonnes[i + self.inventory_start])
					i += 1
			#self.items = list(self.item_inventory.keys())
			screen.blit(self.right_arrow,(750,600))
			screen.blit(self.left_arrow,(50,600))


	def change_inventory(self,object_to_add,quantity):

		if (object_to_add in self.item_inventory):
			self.item_inventory[object_to_add] += quantity
		else:
			self.item_inventory[object_to_add] = quantity
		#print(self.item_inventory)

	def check_invetory(self,object_to_check,quantity):
		if (object_to_check in self.item_inventory):
			if self.item_inventory[object_to_check] >= quantity:
				return True
			else:
				return False
		else:
			return False

	def check_arrow(self,modifieur):
		if self.inventory_start + modifieur >= 0:
			self.inventory_start += modifieur
			


