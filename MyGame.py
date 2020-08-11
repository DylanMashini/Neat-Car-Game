#MY GAME
import pygame
import pickle as pkl
import math
import neat

boundries = pkl.load(open("data/map.pkl", "rb"))

generation = 0
    

class Car():
    def __init__(self):
        self.RewPoints = []

        for i in range(10):
            rewpoint = pkl.load(open("data/rewPoints/" + str(i) + ".pkl", "rb"))
            self.RewPoints.append(rewpoint)
        self.SpeedCounter = 0
        self.RenderDead = False
        self.rewpointsachived = [False, False, False ,False, False, False, False, False, False, False]
        self.fitness = 0
        self.isAllive = True
        self.x = 525
        self.y = 650
        self.center = [self.x + 50, self.y + 50]
        self.angle = 0
        self.vel = 6
        self.standingVel = 6
        len = 40
        self.turningvel = 5
        self.img = pygame.image.load("data/car.png")
        self.top_line = ([self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * len], [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * len])
        self.img = pygame.transform.scale(self.img, (100,100))
        self.rotImg = self.img
        
        
        self.radars = [radar(self.top_line[0],45), radar(self.top_line[1], -45), radar(findMidpoint(self.top_line[0], self.top_line[1]), 0, 100)]
        
        
    def left(self):
        if self.isAllive:
            self.angle += self.turningvel
            self.rotImg = self.rot_center(self.img, self.angle)

    def right(self):
        if self.isAllive:
            self.angle -= self.turningvel
            self.rotImg = self.rot_center(self.img, self.angle)
        
    def go(self):
        if self.isAllive:
            self.x += math.cos(math.radians(360 - self.angle)) * self.vel
            self.y += math.sin(math.radians(360 - self.angle)) * self.vel
            self.SpeedCounter = 0
        
    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
#        rot_rect = rot_image.get_rect()
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    def getCollisionPoints(self):
        len = 40
        
        self.center = [int(self.x) + 50, int(self.y) + 50]
        self.middletopx = (self.top_line[0][0] + self.top_line[1][0]) / 2
        self.top_line = ([self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * len], [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * len])
        
        self.bottom_line = ([self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * len], [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * len])
        
        self.top_line[0][0] += math.cos(math.radians(360 - self.angle)) * 15
        self.top_line[0][1] += math.sin(math.radians(360 - self.angle)) * 15
        self.top_line[1][0] += math.cos(math.radians(360 - self.angle)) * 15
        self.top_line[1][1] += math.sin(math.radians(360 - self.angle)) * 15
        self.bottom_line[0][0] += math.cos(math.radians(360 - self.angle)) * -15
        self.bottom_line[0][1] += math.sin(math.radians(360 - self.angle)) * -15
        self.bottom_line[1][0] += math.cos(math.radians(360 - self.angle)) * -15
        self.bottom_line[1][1] += math.sin(math.radians(360 - self.angle)) * -15
        return (self.top_line, self.bottom_line)
    
    

        
        
    def amIDead(self):
        top, bottom = self.getCollisionPoints()
        top[0][0] = int(top[0][0])
        top[0][1] = int(top[0][1])
        top[1][0] = int(top[1][0])
        top[1][1] = int(top[1][1])
        bottom[0][0] = int(bottom[0][0])
        bottom[0][1] = int(bottom[0][1])
        bottom[1][0] = int(bottom[1][0])
        bottom[1][1] = int(bottom[1][1])
        
        points = [top[0],bottom[1], top[1],bottom[0]]
        for i in points:
            #True means that there was a collision.
            
            tup = (i[0], i[1])
            opp = tup in boundries
            count = 0
            if self.rewpointsachived[0] is False:
                rew = tup in self.RewPoints[0]
                if rew:
                    self.rewpointsachived = [True, False, False ,False, False, False, False, False, False, False]
                    self.addRew()
            elif self.rewpointsachived[1] is False:
                rew = tup in self.RewPoints[1]
                if rew:
                    self.rewpointsachived[1] = True
                    self.addRew()
            elif self.rewpointsachived[2] is False:
                rew = tup in self.RewPoints[2]
                if rew:
                    self.rewpointsachived[2] = True
                    self.addRew()
            elif self.rewpointsachived[3] is False:
                rew = tup in self.RewPoints[3]
                if rew:
                    self.rewpointsachived[3] = True
                    self.addRew()
            elif self.rewpointsachived[4] is False:
                rew = tup in self.RewPoints[4]
                if rew:
                    self.rewpointsachived[4] = True
                    self.addRew()
            elif self.rewpointsachived[5] is False:
                rew = tup in self.RewPoints[5]
                if rew:
                    self.rewpointsachived[5] = True
                    self.addRew()
            elif self.rewpointsachived[6] is False:
                rew = tup in self.RewPoints[6]
                if rew:
                    self.rewpointsachived[6] = True
                    self.addRew()
            elif self.rewpointsachived[7] is False:
                rew = tup in self.RewPoints[7]
                if rew:
                    self.rewpointsachived[7] = True
                    self.addRew()
            elif self.rewpointsachived[8] is False:
                rew = tup in self.RewPoints[8]
                if rew:
                    self.rewpointsachived[8] = True
                    self.addRew()
            elif self.rewpointsachived[9] is False:
                rew = tup in self.RewPoints[9]
                if rew:
                    self.rewpointsachived[9] = True
                    self.rewpointsachived[0] = False
                    self.addRew()

            if opp:
                self.isAllive = False
                if self.RenderDead:
                    self.img = pygame.image.load("data/dead_car.png")
                
                self.img = pygame.transform.scale(self.img, (100,100))
                self.rotImg = self.rot_center(self.img, self.angle)
    def standing(self):
        if self.isAllive:
            self.updateRadars()
            self.x += math.cos(math.radians(360 - self.angle)) * self.standingVel
            self.y += math.sin(math.radians(360 - self.angle)) * self.standingVel
            self.SpeedCounter += 1
            if self.SpeedCounter == 40:
                self.isAllive = False
        
    def addRew(self):
        self.fitness += 10
    def updateRadars(self):

        
        startpoints = [self.top_line[0], self.top_line[1], findMidpoint(self.top_line[0], self.top_line[1])]
        count = 0
        for radar in self.radars:
            radar.collPoint = None
            radar.startPoint = startpoints[count]
            count += 1
            radar.angle = self.angle + radar.startangle
            radar.checkCollision()
    def getData(self):
        data = [0, 0, 0]
        for index, radar in enumerate(self.radars):
            if radar.d2coll is not None:
                data[index] = radar.d2coll
        return data
            
        
        
        
        
class radar():
    def __init__(self, startPoint, angle, length=80):
        self.startPoint = startPoint
        self.startangle = angle
        self.angle = angle
        self.length = length
        self.collPoint = None
        self.d2coll = None
        self.endPoint = (startPoint[0] + (math.cos(math.radians(360 - self.angle)) * self.length), startPoint[1] + math.sin(math.radians(360 - self.angle)) * 80)
        self.line = (self.startPoint, self.endPoint)
    def checkCollision(self):
        
        self.endPoint = (self.startPoint[0] + (math.cos(math.radians(360 - self.angle)) * self.length), self.startPoint[1] + math.sin(math.radians(360 - self.angle)) * self.length)
        x = self.startPoint[0]
        y = self.startPoint[1]
        
        seenwhite = False
        count = 0
        for _ in range(0, self.length):
            if not seenwhite:
                opp = (int(x),int(y)) in boundries
                count += 1
                if opp:
                    self.d2coll = count
                    seenwhite = True
                    self.collPoint = (int(x), int(y))
            # if opp is true than radar is in the white.
            x += math.cos(math.radians(360 - self.angle)) * 1
            y += math.sin(math.radians(360 - self.angle)) * 1

    
            

            

    
        
def findMidpoint(p1,p2):
    return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2
    

def draw():
    win.fill((0,0,0))
    win.blit(bg, (0,0))
#    for rewpoint in RewPoints:
#        pygame.draw.circle(win, (0,255,0), rewpoint, 70, 2)
    for car in cars:
        if car.RenderDead or car.isAllive:
            car.standing()
            win.blit(car.rotImg, (car.x, car.y))
            for radar in car.radars:
                pygame.draw.line(win, (0,0,255), radar.startPoint, radar.endPoint, 3)
                if radar.collPoint is not None:

                    pygame.draw.circle(win, (255,0,0), radar.collPoint, 3)
        
        #Draws Box
#        top_line, bottom_line = car.getCollisionPoints()
#        top_line[0][0] = int(top_line[0][0])
#        top_line[0][1] = int(top_line[0][1])
#        top_line[1][0] = int(top_line[1][0])
#        top_line[1][1] = int(top_line[1][1])
#        bottom_line[0][0] = int(bottom_line[0][0])
#        bottom_line[0][1] = int(bottom_line[0][1])
#        bottom_line[1][0] = int(bottom_line[1][0])
#        bottom_line[1][1] = int(bottom_line[1][1])
#        pygame.draw.line(win, (0,0,255), top_line[0], top_line[1],1)
#        pygame.draw.line(win, (0,0,255), bottom_line[0], bottom_line[1],1)
#        pygame.draw.line(win, (0,0,255), top_line[0], bottom_line[1], 1)
#        pygame.draw.line(win, (0,0,255), top_line[1], bottom_line[0], 1)
        if car.amIDead() is True:
            run = False
  
    pygame.display.update()
    


def run_car(genomes, config):
    pygame.init()

    win = pygame.display.set_mode((1500, 800))
    pygame.display.set_caption("car game")
    bg = pygame.image.load("data/map.png")
    x,y = 50, 50
    nets = []
    cars = []
    for id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0
        cars.append(Car())
    run = True
    global generation
    generation += 1
    while run:
        pygame.time.delay(0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        for index, car in enumerate(cars):
            output = nets[index].activate(car.getData())
            i = output.index(max(output))
            if i == 0:
                car.left()
            elif i == 1:
                car.right()
            elif i == 2:
                car.go()
            #update fitness
            remaining_cars = 0
            for index,car in enumerate(cars):
                if car.isAllive:
                    remaining_cars += 1
                    genomes[index][1].fitness = car.fitness
                
        if remaining_cars == 0:
            break

        

        
        win.fill((0,0,0))
        win.blit(bg, (0,0))
        #    for rewpoint in RewPoints:
        #        pygame.draw.circle(win, (0,255,0), rewpoint, 70, 2)
        for car in cars:
            if car.RenderDead or car.isAllive:
                car.standing()
                car.amIDead()
                win.blit(car.rotImg, (car.x, car.y))
                for radar in car.radars:
                    pygame.draw.line(win, (0,0,255), radar.startPoint, radar.endPoint, 3)
                    if radar.collPoint is not None:

                        pygame.draw.circle(win, (255,0,0), radar.collPoint, 3)
                    
        pygame.display.update()


    


def RUN():
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
    neat.DefaultSpeciesSet, neat.DefaultStagnation, "data/config-feedforward.txt")
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)



    # Runs NEAT for 5 generations, than saves model
    winner = p.run(run_car, 25)
    pkl.dump(winner, open("25_generations.pkl", "wb"))
    
pygame.quit()

#rects are X, Y, Width, Height
