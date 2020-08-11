#main
import pygame
from Helper import Button
import OpenFromPretrained as openfrmpre
import MyGame
pygame.init()

win = pygame.display.set_mode((1500,800))

bg = pygame.image.load("data/bg.png")
bg = pygame.transform.scale(bg, (1500,800))



def goToPreTrained():
	run = False
	openfrmpre.RUN()
def goToTraining():
	run = False
	MyGame.RUN()

goToPreTrainedButton = Button((210 - 30, 666, 250, 70), (0,0,255), win, goToPreTrained, "Go To Pretrained Model")
goToTrainingButton = Button((1060 + 30, 666, 200, 70), (0,0,255), win, goToTraining, "Train New Model", True)

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.blit(bg, (0,0))
	goToPreTrainedButton.draw()
	goToTrainingButton.draw()
	pygame.display.update()
pygame.quit()