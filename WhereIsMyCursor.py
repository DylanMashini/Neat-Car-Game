#Where is My Cursor
import pygame
pygame.init()

win = pygame.display.set_mode((1500,800))
pygame.display.set_caption("Where is my cursor?")
bg = pygame.image.load("data/map.png")
win.blit(bg, (0,0))
pygame.display.update()
run = True
while run:
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

#Notes
#Point spots
#1. 861,684

#2. 1213, 647

#3. 1227, 103

#4. 182, 192

#5. 570, 259

#6. 740, 364

#7. 1026, 269

#8. 986, 527

#9. 336, 433

#10. 262, 665

