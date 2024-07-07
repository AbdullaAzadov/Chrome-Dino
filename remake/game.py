import pygame as pg
from classes.player import Player
from classes.ground import Ground
from config import SCREEN_HEIGHT as H, SCREEN_WIDTH as W

class Game:
    
    def __init__(self):
        self.active = True
        self.over = False
        self.frame = 0
        self.score = 0
        self.ground = Ground(int(H*.8))
        self.player = Player(int(W*.15), self.ground.d)
        self.speed = 3.5

    def update(self):
        self.frame+=1
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.active = False
        if not self.over:
            pressed = pg.key.get_pressed()
        
        self.ground.update(self.speed)
        self.player.update(pressed)
    
    def display(self, screen):
        self.ground.display(screen)
        self.player.display(screen)