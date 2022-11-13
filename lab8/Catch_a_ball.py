import pygame
from pygame.draw import *
from random import randint
pygame.init()

global score
score = 0
FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global x, y, r, color, speedx, speedy, lifetime, countertime

def new_ball():
    global x, y, r, color, speedx, speedy, lifetime, countertime
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    speedx = randint(-8, 8)
    speedy = randint(-8, 8)
    lifetime = randint(25, 100)
    countertime = 0
    circle(screen, color, (x, y), r)

def update_position():
    global x, y, r, speedx, speedy, countertime
    x += speedx
    y += speedy
    countertime += 1
    if (countertime == lifetime):
        new_ball()
    if (x + r > 1200):
        speedx = randint(-8, -1)
    elif (x - r < 0):
        speedx = randint(1, 8)
    elif (y - r < 0):
        speedy = randint(1, 8)
    elif (y + r > 900):
        speedy = randint(-8, -1)
    circle(screen, color, (x,y), r)

def click(event):
    if ((event.pos[0] - x)**2 + (event.pos[1] - y)**2) <= r**2:
        #print("ПОПАЛ!")
        add_score(5)
        return True
    else:
        #print("Не попал!")
        return False

def add_score(points):
    global score
    score += points
    print(score)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (click(event) == True):
                new_ball()
    screen.fill(BLACK)
    update_position()
    pygame.display.update()

pygame.quit()