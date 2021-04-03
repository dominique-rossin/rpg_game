import pygame
from mymap import *

pygame.init()
screen = pygame.display.set_mode([500, 500])

m = Map()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255,255,255))
	m.draw(screen,5,5)
	pygame.display.flip()
pygame.quit()