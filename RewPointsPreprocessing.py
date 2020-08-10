#RewPoints PreProcessing
import pygame
import pickle as pkl
pygame.init()
win = pygame.display.set_mode((1500,800))
pygame.display.set_caption("RewPoints pre processing")
bg = pygame.image.load("data/map.png")
win.blit(bg, (0,0))
pygame.display.update()
run = True
RewPoints = [(861,692), (1213, 647), (1227, 103), (182, 192), (570, 259), (740, 364), (1026, 269), (986, 527), (336, 433), (262, 665)]
count = 0
greenspots = []
while run:
    count += 1
    
    pygame.draw.circle(win, (0,255,0,255), RewPoints[9], 70)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if count == 10:
        run = False
for x in range(0, 1500):
    for y in range(0,800):
        
        color = win.get_at((x,y))
        if color == (0,255,0,255):
            print(x,y)
            greenspots.append((x,y))
greenspots = set(greenspots)
pkl.dump(greenspots, open("data/rewPoints/9.pkl", "wb" ))
        
pygame.quit()
        

