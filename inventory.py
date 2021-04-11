import pygame

class Inventory:
	def __init__(self,zoom_ecran):
		self.zoom = zoom_ecran
		self.isvisible = False
		self.empty_inventory = pygame.transform.scale(pygame.image.load('rpg-pack/UI/generic-rpg-ui-inventario.png'),(450*self.zoom,350*self.zoom))

	def appeal(self):
		if self.isvisible:
			self.isvisible = False
		else:
			self.isvisible = True

	def draw(self,screen):
		if self.isvisible:
			screen.blit(self.empty_inventory,(10*self.zoom,10*self.zoom))


