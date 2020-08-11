#Testing.py

import Helper
import pygame
pygame.init()


def buttonPressed():
	print("YEE")

run = True

win = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Testing")
button = Helper.button((30,30, 100, 50), (255,0,0), win, buttonPressed)
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill((255,255,255))
	button.draw()
	pygame.display.update()

