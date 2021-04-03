import pygame
from mymap import *
from player import *

pygame.init()
longueur,largeur = 0,0
fps = 60
screen = pygame.display.set_mode((longueur,largeur), pygame.FULLSCREEN)

longueur, largeur = pygame.display.Info().current_w, pygame.display.Info().current_h

longueur_virtuelle = 400
largeur_virtuelle = 225

coefficient_longueur = round(longueur/longueur_virtuelle)
coefficient_largeur = round(largeur/largeur_virtuelle)

clock = pygame.time.Clock()
clock.tick(fps)

m = Map()

player = player()
player.draw()




running = True
player_x, player_y = 0,0

haut = False
bas = False
gauche = False
droite = False

while running:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_UP:
				haut = True

			if event.key == pygame.K_DOWN:
				bas = True

			if event.key == pygame.K_LEFT:
				gauche = True

			if event.key == pygame.K_RIGHT:
				droite = True

		if event.type == pygame.KEYUP:

			if event.key == pygame.K_UP:
				haut = False

			if event.key == pygame.K_DOWN:
				bas = False

			if event.key == pygame.K_LEFT:
				gauche = False

			if event.key == pygame.K_RIGHT:
				droite = False
						
		if event.type == pygame.QUIT:
			pygame.quit()
			Fin = True

	if haut:
		player_y -= 0.5

	if bas:
		player_y += 0.5

	if gauche:
		player_x -= 0.5

	if droite:
		player_x += 0.5

	m.scroll_x(player_x)
	m.scroll_y(player_y)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255,255,255))
	m.draw(screen,5,5)
	pygame.display.flip()
pygame.quit()