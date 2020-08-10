#Map Preprocessing
import pygame
import pickle as pkl
import time
run = True
pygame.init()
whitespots = []
filesaveName = input("What should I save the data as?")
win = pygame.display.set_mode((1500, 800))
pygame.display.set_caption("Map preprocessing")
bg = pygame.image.load("map.png")
count = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    count += 1
    win.blit(bg, (0,0))
    if count == 50:
        run = False
    pygame.display.update()

for x in range(0, 1500):
    for y in range(0,800):
        print(x,y)
        color = win.get_at((x,y))
        if color == (255,255,255,255):
            whitespots.append((x,y))
print(len(whitespots))
print(1500*800)
print(type(set(whitespots)))
pkl.dump( set(whitespots), open( filesaveName + ".pkl", "wb" ) )

        


pygame.quit()
    
    
