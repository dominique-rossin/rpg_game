import pygame
from random import *


class Map:


	def __init__(self):
		self.longueur, self.largeur = pygame.display.Info().current_w, pygame.display.Info().current_h
		self.zoom = 1
		self.name = "test"
		self.load_map(self.name)
		self.x = 0
		self.y = 0
		

	def set_zoom(self,z):
		self.zoom = z
		if (z != int(z)):
			self.zoom = int(z)+1
		self.load_map(self.name)

	def load_map(self,name):
		self.mymap = [[randint(1,4) for i in range(200)] for j in range(200)]

		self.tiles = [None, pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile01.png'),(16*self.zoom,16*self.zoom)).convert(), pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile02.png'),(16*self.zoom,16*self.zoom)).convert(),
		pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile03.png'),(16*self.zoom,16*self.zoom)).convert(),pygame.transform.scale(pygame.image.load('rpg-pack/tiles/generic-rpg-tile04.png'),(16*self.zoom,16*self.zoom)).convert()]


	def draw(self, screen, x,y,longueur,largeur):
		#print("draw ",x,y,longueur,largeur,self.zoom) # premier appel 0 0 41 23 2
		for i in range(int(x),int(x)+longueur+1):
			for j in range(int(y), int(y)+largeur+1):

				#print("i = ",i," ,j = ",j," , ",int((i-x)*16*self.zoom),int((j-y)*16*self.zoom))
				if (i >=0 and j >=0 and i < len(self.mymap) and j < len(self.mymap[0])):
					screen.blit(self.tiles[self.mymap[i][j]],(int((i-x)*16*self.zoom),int((j-y)*16*self.zoom)))
