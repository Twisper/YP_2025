import pygame
from pygame.draw import *
import math as m

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 800))
rect(screen, (255,255,255), (0, 0, 1000, 800))
rect(screen, (230,230,230), (0, 0, 1000, 400))

def ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))

def igloo(x,y,r):
    arc(screen, (230, 230, 230), (200*r+x, 300*r+y, 400*r, 300*r), 0, m.pi, 10000)
    arc(screen, (0, 0, 0), (200 * r + x, 300 * r + y, 400 * r, 300 * r), 0, m.pi, 2)
    #Горизонтальные линии
    line(screen, (0, 0, 0), (200*r+x, 450*r+y), (600*r+x, 450*r+y), 1)
    line(screen, (0, 0, 0), (208 * r + x, 410 * r + y), (592 * r + x, 410 * r + y), 1)
    line(screen, (0, 0, 0), (230 * r + x, 370 * r + y), (570 * r + x, 370 * r + y), 1)
    line(screen, (0, 0, 0), (280 * r + x, 330 * r + y), (520 * r + x, 330 * r + y), 1)
    #Блоки иглу
    line(screen, (0, 0, 0), (220 * r + x, 450 * r + y), (230 * r + x, 410 * r + y), 1)
    line(screen, (0, 0, 0), (316 * r + x, 450 * r + y), (328 * r + x, 410 * r + y), 1)
    line(screen, (0, 0, 0), (444 * r + x, 450 * r + y), (438 * r + x, 410 * r + y), 1)
    line(screen, (0, 0, 0), (520 * r + x, 450 * r + y), (509 * r + x, 410 * r + y), 1)
    line(screen, (0, 0, 0), (590 * r + x, 450 * r + y), (580 * r + x, 410 * r + y), 1)

    line(screen, (0, 0, 0), (241 * r + x, 410 * r + y), (254 * r + x, 370 * r + y), 1)
    line(screen, (0, 0, 0), (322 * r + x, 410 * r + y), (345 * r + x, 370 * r + y), 1)
    line(screen, (0, 0, 0), (425 * r + x, 410 * r + y), (408 * r + x, 370 * r + y), 1)
    line(screen, (0, 0, 0), (530 * r + x, 410 * r + y), (490 * r + x, 370 * r + y), 1)

    line(screen, (0, 0, 0), (290 * r + x, 370 * r + y), (310 * r + x, 330 * r + y), 1)
    line(screen, (0, 0, 0), (390 * r + x, 370 * r + y), (379 * r + x, 330 * r + y), 1)
    line(screen, (0, 0, 0), (500 * r + x, 370 * r + y), (488 * r + x, 330 * r + y), 1)

    line(screen, (0, 0, 0), (370 * r + x, 330 * r + y), (400 * r + x, 300 * r + y), 1)

def eskimos(x, y, r):
    circle(screen, (226, 222, 219), (850*r+x, 450*r+y), 80)
    circle(screen, (169, 158, 148), (850*r+x, 450*r+y), 60)
    circle(screen, (230, 199, 177), (850 * r + x, 455 * r + y), 40)
    arc(screen, (140, 105, 83), (750 * r + x, 500 * r + y, 200 * r, 200 * r), 0, m.pi, 100000)
    line(screen, (0, 0, 0), (825 * r + x, 430 * r + y), (840 * r + x, 435 * r + y), 1)
    line(screen, (0, 0, 0), (875 * r + x, 430 * r + y), (860 * r + x, 435 * r + y), 1)
    line(screen, (0, 0, 0), (825 * r + x, 470 * r + y), (840 * r + x, 465 * r + y), 1)
    line(screen, (0, 0, 0), (840 * r + x, 465 * r + y), (860 * r + x, 465 * r + y), 1)
    line(screen, (0, 0, 0), (860 * r + x, 465 * r + y), (875 * r + x, 470 * r + y), 1)
    ellipse_angle(screen, (140, 105, 83), (710 * r + x, 520 * r + y, 100 * r, 25 * r), -20)
    ellipse_angle(screen, (140, 105, 83), (890 * r + x, 520 * r + y, 100 * r, 25 * r), 20)
    ellipse_angle(screen, (140, 105, 83), (760 * r + x, 590 * r + y, 100 * r, 40 * r), 90)
    ellipse_angle(screen, (140, 105, 83), (840 * r + x, 590 * r + y, 100 * r, 40 * r), 90)
    ellipse_angle(screen, (140, 105, 83), (770 * r + x, 635 * r + y, 50 * r, 30 * r), 0)
    ellipse_angle(screen, (140, 105, 83), (880 * r + x, 635 * r + y, 50 * r, 30 * r), 0)
    polygon(screen, (77, 53, 12), [(750 * r + x, 600 * r + y), (750 * r + x, 620 * r + y), (950 * r + x, 620 * r + y),
                                   (950 * r + x, 600 * r + y)])
    polygon(screen, (77, 53, 12), [(825 * r + x, 600 * r + y), (875 * r + x, 600 * r + y), (875 * r + x, 500 * r + y),
                                   (825 * r + x, 500 * r + y)])
    line(screen, (0, 0, 0), (720 * r + x, 450 * r + y), (740 * r + x, 660 * r + y), 3)

def kot(x, y, r):
    ellipse(screen, (220, 220, 220), (200 * r + x, 600 * r + y, 200 * r, 30 * r))
    ellipse(screen, (220, 220, 220), (190 * r + x, 580 * r + y, 60 * r, 30 * r))
    ellipse_angle(screen, (220, 220, 220), (375 * r + x, 575 * r + y, 80 * r, 20 * r), 45)
    ellipse_angle(screen, (220, 220, 220), (375 * r + x, 630 * r + y, 60 * r, 16 * r), -45)
    ellipse_angle(screen, (220, 220, 220), (350 * r + x, 630 * r + y, 60 * r, 16 * r), -45)
    ellipse_angle(screen, (220, 220, 220), (170 * r + x, 615 * r + y, 80 * r, 16 * r), 30)
    ellipse_angle(screen, (220, 220, 220), (200 * r + x, 625 * r + y, 80 * r, 16 * r), 37)
    ellipse_angle(screen, (255, 255, 255), (192 * r + x, 585 * r + y, 10 * r, 10 * r), 25)
    ellipse_angle(screen, (255, 255, 255), (210 * r + x, 585 * r + y, 10 * r, 10 * r), 25)
    ellipse_angle(screen, (0, 0, 0), (198 * r + x, 588 * r + y, 5 * r, 5 * r), 25)
    ellipse_angle(screen, (0, 0, 0), (218 * r + x, 588 * r + y, 5 * r, 5 * r), 25)
    ellipse_angle(screen, (0, 0, 0), (198 * r + x, 598 * r + y, 3 * r, 3 * r), 25)
    polygon(screen, (220, 220, 220),
            [(205 * r + x, 585 * r + y), (212 * r + x, 570 * r + y), (219 * r + x, 580 * r + y),
             (205 * r + x, 585 * r + y)])
    polygon(screen, (220, 220, 220),
            [(225 * r + x, 585 * r + y), (232 * r + x, 570 * r + y), (242 * r + x, 590 * r + y),
             (225 * r + x, 585 * r + y)])
    ellipse_angle(screen, (163, 153, 196), (165 * r + x, 605 * r + y, 75 * r, 15 * r), -25)
    polygon(screen, (163, 153, 196),
            [(225 * r + x, 620 * r + y), (240 * r + x, 635 * r + y), (245 * r + x, 625 * r + y),
             (225 * r + x, 620 * r + y)])
    circle(screen, (255, 255, 255), (175 * r + x, 599 * r + y), 5 * r)
    circle(screen, (0, 0, 0), (175 * r + x, 599 * r + y), 5 * r, 1)
    circle(screen, (0, 0, 0), (175 * r + x, 599 * r + y), 2 * r)

igloo(400, 200, 0.5)
igloo(0, 200, 0.5)
igloo(0, 50, 1)
igloo(400, 300, 0.5)
igloo(0, 300, 0.5)

eskimos(0, 0, 1)
eskimos(75, 300, 0.5)
eskimos(150, 400, 0.5)
eskimos(275, 450, 0.5)

kot(0, 300, 0.5)
kot(0, 100, 1)
kot(200, 300, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()