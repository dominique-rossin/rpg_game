import pygame
from mymap import *
import sys
from player import *
from random import *
from inventory import *
from enemy import *


pygame.init()

fps = 60
zoom_ecran = 1
deplacement_joueur = 0.1
resolution_ecran = (1280,720)
longueur_virtuelle = 30
tile_size = 16
largeur_virtuelle = round(longueur_virtuelle*resolution_ecran[1]/resolution_ecran[0])

#screen = pygame.display.set_mode((1280,720), pygame.FULLSCREEN|pygame.DOUBLEBUF)
screen = pygame.display.set_mode(resolution_ecran, pygame.DOUBLEBUF)
#screen2 = pygame.Surface((1920))
longueur, largeur = pygame.display.Info().current_w, pygame.display.Info().current_h
print(longueur," ",largeur)

coefficient_longueur = int(longueur/longueur_virtuelle)
coefficient_largeur = int(largeur/largeur_virtuelle)
print("coefs long/larg ",coefficient_longueur," ",coefficient_largeur)
zoom_ecran = int(min(coefficient_largeur,coefficient_longueur)/tile_size)

longueur_virtuelle = int(longueur / (tile_size* zoom_ecran))+1
largeur_virtuelle = int(largeur / (tile_size * zoom_ecran))+1

print("Zoom : ",zoom_ecran)

clock = pygame.time.Clock()
clock.tick(fps)

m = Map()
#print(zoom_ecran)
m.set_zoom(zoom_ecran)

inventory = Inventory(zoom_ecran)

player_x, player_y = longueur_virtuelle/2,largeur_virtuelle/2

player = Player(zoom_ecran)
player.set_pos(player_x,player_y)

inventory_pause = False


running = True
screen_x,screen_y = 0,0

haut = False
bas = False
gauche = False
droite = False

elapsed_time = 0

#inventory.change_inventory("sword",1)

inventory.change_inventory("sword",1)
inventory.change_inventory("shield",1)
inventory.change_inventory("heal_potion",1)
inventory.change_inventory("mana_potion",1)

enemies = pygame.sprite.Group()

enemy = Enemy(zoom_ecran,'slime-blue',tile_size,enemies)
enemy = Enemy(zoom_ecran,'slime-blue',tile_size,enemies)
enemy = Enemy(zoom_ecran,'slime-blue',tile_size,enemies)
enemy = Enemy(zoom_ecran,'slime-blue',tile_size,enemies)
enemyorange = Enemy(zoom_ecran,'slime-orange',tile_size,enemies)
enemy = Enemy(zoom_ecran,'worm-run-idle',tile_size,enemies)
enemy = Enemy(zoom_ecran,'worm-run-idle',tile_size,enemies)
enemy = Enemy(zoom_ecran,'worm-run-idle',tile_size,enemies)



while running:
	elapsed_time += clock.tick(fps)

	#print(inventory.check_open())

	if inventory.check_open() == False:
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
				if event.key == pygame.K_e:
					inventory.appeal()


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
				running = False

		if haut and not bas:
			player.move(0,-deplacement_joueur)

		if bas and not haut:
			player.move(0,deplacement_joueur)

		if gauche and not droite:
			player.move(-deplacement_joueur,0)

		if droite and not gauche:
			player.move(deplacement_joueur,0)

		if player.x-screen_x <= longueur_virtuelle/4:
			screen_x -= longueur_virtuelle/4-(player.x-screen_x)
			screen_x = max(0,screen_x)

		elif player.x-screen_x >=(longueur_virtuelle/4)*3:
			screen_x += (player.x-screen_x)-longueur_virtuelle*3/4
			screen_x = min(screen_x,longueur_virtuelle-1)

		if player.y-screen_y<=largeur_virtuelle/4:
			screen_y -= largeur_virtuelle/4-(player.y-screen_y)
			screen_y = max(0,screen_y)

		elif player.y-screen_y>=(largeur_virtuelle/4)*3:
			screen_y += player.y-screen_y-largeur_virtuelle*3/4
			screen_y = min(screen_y,largeur_virtuelle)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	else:
		haut,bas,gauche,droite = False, False, False, False
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					inventory.check_arrow(-3)
				if event.key == pygame.K_DOWN:
					inventory.check_arrow(3)
				if event.key == pygame.K_LEFT:
					inventory.check_arrow(1)
				if event.key == pygame.K_RIGHT:
					inventory.check_arrow(-1)
				if event.key == pygame.K_e:
					inventory.appeal()
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = event.pos
				inventory.check_arrow(x,y)
			if event.type == pygame.QUIT:
				running = False



	screen.fill((255,255,255))

	m.draw(screen,screen_x,screen_y,longueur_virtuelle,largeur_virtuelle)


	#player.idle(screen,x_limite*16,y_limite*16)

	if droite and not gauche or gauche and not droite or haut and not bas or bas and not haut:
		player.animate(elapsed_time)

	for enemy in enemies.sprites():
		enemy.animate(elapsed_time)
		enemy.draw(screen,screen_x,screen_y)

#	inventory.change_inventory("sword",5)
#	if inventory.check_invetory("sword",31):
#		print("test concluant")

	player.draw(screen,screen_x,screen_y)
	collision = pygame.sprite.collide_rect(player, enemyorange)
	if (collision):
		sys.exit()

	inventory.draw(screen)
			

	pygame.display.flip()
pygame.quit()