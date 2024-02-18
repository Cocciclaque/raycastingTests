import pygame
import math
import readIni
import readDat
from grid import Grid
from player import Player
from keyboard import Keyboard
import math
pygame.init()

#------------------Parameters---------------------
paramFile = r"data\data.ini"
params = readIni.read(paramFile)
map = readDat.read(params["level"])

#------------------World Variables----------------
run = True
dt = 0
fps = 144
clock = pygame.time.Clock()
grid = Grid(params['tilesize'], map[0], map[1])
screen = pygame.display.set_mode((int(params['sizeX']),int(params['sizeY'])))

        #---------Player Variables----------------
pAxis = p1Axis = {'vertical':[0, [pygame.K_z, pygame.K_s]], 'horizontal':[0, [pygame.K_q, pygame.K_d]]}
kb = Keyboard(pAxis)
player = Player(params['playerColor'], [5, 2], 5, .02, 70)

#------------------Main Loop----------------------
while run:
    screen.fill(params['screenFillColor'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #--------------Player Movement---------------
    pAxis = kb.get()
    if pAxis['vertical'][0] != 0:
        preposX = player.x
        preposY = player.y
        
        player.x += math.cos(math.radians(player.a))*player.sp * pAxis['vertical'][0] * -1 * int(params['tilesize']) * dt
        
        if grid.isColliding(player.getPos()):
            player.x = preposX
        
        player.y += math.sin(math.radians(player.a))*player.sp * pAxis['vertical'][0] * -1 * int(params['tilesize']) * dt
        
        if grid.isColliding(player.getPos()):
            player.y = preposY
            
    if pAxis['horizontal'][0] != 0:
        player.a += pAxis['horizontal'][0]*player.sp*-1*dt*350

    
    
    #--------------Draws-------------------------
    grid.draw(screen, params['wallColorGrid'], 0, int(params['sizeY'])-(int(params['tilesize'])*grid.dy))
    player.draw(screen, 0, int(params['sizeY'])-(int(params['tilesize'])*grid.dy), int(params['tilesize']))
    # player.drawSight(screen, 0, int(params['sizeY'])-(int(params['tilesize'])*grid.dy), int(params['tilesize']))
    player.drawRaycasts(screen, params['rayCastColor'], 0, int(params['sizeY'])-(int(params['tilesize'])*grid.dy), int(params['tilesize']), grid, int(params['resX']))
    dt = clock.tick(fps)
    pygame.display.flip()
pygame.quit()