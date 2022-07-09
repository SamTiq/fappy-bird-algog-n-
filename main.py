import pygame
from bird import Bird
from colone import Colone
from math import *
from shapely.geometry import LineString


def intersect2Segments(tuple1, tuple2, tuple3, tuple4):
    s1 = LineString([tuple1, tuple2])
    s2 = LineString([tuple3, tuple4])

    if not s1.intersects(s2):
        return False
    try:
        solve = (s1.intersection(s2).x, s1.intersection(s2).y)
    except:
        solve = False
    return solve
    
def findPoint(tuple1, tuple2, c, b):
    colone_x = round(500*(c.x/10))
    segments = [[(colone_x, 0), (colone_x, c.trou)], [(colone_x, c.trou), (colone_x+50, c.trou)], [(colone_x, c.trou+100), (colone_x, 500)], [(colone_x, c.trou+100), (colone_x+50, c.trou+100)], [(0, 0), (500, 0)], [(500, 0), (500, 500)], [(0, 0), (500, 0)], [(0, 500), (500, 500)]]
    for element in segments:
        val = intersect2Segments(tuple1, tuple2, (element[0][0], element[0][1]), (element[1][0], element[1][1]))
        if val != False:
            pygame.draw.line(window_surface, (0, 0, 0), (100,  round(500*(b.y/10))), val)
            break

def AllLines(tuple1, c, b, nombre_angle):

    for i in range(nombre_angle//2):
        angle1 = (i * pi)/nombre_angle

        x1 = round(500*(b.y/10)) * tan(angle1) + 100
        x2 =  (500-(round(500*(b.y/10)))) * tan(angle1) + 100

        findPoint(tuple1, (x1, 0), c, b)
        findPoint(tuple1, (x2, 500), c, b)

    findPoint(tuple1, (500, tuple1[1]), c, b)

pygame.init()
window_surface=pygame.display.set_mode((500, 500))

old = pygame.time.get_ticks()
launched=True
b = Bird()
c = Colone()
point = 0

while launched:
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            launched=False

        elif event.type == pygame.MOUSEBUTTONUP:
            b.vitesse = -5


    time = (pygame.time.get_ticks()-old)/1000
    b.vitesse = b.vitesse+b.acceleration*time
    b.y = b.y+b.vitesse*time
    c.x = c.x-c.vitesse*time
    old = pygame.time.get_ticks()

    if c.x<-1:
        c = Colone()
        point += 1

    #Display
    window_surface.fill((0,0,255))
    c.rectUp = pygame.Rect((round(500*(c.x/10)), 0), (50, c.trou))
    c.rectDown = pygame.Rect((round(500*(c.x/10)), c.trou+c.taille_trou), (50, 500-c.trou-c.taille_trou))
    bird_rect = pygame.Rect((90, round(500*(b.y/10))-10), (20, 20))
    top = pygame.Rect((0, -10), (500, 10))
    bottom = pygame.Rect((0, 500), (500, 10))

    pygame.draw.rect(window_surface, (0,255,0), c.rectUp)
    pygame.draw.rect(window_surface, (0,255,0), c.rectDown)
    pygame.draw.rect(window_surface, (255,0,0), bird_rect)

    if(c.rectUp.colliderect(bird_rect) or c.rectDown.colliderect(bird_rect) or top.colliderect(bird_rect) or bottom.colliderect(bird_rect)):
        launched = False

    AllLines((100, round(500*(b.y/10))), c, b, 100)

    pygame.display.flip()

print(point)