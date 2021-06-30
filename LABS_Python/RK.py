import pygame
from math import*
pygame.init()
window = pygame.display.set_mode((900, 600))
run = True
clock = pygame.time.Clock()
White = (255, 255, 255)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)
r_nlo_1 = 30
r_nlo_2 = 63
r_nlo_3 = 103
counter = 25
Coordinates_of_the_nlo_1 = [405, 395]
Coordinates_of_the_nlo_0 = [350, 425, 103, 65]
Coordinates_of_the_nlo_0_copy = [353, 426, 100, 63]
Coordinates_of_the_krug = [125, 425]
Coordinates_of_the_roof = [[50, 300], [150, 250] , [250, 300]]
Coordinates_of_the_second_window = [[180, 360], [220, 360], [200, 310], [200, 360], [180, 360], [200, 310]]

while run:
    for kek in pygame.event.get():
        if kek.type == pygame.QUIT:
            run = False

    clock.tick(20)
    window.fill(White)


    pygame.draw.rect(window, Black, (0, 500, 900, 600))
    pygame.draw.rect(window, White, (1, 501, 898, 598))
    pygame.draw.rect(window, Black, (49, 301, 200, 200))
    pygame.draw.rect(window, White, (50, 300, 198, 198))
    pygame.draw.rect(window, Green, (210, 225, 30, 75))
    pygame.draw.circle(window, Black, Coordinates_of_the_krug, 50)
    pygame.draw.circle(window, White, Coordinates_of_the_krug, 49)
    pygame.draw.circle(window, Black, Coordinates_of_the_nlo_1, r_nlo_1 + 1)    
    pygame.draw.circle(window, White, Coordinates_of_the_nlo_1, r_nlo_1)
    pygame.draw.ellipse(window, Black, Coordinates_of_the_nlo_0)
    pygame.draw.ellipse(window, White, Coordinates_of_the_nlo_0_copy)
    
    pygame.draw.rect(window, Black, (75, 425, 50, 50))
    pygame.draw.rect(window, White, (76, 426, 48, 48))
    pygame.draw.rect(window, Black, (125, 425, 50, 50))
    pygame.draw.rect(window, White, (126, 426, 48, 48))
    pygame.draw.polygon(window, Yellow, Coordinates_of_the_roof)
    pygame.draw.aalines(window, Black, False, Coordinates_of_the_second_window)

    if r_nlo_1 > 2 :
        r_nlo_1 -= 1
    if r_nlo_2 > 2:
        r_nlo_2 -= 1
        Coordinates_of_the_nlo_0_copy[2] = r_nlo_2
        Coordinates_of_the_nlo_0[2] = r_nlo_2 + 2
    if r_nlo_3 > 2:
        r_nlo_3 -= 1
        Coordinates_of_the_nlo_0_copy[2] = r_nlo_3
        Coordinates_of_the_nlo_0[2] = r_nlo_3 + 7
    Coordinates_of_the_nlo_0[0] += 30
    Coordinates_of_the_nlo_0[1] -= 30
    Coordinates_of_the_nlo_0_copy[0] += 30
    Coordinates_of_the_nlo_0_copy[1] -= 30
    Coordinates_of_the_nlo_1[0] += 30
    Coordinates_of_the_nlo_1[1] = Coordinates_of_the_nlo_0[1] - counter - 5
    counter -= 1
    
    
    pygame.display.update()

pygame.quit()
