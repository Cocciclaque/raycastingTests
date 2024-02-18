import pygame
from readIni import read

class Drawer:
    
    def __init__(self, screen, screenX, screenY, resolution, color, colorFar):
        self.s = screen
        self.x = screenX
        self.y = screenY
        self.res = resolution
        self.c = color
        self.cf = colorFar

    def draw(self, position:int, distance:int, renderDistance:int):
        height = (1/distance)*1000
        width = self.x/self.res

        rectStartLeft=self.x-((self.x/self.res)*position)-(self.x/self.res)
        rectStartTop=distance+(self.y/2.5)-(0.30*height)

        furthestPossible=renderDistance

        differenceR = int(self.cf[0]) - int(self.c[0])
        differenceG = int(self.cf[1]) - int(self.c[1])
        differenceB = int(self.cf[2]) - int(self.c[2])

        color = (int(self.c[0]) + (differenceR/furthestPossible*distance),
                 int(self.c[1]) + (differenceG/furthestPossible*distance),
                 int(self.c[2]) + (differenceB/furthestPossible*distance),
                 255
                 )        


        pygame.draw.rect(self.s, pygame.color.Color(color), (rectStartLeft, rectStartTop, width, height))