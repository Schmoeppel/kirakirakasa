import pygame
import numpy as np
from animation_creator_class import AnimationCreator
from animation_class import Animation
import random

fps = 20
speed = 1.0
start_time = 0.0
file_name = "animation_12"
led_matrix = np.array([ [16, 51, 84, 119, 17, 50, 85, 118],
                        [15, 52, 83, 120, 18, 49, 86, 117],
                        [14, 53, 82, 121, 19, 48, 87, 116],
                        [13, 54, 81, 122, 20, 47, 88, 115],
                        [12, 55, 80, 123, 21, 46, 89, 114],
                        [11, 56, 79, 124, 22, 45, 90, 113],
                        [10, 57, 78, 125, 23, 44, 91, 112],
                        [9, 58, 77, 126, 24, 43, 92, 111],
                        [8, 59, 76, 127, 25, 42, 93, 110],
                        [7, 60, 75, 128, 26, 41, 94, 109],
                        [6, 61, 74, 129, 27, 40, 95, 108],
                        [5, 62, 73, 130, 28, 39, 96, 107],
                        [4, 63, 72, 131, 29, 38, 97, 106], 
                        [3, 64, 71, 132, 30, 37, 98, 105],
                        [2, 65, 70, 133, 31, 36, 99, 104],
                        [1, 66, 69, 134, 32, 35, 100, 103],
                        [0, 67, 68, 135, 33, 34, 101, 102]])

num_leds = led_matrix.size

pygame.init()

animation_creator = AnimationCreator(num_leds, fps, speed)


def random_color():
    color_choose = random.randint(0,3)
    if color_choose == 0:
        color = [100, 100, 255]
    if color_choose == 1:
        color = [50, 10, 255]
    if color_choose == 2:
        color = [10, 255, 10]
    if color_choose == 3:
        color = [255, 255, 100]
    return color

def rainbow_color(i):
    f = (i / 255.0)
    r = int(abs(f*255.0-255.0))
    g = int(abs(f*255.0-170.0))
    b = int(abs(f*255.0-85.0))
    return [r, g, b]

def rainbow_color2(i):
    x = (i / 255.0)
    r = int(255/(1+3*x**2)) + int(255/(1+200*(x-1)**2))
    g = int(255*4*(-x**2+x))
    b = int(255/(1+3*(x-1)**2))

    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)

    return [r, g, b]

total_rows = 17
total_columns = 8
highest_row = total_rows - 1
highest_column = total_columns - 1

#################
# Create animations here.

animation_creator.set_light(5, [0, 255, 0])

for column in range(total_columns):
    animation_creator.fade_light(led_matrix[:,column], [255,0,0], 1)
    animation_creator.wait_for_all_leds()

for row in range(total_rows):
    animation_creator.fade_light(led_matrix[row,:], [0,0,255], 0.5)
    animation_creator.wait_for_all_leds()


#################


animation_creator.wait_for_all_leds()

#animation_creator.print_animation()


animation = Animation(led_matrix, animation_creator.fps)
animation.set_sequence(animation_creator.get_sequence())

#animation.create_txt(file_name)
animation.create_binary(file_name)

#animation.create_square_layout(spacing=17, led_radius=4)
animation.create_circular_layout(spacing=17, led_radius=4)
animation.run_preview(start_time=start_time)

################################
# Example animations are commented out

'''
# turn off and stay off (animation_0)
animation_creator.fade_light(led_matrix[:, :], [0,0,0], 2)
animation_creator.wait_for_all_leds()
'''

'''# fade through columns
animation_creator.fade_light(led_matrix[:, 7], [0,0,0], 2)
animation_creator.fade_light(led_matrix[:, 0], [10,0,200], 2)
animation_creator.wait_for_all_leds()

for i in range(7):
    animation_creator.fade_light(led_matrix[:, i], [0,0,0], 2)
    animation_creator.fade_light(led_matrix[:, i+1], [0,0,200], 2)
    animation_creator.wait_for_all_leds()

animation_creator.wait_for_all_leds()'''


'''
# fade through all rows
animation_creator.fade_light(led_matrix[0, :], [10,0,200], 2)

for i in range(16):
    animation_creator.fade_light(led_matrix[i, :], [0,0,0], 2)
    animation_creator.fade_light(led_matrix[i+1, :], [0,0,200], 2)

    animation_creator.fade_light(led_matrix[(i+8)%16, :], [0,0,0], 2)
    animation_creator.fade_light(led_matrix[(i+9)%16, :], [0,0,200], 2)

    animation_creator.wait_for_all_leds()
animation_creator.fade_light(led_matrix[16, :], [0,0,0], 2)

animation_creator.wait_for_all_leds()
'''

'''
# Magma
for i in range(20):
    for idx in range(num_leds):
        dur = random.uniform(0.5, 2.0)
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        animation_creator.fade_light(idx, [red, 0*green, 0*blue], dur)
animation_creator.wait_for_all_leds()
'''

'''
# wave through kasa
rows = len(led_matrix)
for i in range(5):
    for i in range(rows-1, -1, -1):
        animation_creator.fade_light(led_matrix[i, 5:], [0,200,0], 0.5)
        animation_creator.wait_for_all_leds()
    animation_creator.fade_light(led_matrix[:, 0], [0,200,0], 0.5)
    animation_creator.fade_light(led_matrix[:, 4], [0,200,0], 0.5)
    animation_creator.wait_for_all_leds()
    for i in range(rows):
        animation_creator.fade_light(led_matrix[i, :4], [0,200,0], 0.5)
        animation_creator.wait_for_all_leds()

    for i in range(rows-1, -1, -1):
        animation_creator.fade_light(led_matrix[i, 5:], [200,0,0], 0.5)
        animation_creator.wait_for_all_leds()
    animation_creator.fade_light(led_matrix[:, 0], [200,0,0], 0.5)
    animation_creator.fade_light(led_matrix[:, 4], [200,0,0], 0.5)
    animation_creator.wait_for_all_leds()
    for i in range(rows):
        animation_creator.fade_light(led_matrix[i, :4], [200,0,0], 0.5)
        animation_creator.wait_for_all_leds()

animation_creator.wait_for_all_leds()
'''

'''
# double waves
rows = len(led_matrix)
for i in range(5):
    for i in range(rows-1, -1, -1):
        animation_creator.fade_light(led_matrix[i, 5:], [0,200,0], 0.5)
        animation_creator.fade_light(led_matrix[rows-1-i, 0:5], [200,0,0], 0.5)
        animation_creator.wait_for_all_leds()
    #animation_creator.fade_light(led_matrix[:, 0], [0,200,0], 0.5)
    #animation_creator.fade_light(led_matrix[:, 4], [0,200,0], 0.5)
    animation_creator.wait_for_all_leds()
    for i in range(rows):
        animation_creator.fade_light(led_matrix[i, :5], [0,200,0], 0.5)
        animation_creator.fade_light(led_matrix[rows-1-i, 5:], [200,0,0], 0.5)
        animation_creator.wait_for_all_leds()

    #animation_creator.fade_light(led_matrix[:, 0], [200,0,0], 0.5)
    #animation_creator.fade_light(led_matrix[:, 4], [200,0,0], 0.5)
    animation_creator.wait_for_all_leds()

animation_creator.wait_for_all_leds()
'''


'''
# rainbow waves
for i in range(17-2):
    animation_creator.fade_light(led_matrix[i, :], rainbow_color2(i), 0.1)
    animation_creator.fade_light(led_matrix[i+1, :], rainbow_color2(i), 0.1)
    animation_creator.fade_light(led_matrix[i+2, :], rainbow_color2(i), 0.1)

    animation_creator.fade_light(led_matrix[(i+7)%17, :], rainbow_color2(i), 0.1)
    animation_creator.fade_light(led_matrix[(i+8)%17, :], rainbow_color2(i), 0.1)
    animation_creator.fade_light(led_matrix[(i+9)%17, :], rainbow_color2(i), 0.1)



    animation_creator.wait_for_all_leds()
    animation_creator.fade_light(led_matrix[i, :], [0,0,0], 0.1)
    animation_creator.fade_light(led_matrix[(i+7)%17, :], [0,0,0], 0.1)

animation_creator.fade_light(led_matrix[15, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[16, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[0, :], rainbow_color2(14), 0.1)

animation_creator.fade_light(led_matrix[5, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[6, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[7, :], rainbow_color2(14), 0.1)

animation_creator.wait_for_all_leds()
animation_creator.fade_light(led_matrix[15, :], [0,0,0], 0.1)
animation_creator.fade_light(led_matrix[5, :], [0,0,0], 0.1)

animation_creator.fade_light(led_matrix[16, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[0, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[1, :], rainbow_color2(14), 0.1)

animation_creator.fade_light(led_matrix[6, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[7, :], rainbow_color2(14), 0.1)
animation_creator.fade_light(led_matrix[8, :], rainbow_color2(14), 0.1)

animation_creator.wait_for_all_leds()
animation_creator.fade_light(led_matrix[16, :], [0,0,0], 0.1)
animation_creator.fade_light(led_matrix[6, :], [0,0,0], 0.1)'''



'''# static rainbow
total_steps = 50
for step in range(total_steps):
    color_shift = 255/total_steps*5
    color_int = (color_shift*step)%255
    for column in range(total_columns):
        animation_creator.fade_light(led_matrix[:, column], rainbow_color2(color_int), 0.2)
'''

'''
# column rainbow

total_steps = 50
for step in range(total_steps):
    color_shift = 255/total_steps*5
    for column in range(total_columns):
        color_int = (color_shift*step + (255/total_columns*column))%255
        animation_creator.fade_light(led_matrix[:, column], rainbow_color2(color_int), 0.2)

animation_creator.wait_for_all_leds()
'''

'''
# row rainbow
total_steps = 10
for step in range(total_steps):
    color_shift = 255/total_steps*1
    for row in range(total_rows):
        color_int = (color_shift*step + (255/total_rows*row))%255
        animation_creator.fade_light(led_matrix[row, :], rainbow_color2(color_int), 0.2)

animation_creator.wait_for_all_leds()
'''