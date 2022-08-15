from venv import create
import pygame
import numpy as np

pygame.init()




# time_adjustment = pygame.time.get_ticks() - start_second*1000

#from sqlalchemy import true

num_of_leds = 136

screenwidth = 1200
screenheight = 680

kasa_radius = int(300)

win = pygame.display.set_mode((screenwidth, screenheight))

class LedCreator:
    def __init__(self, position, idx, win):
        self.position = position
        self.idx = idx
        self.win = win
        self.color = [100, 100, 100]
        self.radius = 4


    def add_animation(self, color, duration, win):
        pass

    def wait_for_all_animations():
        pass

    def draw(self):
        pygame.draw.circle(self.win, self.color, self.position, self.radius)


def draw_background():
    color = [10,10,10]
    position = [int(screenwidth/2), int(screenheight/2)]
    #radius = 300
    pygame.draw.circle(win, color, position, int(kasa_radius))


def sin(deg):
    return np.sin(np.deg2rad(deg))

def cos(deg):
    return np.cos(np.deg2rad(deg))


pygame.display.set_caption("KiraKiraKasa Animation Simulator")

clock = pygame.time.Clock()
#clock.tick(27)

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

create_leds(leds)

#led1 = LedCreator([100, 100], 0, win)

#leds[0].draw()
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
