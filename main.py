import numpy as np
import pygame
import sys
import math
import random
import time
pygame.init()


class planet:
    def __init__(self, mass, pos):
        self.mass = mass
        self.pos = pos

class partical:
    def __init__(self ,pos, mass):
        self.pos = pos
        self.velocity = np.array((0,0.0))
        self.acc = np.array((0.0,0.0))
        self.mass = mass


    def draw(self,surface):
        surface.set_at((int(self.pos[0]), int(self.pos[1])), (255,100,100))

    

    def update(self, gravmap):

        self.acc = np.array((0.0,0.0))

        try:
            self.acc[0] += gravmap[int(self.pos[0])]
            self.acc[1] +=  gravmap[int(self.pos[1])]
        except:
            pass
        
        self.velocity += self.acc

    def move(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]


def gray(color):
    if color > 255:
        return (255,255,255)
    elif color < 0:
        return (0,0,0)
    return (color,color,color)

def inverted(color):
    if color > 255:
        return (0,0,0)
    elif color < 0:
        return (255,255,255)
    return (255-color,255-color,255-color)

def makemap(gravmap, planet):
    for x in range(len(gravmap)):
        for y in range(len(gravmap[x])):
            distancex = planet.pos[0]-x
            distancey = planet.pos[1]-y

            #gravmap[x][y][0] += planet.mass/(distancex*distancex) if distancex !=0 else planet.mass
            #gravmap[x][y][1] += planet.mass/(distancey*distancey) if distancey !=0 else planet.mass

            gravmap[x][y][0] += planet.mass/distancex if distancex !=0 else planet.mass
            gravmap[x][y][1] += planet.mass/distancey if distancey !=0 else planet.mass




size = (320*2,240*2)
gravitymap = np.zeros((size[0],size[1],2))

planets = [planet(random.uniform(10, 255),[random.randint(0+20, size[0]-20),random.randint(0+20, size[1]-20)]) for _ in range(1)]

for i in planets:
    makemap(gravitymap,i)


screen = pygame.display.set_mode(size)

mainpart = partical([random.randint(0+20, size[0]-20),random.randint(0+20, size[1]-20)],100)

screen.fill((0,0,0))
for x in range(len(gravitymap)):
    for y in range(len(gravitymap[x])):
        screen.set_at((x, y), gray(math.hypot(gravitymap[x][y][0],gravitymap[x][y][1])))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    mainpart.draw(screen)
    mainpart.update(gravitymap)
    mainpart.move()
    pygame.display.flip()
    
