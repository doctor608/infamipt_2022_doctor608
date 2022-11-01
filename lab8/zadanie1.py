import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
rect(screen, (0, 0, 0), (150, 225, 100, 20))
circle(screen, (255, 0, 0), (250, 150), 15)
circle(screen, (0, 0, 0), (250, 150), 8)
circle(screen, (255, 0, 0), (155, 150), 22)
circle(screen, (0, 0, 0), (155, 150), 13)
line(screen, (0, 0, 0), (185, 140), (120, 110), 10)
line(screen, (0, 0, 0), (225, 140), (300, 110), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
