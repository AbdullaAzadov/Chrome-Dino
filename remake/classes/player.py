import pygame as pg
from assets import asset
from utilities import *

class Jump:
    def __init__(self, start, heihgt, delta, gravity) -> None:
        self.down = start
        self.cur = start
        self.up = start - heihgt
        self.delta = delta
        self.cd = delta
        self.g = gravity
        self.cg = 0
        self.step = 0

    def update(self):
        if self.step == 1:
            self.cur -= self.cd
            if self.cd > self.delta/2:
                self.cd-=0.75
            if self.cur <= self.up:
                self.cur = self.up
                self.step = 2
            return self.cur

        elif self.step == 2:
            self.cur+= self.cg
            if self.cg < self.g:
                self.cg+=0.5
            if self.cur >= self.down:
                self.__reset()
            return self.cur        

    def __reset(self):
        self.cur = self.down
        self.step = 0
        self.cg = 0
        self.cd = self.delta


class Player:

    images = {"idle": asset['dino'], 
            "death": asset['dino_death'], 
            "sit_death": asset['dino_sit_death'],
            "move0": asset['dino_move0'],
            "move1": asset['dino_move1'], 
            "sit_move0": asset['dino_sit_move0'], 
            'sit_move1': asset['dino_sit_move1']}
    l = BoxData()
    r = BoxData()
    u = BoxData()
    d = BoxData()

    def __init__(self, l:int, d:int, jump=14, g=7) -> None:
        self.w = self.images['idle'].get_width()
        self.h = self.images['idle'].get_height()
        self.x = l
        self.y = d - self.h

        self.jump = Jump(self.y, 144, jump, g)
        self.state = 'M'
        
        self.keyFrameIndex = 0
        self.keyFrame = 0
        self.anim = "move"

    def update(self, pressed):
        self.control(pressed)
        self.__updateAnim(self.state)

        if self.state == "J":
            self.y = self.jump.update()
            if self.jump.step == 0:
                self.state = "M"
        

    def display(self, screen):
        screen.blit(self.images[self.anim], (self.x, self.y))
        
    def control(self, pressed):
        if (pressed[pg.K_SPACE] or pressed[pg.K_UP]) and self.state == 'M':
            self.jump.step = 1
            self.state = "J"
        #elif pressed[pg.K_DOWN]: self.Sitted = True
        #else: self.Sitted = False

    def __updateAnim(self, state):
        self.keyFrame += 1
        if self.keyFrame >= 12:
            self.keyFrame = 0
        if self.keyFrame in range(0, 6):
            self.keyFrameIndex = 0
        else:
            self.keyFrameIndex = 1
        
        if state == "S":
            self.anim = f'sit_move{self.keyFrameIndex}'
        elif state == "J":
            self.anim = 'idle'
        elif state == "M":
            self.anim = f'move{self.keyFrameIndex}'
