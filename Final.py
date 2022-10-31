import pygame
import random
import sys

pygame.init()

#กำหนดขนาดเกม
W = 800
H = 600

#กำหนดสี
White = (240,255,255)
Red = (220,20,60)
YELLOW = (255,255,0)
BG_Cl = (0,0,0)

player_size = 50
player_pos = [400, 500]

e_size = 25
e_pos = [random.randint(0,775), 0]
e_list = [e_pos]

SPEED = 10

screen = pygame.display.set_mode((W, H))

Lose = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)



#สร้างอุปสรรคโดยการสุ่มเกิด
def drop_enemies(e_list):
	delay = random.random()
	if len(e_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,775)
		y_pos = 0
		e_list.append([x_pos, y_pos])

#ฟังก์ชันทำให้เห็นอุปสรรค
def appear_enemies(e_list):
	for e_pos in e_list:
		pygame.draw.rect(screen, Red, (e_pos[0], e_pos[1], e_size, e_size))

def enemy_pos(e_list, score):
	for idx, e_pos in enumerate(e_list):
		if e_pos[1] >= 0 and e_pos[1] < H:
			e_pos[1] += SPEED
		else:
			e_list.pop(idx)
			score += 1
	return score

def collision_check(e_list, player_pos):
	for e_pos in e_list:
		if detect_collision(e_pos, player_pos):
			return True
	return False

def detect_collision(player_pos, e_pos):
	player_x = player_pos[0]
	player_y = player_pos[1]

	e_x = e_pos[0]
	e_y = e_pos[1]

	if (e_x >= player_x and e_x < (player_x + player_size)) or (player_x >= e_x and player_x < (e_x+e_size)):
		if (e_y >= player_y and e_y < (player_y + player_size)) or (player_y >= e_y and player_y < (e_y+e_size)):
			return True
	return False

while not Lose:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size

			player_pos = [x,y]

	screen.fill(BG_Cl)

	drop_enemies(e_list)
	score = enemy_pos(e_list, score)




	if collision_check(e_list, player_pos):
		game_over = True
		break

	appear_enemies(e_list)

	pygame.draw.rect(screen, White, (player_pos[0], player_pos[1], player_size, player_size))

	clock.tick(30)

	pygame.display.update()