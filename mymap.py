import pygame

class Map:


	def __init__(self):
		self.longueur, self.largeur = pygame.display.Info().current_w, pygame.display.Info().current_h
		self.longueur_virtuelle = 400
		self.largeur_virtuelle = 225

		self.coefficient_longueur = round(self.longueur/self.longueur_virtuelle)
		self.coefficient_largeur = round(self.largeur/self.largeur_virtuelle)

		self.name = "test"
		self.load_map(self.name)
		self.x = 0
		self.y = 0
		a = 2

		

	def load_map(self,name):
		self.mymap = [
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3],
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3],
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3],
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3],
		[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4],
		[2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1],
		[3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2],
		[4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3],
		]

		self.size = round(self.largeur_virtuelle / len(self.mymap[0]))
		self.tiles = [None, pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile01.png'),(self.size*self.coefficient_largeur,self.size*self.coefficient_largeur)), pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile02.png'),(self.size*self.coefficient_largeur,self.size*self.coefficient_largeur)),
		pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile03.png'),(self.size*self.coefficient_largeur, self.size*self.coefficient_largeur)),pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile04.png'),(self.size*self.coefficient_largeur,self.size*self.coefficient_largeur))]


	def scroll_x(self,dir):
		self.x = dir

	def scroll_y(self,dir):
		self.y = dir

	def draw(self, screen, center_x,center_y):
		for i in range(center_x-10,center_x+10):
			for j in range(center_y-10, center_y+10):
				screen.blit(self.tiles[self.mymap[i][j]],(250-(center_x-i)*16+ self.x,250-(center_y-j)*16+self.y))
