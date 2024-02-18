import pygame
import math
from grid import Grid
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

    def drawRaycasts(self, screen:pygame.display, color:pygame.Color, posX:int, posY:int, tilesize:int, grid:Grid, screenSize:int):
        baseOffsetCos = math.cos(self.a+self.fov)
        baseOffsetSin = math.sin(self.a+self.fov)
        raypos=[self.x, self.y]
        for i in range(screenSize):
            self.drawRay(screen, color, posX, posY, tilesize, (self.fov/screenSize)*i, grid)
            
            # OffsetCos = baseOffsetCos+math.cos(self.fov)
            # pygame.draw.line(screen, color, (float(self.y*tilesize+posX), float(self.x*tilesize+posY)), 
            #                  (float(self.y*tilesize+posX+(tilesize*6*baseOffsetSin)), 
            #                   float(self.x*tilesize+posY+(tilesize*6*baseOffsetCos))),1)
                              
    def drawRay(self, screen:pygame.display, color:pygame.color, posX:int, posY:int, tilesize:int, angle:int, grid:Grid):
        
        pygame.draw.line(screen, color,(float(self.y*tilesize+posX), float(self.x*tilesize+posY)),
                          (float(self.y*tilesize+posX+(tilesize*6*
                                math.sin(math.radians(self.a+angle-(self.fov/2)))
                                )), 
                        float(self.x*tilesize+posY+(tilesize*6*
                                math.cos(math.radians(self.a+angle-(self.fov/2)))
                                ))))
        
    def getPos(self):
        return [math.floor(self.x), math.floor(self.y)]