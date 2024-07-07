import pygame as pg
from assets import asset
from utilities import *
from config import SCREEN_HEIGHT, SCREEN_WIDTH, GREY

class GroundTile:
    l = BoxData()
    r = BoxData()
    u = BoxData()
    d = BoxData()
    def __init__(self, x, y, image, rBorder) -> None:
        self.x = x
        self.y = y
        self.image = image
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rBorder = rBorder
        self.lBorder = 0

    def update(self, delta):
        self.x-=delta
        if self.r <= self.lBorder:
            self.x = self.rBorder
    
    def display(self, s):
        s.blit(self.image, (self.x, self.y))

class Ground:
    l = BoxData()
    r = BoxData()
    u = BoxData()
    d = BoxData()
    images = {"left": asset['ground0'], "right":asset['ground1']}
    def __init__(self, d:int) -> None:
        self.w = self.images['left'].get_width()
        self.h = self.images['left'].get_height()
        self.x = 0
        self.y = d - self.images['left'].get_height()
        self.leftTile = GroundTile(self.x, self.y, self.images['left'], SCREEN_WIDTH)
        self.rightTile = GroundTile(self.r, self.y, self.images['right'], SCREEN_WIDTH)

    def update(self, delta:int):
        self.leftTile.update(delta)
        self.rightTile.update(delta)

    def display(self, s):
        s.fill(GREY)
        self.leftTile.display(s)
        self.rightTile.display(s)
