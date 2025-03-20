import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255,255,255), (0, 0, 400, 400))
circle(screen, (252, 219, 3), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (0, 0, 0), (150, 175), 20, 1)
circle(screen, (0, 0, 0), (150, 175), 10)
circle(screen, (255, 0, 0), (250, 175), 16)
circle(screen, (0, 0, 0), (250, 175), 16, 1)
circle(screen, (0, 0, 0), (250, 175), 8)
rect(screen, (0, 0, 0), (150, 250, 100, 25))
polygon(screen, (0, 0, 0), [(180, 160), (100, 120), (105, 110), (185, 150)])
polygon(screen, (0, 0, 0), [(237, 149), (240, 158), (300, 132), (297, 123)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()