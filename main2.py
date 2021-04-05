import pygame
from mymap import *
from player import *


pygame.init()

fps = 60
zoom_ecran = 1
longueur_virtuelle = 30
largeur_virtuelle = round(longueur_virtuelle*9/16)

screen = pygame.display.set_mode((longueur_virtuelle,largeur_virtuelle), pygame.FULLSCREEN)

longueur, largeur = pygame.display.Info().current_w, pygame.display.Info().current_h


coefficient_longueur = round(longueur/longueur_virtuelle)
coefficient_largeur = round(largeur/largeur_virtuelle)
zoom_ecran = min(coefficient_largeur,coefficient_longueur)

clock = pygame.time.Clock()
clock.tick(fps)

m = Map()
player = Player()



running = True
player_x, player_y = longueur_virtuelle/2,largeur_virtuelle/2
x_limite, y_limite = player_x, player_y

haut = False
bas = False
gauche = False
droite = False

elapsed_time = 0

while running:
	elapsed_time += clock.tick(fps)

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
		y_limite -= 0.5
		player_y -= 0.5
		player_y_move = 0.5

	if bas:
		y_limite += 0.5
		player_y += 0.5
		player_y_move = -0.5

	if gauche:
		x_limite -= 0.5
		player_x -= 0.5
		player_x_move = 0.5

	if droite:
		x_limite += 0.5
		player_x += 0.5
		player_x_move = -0.5

	if x_limite < longueur_virtuelle/4:
		x_limite = longueur_virtuelle/4

	if x_limite > (longueur_virtuelle/4)*3:
		x_limite = (longueur_virtuelle/4)*3

	if y_limite < largeur_virtuelle/4:
		y_limite = largeur_virtuelle/4

	if y_limite > (largeur_virtuelle/4)*3:
		y_limite = (largeur_virtuelle/4)*3


	if x_limite<=longueur_virtuelle/4:
		if gauche:
			m.scroll_x(player_x_move)

	elif x_limite>=(longueur_virtuelle/4)*3:
		if droite:
			m.scroll_x(player_x_move)

	if y_limite<=largeur_virtuelle/4:
		if haut:
			m.scroll_y(player_y_move)

	elif y_limite>=(largeur_virtuelle/4)*3:
		if bas:
			m.scroll_y(player_y_move)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((255,255,255))
	m.draw(screen,5,5)


	player.idle(screen,x_limite*16,y_limite*16)

	if droite or gauche:
		if elapsed_time >= 100:
			elapsed_time = 0
			player.animate(screen,x_limite*16,y_limite*16)

	pygame.display.flip()
pygame.quit()