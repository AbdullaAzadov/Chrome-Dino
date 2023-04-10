import pygame, random
from settings import *
def generateEnemy(sp, gr):
    Rpos = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
    cnt = random.randint(1, 6)
    Rtype = random.randint(0, 1)
    if sp < 8: 
        cnt = cnt % 5
        if cnt == 0: cnt+= 1
        Rtype = 0
    if Rtype == 0:
        Rw = 34 * cnt
        Rh = 70
    else:
        Rw = 50 * cnt
        Rh = 100
    Rsurf = pygame.Surface((Rw, Rh), pygame.SRCALPHA)
    return Rpos, gr - Rh, Rsurf, Rtype, Rw, Rh, 