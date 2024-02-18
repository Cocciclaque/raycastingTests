import pygame

class Grid:

    def __init__(self, tilesize:int, dimensions:list[int], grid:list[list[int]]):
        self.t = int(tilesize)
        self.dx = int(dimensions[0])
        self.dy = int(dimensions[1])
        self.g = grid 

    def draw(self, screen, color, posX, posY):

        for x in range(len(self.g)):
            for y in range(len(self.g[x])):
                if self.g[x][y] == '1':
                    pygame.draw.rect(screen, color, (float(y*self.t+posX), float(x*self.t+posY), float(self.t), float(self.t)))

    def isColliding(self, position):
        posX = position[0]
        posY = position[1]
        try:
            if self.g[posX][posY] == '1':
                return True
        except:
            pass
        return False
    
