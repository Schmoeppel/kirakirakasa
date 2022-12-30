import pygame
import numpy as np
from animation_creator_class import AnimationCreator
from animation_class import Animation
from matrix_handler import MatrixHandler

real_matrix = np.array([[1,2,3], 
                        [4,5,6]])

user_matrix = np.array([[1, 3, 5],
                        [2, 4, 6]])

leds = MatrixHandler(real_matrix, user_matrix)

leds.check_matrix_sizes()

pygame.init()

AnimationCreator = AnimationCreator(3)

AnimationCreator.set_led_in_seq(2, [1,2,3])

AnimationCreator.wait(2, 0.5)
#AnimationCreator.add_empty_line()
AnimationCreator.print_animation()

print(AnimationCreator.animation_sequence.shape)
print(AnimationCreator.animation_row_pointers)



# time_adjustment = pygame.time.get_ticks() - start_second*1000

# from sqlalchemy import true

'''
num_of_leds = 136

screenwidth = 1200
screenheight = 680

kasa_radius = int(300)

win = pygame.display.set_mode((screenwidth, screenheight))


def sin(deg):
    return np.sin(np.deg2rad(deg))

def cos(deg):
    return np.cos(np.deg2rad(deg))


pygame.display.set_caption("KiraKiraKasa Animation Simulator")

clock = pygame.time.Clock()
# clock.tick(27)

leds = [None]*num_of_leds

def create_leds(leds):
    x_center = int(screenwidth/2)
    y_center = int(screenheight/2)

    pos = np.array([int(x_center), int(y_center - kasa_radius)])
    dxy = np.array([0,kasa_radius*2/33])
    for i in range(34):
        leds[i] = LedCreator(pos.astype(int), i, win)
        pos = pos+dxy

    pos = np.array([x_center+sin(45)*int(kasa_radius),
                    y_center + cos(45)*int(kasa_radius)])
    dxy = np.array([-sin(45)*int(kasa_radius)*2/33,
                    -cos(45)*int(kasa_radius)*2/33
                    ])
    for i in range(34):
        leds[i+34*1] = LedCreator(pos.astype(int), i, win)
        pos = pos+dxy

    pos = np.array([int(x_center - kasa_radius), int(y_center)])
    dxy = np.array([kasa_radius*2/33, 0])
    for i in range(34):
        leds[i+34*2] = LedCreator(pos.astype(int), i, win)
        pos = pos+dxy

    pos = np.array([x_center+sin(45)*int(kasa_radius),
                    y_center - cos(45)*int(kasa_radius)])
    dxy = np.array([-sin(45)*int(kasa_radius)*2/33,
                    +cos(45)*int(kasa_radius)*2/33
                    ])
    for i in range(34):
        leds[i+34*3] = LedCreator(pos.astype(int), i, win)
        pos = pos+dxy

def draw_background():
    color = [10,10,10]
    position = [int(screenwidth/2), int(screenheight/2)]
    #radius = 300
    pygame.draw.circle(win, color, position, int(kasa_radius))

create_leds(leds)

draw_background()

pygame.display.update()


is_running = True


while is_running:
    for led in leds:
        led.draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        pass

    if keys[pygame.K_LEFT]:
        pass


pygame.quit()
print("pygame closed correclty")
'''