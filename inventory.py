import pygame

class Inventory:
	def __init__(self,zoom_ecran):
		self.zoom = zoom_ecran
		self.isvisible = False
		self.empty_inventory = pygame.transform.scale(pygame.image.load('rpg-pack/UI/generic-rpg-ui-inventario.png'),(450*self.zoom,350*self.zoom))
		self.item_inventory = dict()

	def appeal(self):
		if self.isvisible:
			self.isvisible = False
		else:
			self.isvisible = True

	def draw(self,screen):
		if self.isvisible:
			screen.blit(self.empty_inventory,(10*self.zoom,10*self.zoom))

	def change_inventory(self,object_to_add,quantity):

		if (object_to_add in self.item_inventory):
			self.item_inventory[object_to_add] += quantity
		else:
			self.item_inventory[object_to_add] = quantity
		print(self.item_inventory)

	def check_invetory(self,object_to_check,quantity):
		if (object_to_check in self.item_inventory):
			if self.item_inventory[object_to_check] >= quantity:
				return True
			else:
				return False
		else:
			return False

