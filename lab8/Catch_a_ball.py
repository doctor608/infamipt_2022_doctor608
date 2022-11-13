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

x = [0]*2
y = [0]*2
r = [0]*2
color = [0]*2
speedx = [0]*2
speedy = [0]*2
lifetime = [0]*2
countertime = [0]*2

def new_ball(i):
    global x, y, r, color, speedx, speedy, lifetime, countertime
    x[i] = randint(100, 700)
    y[i] = randint(100, 500)
    r[i] = randint(30, 50)
    color[i] = COLORS[randint(0, 5)]
    speedx[i] = randint(-8, 8)
    speedy[i] = randint(-8, 8)
    lifetime[i] = randint(25, 100)
    countertime[i] = 0
    circle(screen, color[i], (x[i], y[i]), r[i])

def update_position(i):
    global x, y, r, speedx, speedy, countertime
    x[i] += speedx
    y[i] += speedy
    countertime[i] += 1
    if (countertime[i] == lifetime[i]):
        new_ball(i)
    if (x + r > 1200):
        speedx[i] = randint(-8, -1)
    elif (x - r < 0):
        speedx[i] = randint(1, 8)
    elif (y - r < 0):
        speedy[i] = randint(1, 8)
    elif (y + r > 900):
        speedy[i] = randint(-8, -1)
    circle(screen, color[i], (x[i],y[i]), r[i])

def click(event):
    if ((event.pos[0] - x[0])**2 + (event.pos[1] - y[0])**2) <= r[0]**2:
        add_score(5)
        return 0
    elif ((event.pos[0] - x[1])**2 + (event.pos[1] - y[1])**2) <= r[1]**2:
        add_score(5)
        return 1
    else:
        return False

def add_score(points):
    global score
    score += points
    print(score)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball(0)
new_ball(1)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (click(event) == 0):
                new_ball(0)
            elif (click(event) == 1):
                new_ball(1)
    screen.fill(BLACK)
    update_position(0)
    update_position(1)
    pygame.display.update()

pygame.quit()