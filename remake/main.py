import pygame as pg
import random
from game import Game

from config import *

pg.init()
fps = pg.time.Clock()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Game()
while game.active:
    game.update()
    game.display(screen)
    pg.display.flip()
    pg.display.set_caption(str(fps))
    fps.tick(60)