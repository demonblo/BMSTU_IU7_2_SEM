import pygame
from math import*
pygame.init()
window = pygame.display.set_mode((900, 600))

Coordinates_of_dragon = [[100, 370], [90, 360], [87, 350], [94, 355], [80, 330], 
[77, 290], [84, 270], [100, 250], [140, 220], 
[200, 200], [193, 175], [170, 154], [150, 146], 
[110, 153], [94, 160], [83, 170], [40, 250], [23, 190],  [20, 150], [40, 80], 
[60, 50], [90, 19], [110, 12], [130, 10], 
[160, 20], [180, 40], [200, 60], [240, 140], [243, 190], [255, 180], [275, 173], 
[285, 173], [310, 190], [325, 215], [320, 175], [355, 215], 
[357, 221], [359, 227], [371, 260], [368, 263], [358, 265], [330, 235], [325, 237], 
[321, 243],
[337, 270], [330, 275], [307, 255], [300, 245], [300, 225], [285, 210], [278, 227], 
[270, 237], [265, 256], [240, 285], [220, 290], [210, 285], [190, 280], [175, 285], 
[166, 292], [158, 305], [175, 326], [179, 339], [157, 353], [155, 358], [154, 361], 
[165, 375], [179, 370], [183, 373], [185, 375], [186, 378], [187, 379], [190, 383], 
[198, 395], [185, 393], [173, 387],
[160, 394], [153, 397], [148, 390], [146, 386], [135, 368], [128, 340], [139, 330], 
[125, 305], [105, 295], [98, 305], [101, 325], [102, 335], [101, 345], 
[102, 340], [103, 350], [106, 345], [106, 355], [105, 360]]

Coordinates_of_dragon_copy = [[100, 370], [90, 360], [87, 350], [94, 355], [80, 330], 
[77, 290], [84, 270], [100, 250], [140, 220], 
[200, 200], [193, 175], [170, 154], [150, 146], 
[110, 153], [94, 160], [83, 170], [40, 250], [23, 190],  [20, 150], [40, 80], 
[60, 50], [90, 19], [110, 12], [130, 10], 
[160, 20], [180, 40], [200, 60], [240, 140], [243, 190], [255, 180], [275, 173], 
[285, 173], [310, 190], [325, 215], [320, 175], [355, 215], 
[357, 221], [359, 227], [371, 260], [368, 263], [358, 265], [330, 235], [325, 237], 
[321, 243],
[337, 270], [330, 275], [307, 255], [300, 245], [300, 225], [285, 210], [278, 227], 
[270, 237], [265, 256], [240, 285], [220, 290], [210, 285], [190, 280], [175, 285], 
[166, 292], [158, 305], [175, 326], [179, 339], [157, 353], [155, 358], [154, 361], 
[165, 375], [179, 370], [183, 373], [185, 375], [186, 378], [187, 379], [190, 383], 
[198, 395], [185, 393], [173, 387],
[160, 394], [153, 397], [148, 390], [146, 386], [135, 368], [128, 340], [139, 330], 
[125, 305], [105, 295], [98, 305], [101, 325], [102, 335], [101, 345], 
[102, 340], [103, 350], [106, 345], [106, 355], [105, 360]]

Coordinates_of_the_first_fireball = [370, 235]
Coordinates_of_the_first_fireball_copy = [370, 235]
Coordinates_of_the_second_fireball = [470, 235]
Coordinates_of_the_second_fireball_copy = [470, 235]
Coordinates_of_eye = [350, 230]
Coordinates_of_human_first = [[600, 515], [605, 500], [610, 515], [605, 500], [605, 480], [600, 495], [605, 480], [610, 495]]
Coordinates_of_head_first = [605, 475]
Coordinates_of_human_second = [[500, 545], [505, 530], [510, 545], [505, 530], [505, 510], [500, 525], [505, 510], [510, 525]]
Coordinates_of_head_second = [505, 505]
Coordinates_of_human_third = [[680, 585], [685, 570], [690, 585], [685, 570], [685, 540], [680, 565], [685, 540], [690, 565]]
Coordinates_of_head_third = [685, 533]
key_first = 0
key_second = 0
key_third = 0
for i in range(len(Coordinates_of_dragon_copy)):
	Coordinates_of_dragon_copy[i][0] -= 360

pygame.display.set_caption("Viseryon")

Dragons_main_color = (70, 130, 180)
Black = (0, 0, 0)
Background_color = (224, 255, 255)
Earth_color = (0, 139, 139,)
Main_fire_color = (255, 69, 0)
Second_fire_color = (255, 140, 0)
xp = 180
yp = 220
run = True
clock = pygame.time.Clock()

def rotate(x0, y0, xp, yp, angle):
    xq = xp + (x0 - xp) * cos(angle) + (y0 - yp) * sin(angle)
    yq = yp + (y0 - yp) * cos(angle) - (x0 - xp) * sin(angle)
 
    return xq, yq

while run:
    for kek in pygame.event.get():
        if kek.type == pygame.QUIT:
            run = False
    
    clock.tick(60)
    window.fill(Background_color)

    
    pygame.draw.rect(window, Earth_color, (0, 500, 900, 600))
    pygame.draw.polygon(window, Dragons_main_color, Coordinates_of_dragon)
    pygame.draw.aalines(window, Dragons_main_color, True, Coordinates_of_dragon)
    pygame.draw.circle(window, Black, Coordinates_of_eye, 5)
    pygame.draw.circle(window, Main_fire_color, Coordinates_of_eye, 3)
    pygame.draw.aalines(window, Black, False, Coordinates_of_human_first)
    pygame.draw.circle(window, Black, Coordinates_of_head_first, 5)
    pygame.draw.aalines(window, Black, False, Coordinates_of_human_second)
    pygame.draw.circle(window, Black, Coordinates_of_head_second, 5)
    pygame.draw.aalines(window, Black, False, Coordinates_of_human_third)
    pygame.draw.circle(window, Black, Coordinates_of_head_third, 10)

    if key_first:
        for i in range(len(Coordinates_of_human_first)):
            Coordinates_of_human_first[i][0] -= 9
        Coordinates_of_head_first[0] -= 9
    elif not key_first:
        for i in range(len(Coordinates_of_human_first)):
            Coordinates_of_human_first[i][0] += 9
        Coordinates_of_head_first[0] += 9
    if Coordinates_of_head_first[0] > 800 and not key_first:
        key_first = 1
    elif Coordinates_of_head_first[0] < 450 and key_first:
        key_first = 0

    if key_second:
        for i in range(len(Coordinates_of_human_second)):
            Coordinates_of_human_second[i][0] -= 9
        Coordinates_of_head_second[0] -= 9
    elif not key_second:
        for i in range(len(Coordinates_of_human_second)):
            Coordinates_of_human_second[i][0] += 9
        Coordinates_of_head_second[0] += 9
    if Coordinates_of_head_second[0] > 600 and not key_second:
        key_second = 1
    elif Coordinates_of_head_second[0] < 370 and key_second:
        key_second = 0

    if key_third:
        for i in range(len(Coordinates_of_human_third)):
            Coordinates_of_human_third[i][0] -= 9
        Coordinates_of_head_third[0] -= 9
    elif not key_third:
        for i in range(len(Coordinates_of_human_third)):
            Coordinates_of_human_third[i][0] += 9
        Coordinates_of_head_third[0] += 9
    if Coordinates_of_head_third[0] > 890 and not key_third:
        key_third = 1
    elif Coordinates_of_head_third[0] < 600 and key_third:
        key_third = 0

    Coordinates_of_eye[0], Coordinates_of_eye[1] = rotate(Coordinates_of_eye[0], Coordinates_of_eye[1], xp, yp, 0.1)
    Coordinates_of_eye[0] = int(Coordinates_of_eye[0])
    Coordinates_of_eye[1] = int(Coordinates_of_eye[1])
    Coordinates_of_eye[0] += 7

    for i in range(len(Coordinates_of_dragon)):
        Coordinates_of_dragon[i][0], Coordinates_of_dragon[i][1] = rotate(Coordinates_of_dragon[i][0], Coordinates_of_dragon[i][1], xp, yp, 2)
        Coordinates_of_dragon[i][0] += 7
    xp += 7
    

    if Coordinates_of_dragon[45][0] >= 370 and Coordinates_of_the_first_fireball[1] < 510:
        pygame.draw.circle(window, Main_fire_color, Coordinates_of_the_first_fireball, 20)
        pygame.draw.circle(window, Second_fire_color, Coordinates_of_the_first_fireball, 16)
        Coordinates_of_the_first_fireball[0] += 6
        Coordinates_of_the_first_fireball[1] += 6

    if Coordinates_of_dragon[45][0] >= 470 and Coordinates_of_the_second_fireball[1] < 580:
        pygame.draw.circle(window, Main_fire_color, Coordinates_of_the_second_fireball, 20)
        pygame.draw.circle(window, Second_fire_color, Coordinates_of_the_second_fireball, 16)
        Coordinates_of_the_second_fireball[0] += 4
        Coordinates_of_the_second_fireball[1] += 9

    pygame.display.update()

    if Coordinates_of_dragon[15][0] > 900:
        xp = -200
        Coordinates_of_eye = [-10, 230] 
        for i in range(0, 2):
            Coordinates_of_the_first_fireball[i] = Coordinates_of_the_first_fireball_copy[i]
            

        for i in range(0, 2):
            Coordinates_of_the_second_fireball[i] = Coordinates_of_the_second_fireball_copy[i]

        for i in range(len(Coordinates_of_dragon_copy)):
            Coordinates_of_dragon[i][0] = Coordinates_of_dragon_copy[i][0]
            Coordinates_of_dragon[i][1] = Coordinates_of_dragon_copy[i][1]

pygame.quit()
