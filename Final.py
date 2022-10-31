import pygame
import random
import sys

pygame.init()

#กำหนดขนาดเกม
W = 750
H = 550

#กำหนดสี
White = (240,255,255)
Red = (220,20,60)
YELLOW = (255,255,0)
BG_Cl = (0,0,0)

p_size = 50
p_pos = [400, 500]

e_size = 30
e_pos = [random.randint(0,775), 0]
e_list =[e_pos]

SPEED = 15

show = pygame.display.set_mode((W, H))

Lose = False

score = 0

clock = pygame.time.Clock()





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
		pygame.draw.rect(show, Red, (e_pos[0], e_pos[1], e_size, e_size))

def enemy_pos(e_list, score):
	for idx, e_pos in enumerate(e_list):
		if e_pos[1] >= 0 and e_pos[1] < H:
			e_pos[1] += SPEED
		else:
			e_list.pop(idx)
			score += 1
	return score

def collision_check(e_list, p_pos):
	for e_pos in e_list:
		if detect_collision(e_pos, p_pos):
			return True
	return False

def detect_collision(p_pos,e_pos):
	player_x = p_pos[0]
	player_y = p_pos[1]

	e_x = e_pos[0]
	e_y = e_pos[1]

	if (e_x >= player_x and e_x < (player_x + p_size)) or (player_x >= e_x and player_x < (e_x + e_size)):
		if (e_y >= player_y and e_y < (player_y + p_size)) or (player_y >= e_y and player_y < (e_y + e_size)):
			return  True
	return False

while not Lose:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = p_pos[0]
			y = p_pos[1]

			if event.key == pygame.K_LEFT:
				x -= p_size
			elif event.key == pygame.K_RIGHT:
				x += p_size

			p_pos = [x,y]

	show.fill(BG_Cl)

	drop_enemies(e_list)
	score = enemy_pos(e_list, score)




	if collision_check(e_list, p_pos):
		game_over = True
		break

	appear_enemies(e_list)

	pygame.draw.rect(show, White, (p_pos[0], p_pos[1], p_size, p_size))

	clock.tick(40)

	pygame.display.update()