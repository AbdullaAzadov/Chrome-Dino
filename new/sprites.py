import pygame, random
from path import *

dino = pygame.transform.scale(pygame.image.load(path + "dino.png"), (324, 225))
dino_walk = [
    pygame.transform.scale(pygame.image.load(path + "dino_w0.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w1.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w2.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w3.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w4.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w5.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w6.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w7.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_w8.png"), (324, 225)),
    ]
dino_walk_cntr = 0
rand01 = random.randint(0, 1)
ground_img = pygame.image.load(path + f"back{rand01}.jpg")
tmp_ground_img = pygame.image.load(path + f"back{2 + rand01}.jpg")

dino_jump = [
    pygame.transform.scale(pygame.image.load(path + "dino_r2.png"), (324, 225)),
    pygame.transform.scale(pygame.image.load(path + "dino_r4.png"), (324, 225)),
]
dino_jump_cntr = random.randint(0, 1)
