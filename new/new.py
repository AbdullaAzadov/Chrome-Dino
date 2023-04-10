import pygame
import random
from sprites import *
from path import *
from settings import *
from generator import *
# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (224, 224, 224)

fps = pygame.time.Clock()
# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)


# Объявление спрайтов
dino_death = pygame.image.load(path + "dino_d.png")
dino_sit_death = pygame.image.load(path + "dino_sd.png")
dino_sit_move = [pygame.image.load(path + "dino_sm0.png"), pygame.image.load(path + "dino_sm1.png")]
cactus = [pygame.image.load(path + "cactus0.png"), pygame.image.load(path + "cactus1.png")]
cactus_type = 0
gamovr = pygame.image.load(path + "go.png")
rest = pygame.image.load(path + "btn.png")
# Текст
font = pygame.font.Font(None, 36)

# Создание земли
ground_x = 0
ground = 700 - random.randint(1, 45)
tmp_ground_x = SCREEN_WIDTH

# Создание "персонажа"
dino_width = 137
dino_height = 197
dino_top = 187
dino_x = SCREEN_WIDTH // 10
dino_y = ground - dino_height
dino_prev_y = 0
hold_in_space = 0
jump_force = 128
isGround = True
g = 7

# Создание врага
enemy_width = 34
enemy_height = 70
enemy_x = SCREEN_WIDTH
enemy_y = ground - enemy_height
enemy_speed = 3.5
enemy_surf = pygame.Surface((enemy_width, enemy_height), pygame.SRCALPHA)
# Счет игрока
score = 0
frame = 0


# Основной игровой цикл
play = True
GameOver = False

while play:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    if not GameOver:
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_SPACE] or pressed[pygame.K_UP]) and isGround: dino_y -= g

    # Проверка стоит ли дино на земле
        if (dino_prev_y == dino_y and dino_prev_y != 0) or dino_y < ground - jump_force - dino_height: isGround = False
        if not isGround:
            hold_in_space+= 1
            if hold_in_space >= 15 or (dino_y >= ground - jump_force - dino_height) and 0:
                dino_y += g
                if dino_y > ground - dino_height:
                    dino_y = ground - dino_height
                    isGround = True
                    hold_in_space = 0
            elif hold_in_space >= 10: dino_y -= 1
            elif hold_in_space >= 5: dino_y -= 3
            else: dino_y -= 5
    
    # Перемещение и генерация врагов
        enemy_surf.blit(cactus[cactus_type], (0, 0))
        enemy_x -= enemy_speed
        if enemy_x < -enemy_width:
            enemy_x, enemy_y, enemy_surf, cactus_type, enemy_width, enemy_height = generateEnemy(enemy_speed, ground)
            if enemy_speed <= 16: 
                enemy_speed += random.randint(1, 6) / 10

    # Проверка на столкновение врага и дино
        if ((dino_x+16 in range(int(enemy_x), int(enemy_x + enemy_width+1)) or
            dino_x-24 + dino_width in range(int(enemy_x), int(enemy_x + enemy_width+1))) and 
        (dino_y + dino_height in range(int(enemy_y+24), int(enemy_y + enemy_height+1)))): pass
            #GameOver = True

    # Перемещение фона 
        ground_x -= enemy_speed
        tmp_ground_x -= enemy_speed
        if ground_x <= -SCREEN_WIDTH: ground_x = SCREEN_WIDTH
        if tmp_ground_x <= -SCREEN_WIDTH: tmp_ground_x = SCREEN_WIDTH

    # Отрисовка фона
        screen.fill(RED)
        screen.blit(ground_img, (ground_x, 0))
        screen.blit(tmp_ground_img, (tmp_ground_x, 0))

    # Отрисовка врага
        screen.blit(enemy_surf, (enemy_x, enemy_y))

    # Отрисовка Дино
        if not frame % 3: dino_walk_cntr = (dino_walk_cntr + 1) % 9
        if isGround: screen.blit(dino_walk[dino_walk_cntr], (dino_x, dino_y))
        else: screen.blit(dino, (dino_x, dino_y))
 
    # Отрисовка счета
        text = font.render("Счет: " + str(int(score/100)), 1, BLACK)
        screen.blit(text, (10, 10))

        print(ground_x, tmp_ground_x)
    # Обновление экрана
        #dino_prev_y = dino_y
        score+= enemy_speed
        frame+= 1
    else:
        pass
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if isSitted: screen.blit(dino_sit_death, (dino_x, dino_y))
        else: screen.blit(dino_death, (dino_x, dino_y))
        screen.blit(gamovr, (SCREEN_WIDTH//2 - gamovr.get_width() / 2, 200))
        screen.blit(rest, (SCREEN_WIDTH//2 - rest.get_width() / 2, 250))
        if (((SCREEN_WIDTH//2) - (rest.get_width() / 2) < mouse[0] < (SCREEN_WIDTH//2) + (rest.get_width() / 2)) and 250 < mouse[1] < 250 + rest.get_height()) and click[0]:
            cactus_type = 0
            ground_x = 0
            ground_y = SCREEN_HEIGHT - 80 - ground_img.get_height()
            ground = ground_y + random.randint(16, 32)
            tmp_ground_x = SCREEN_WIDTH * 2
            dino_width = 88
            dino_height = 94
            dino_x = SCREEN_WIDTH // 10
            dino_y = ground - dino_height
            dino_prev_y = 0
            hold_in_space = 0
            jump_force = 128
            isGround = True
            isSitted = False
            g = 7
            enemy_width = 34
            enemy_height = 70
            enemy_x = SCREEN_WIDTH
            enemy_y = ground - enemy_height
            enemy_speed = 3.5
            enemy_surf = pygame.Surface((enemy_width, enemy_height), pygame.SRCALPHA)
            score = 0
            frame = 0
            GameOver = False
        """
    pygame.display.flip()
    pygame.display.set_caption(str(fps))
    fps.tick(60)