import pygame
import math
from grid import Grid
from drawer import Drawer
class Player:

    def __init__(self, color, position, size, speed, FOV):
        self.c = color
        self.x = position[0]
        self.y = position[1]
        self.sz = size
        self.sp = speed/50
        self.a = 0
        self.fov = FOV

    def draw(self, screen, posX, posY, tilesize):
        pygame.draw.circle(screen, self.c, (float(self.y*tilesize+posX), float(self.x*tilesize+posY)), self.sz)

    def drawSight(self, screen, posX, posY, tilesize):
        origin = (float(self.y*tilesize+posX), float(self.x*tilesize+posY))
        pygame.draw.line(screen, self.c, origin, 
                         (origin[0]+(tilesize*3*math.sin(math.radians(self.a))), 
                          origin[1]+(tilesize*3*math.cos(math.radians(self.a)))), 2)

    def drawRaycasts(self, screen:pygame.display, color:pygame.Color, posX:int, posY:int, tilesize:int, grid:Grid, screenSize:int, drawer:Drawer, renderDistance:int):
        for i in range(screenSize):
            self.drawRay(screen, color, posX, posY, tilesize, (self.fov/screenSize)*i, grid, i, drawer, renderDistance)
                              
    def drawRay(self, screen:pygame.display, color:pygame.color, posX:int, posY:int, tilesize:int, angle:int, grid:Grid,  position:int, drawer:Drawer, renderDistance:int):

        origin = (float(self.y*tilesize+posX), float(self.x*tilesize+posY))
        angleCast = self.a+angle-(self.fov/2)
        distance = self.getRayDistanceFromWall(angleCast, grid, renderDistance)
        # pygame.draw.line(screen, color,origin,
        #                   (origin[0]+(tilesize*1*
        #                         math.sin(math.radians(angleCast))*distance
        #                         ), 
        #                 origin[1]+(tilesize*1*
        #                         math.cos(math.radians(angleCast))*distance
        #                         )))
        if distance != False:
            drawer.draw(position, distance, renderDistance)

    def getRayDistanceFromWall(self, angle, grid, renderDistance):
        origin = [self.x, self.y]
        dzs = [0, 0]

        colliding = True
        distance = 0

        while colliding:
            distance+=0.01
            dzs[0] += math.cos(math.radians(angle))*0.01
            dzs[1] += math.sin(math.radians(angle))*0.01
            if grid.isColliding([math.floor(origin[0]+dzs[0]), math.floor(origin[1]+dzs[1])]):
                colliding = False
        colliding = True

        while colliding:
            distance += 1
            origin[0] += dzs[0]
            origin[1] += dzs[1]
            
            if distance > renderDistance:
                return False
            if grid.isColliding([math.floor(origin[0]), math.floor(origin[1])]):
                colliding = False
        distance-=1
        # return [math.floor(origin[0]+dzs[0]), math.floor(origin[1]+dzs[1])]
        return distance
       

    def getPos(self):
        return [math.floor(self.x), math.floor(self.y)]