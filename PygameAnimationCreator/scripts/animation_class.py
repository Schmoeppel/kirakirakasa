from led_creator_class import LedCreator
import pygame
import numpy as np
import struct
import math
import os
import time




class Animation:
    def __init__(self, user_matrix, fps):
        pygame.init()
        self.user_matrix = user_matrix
        self.leds = [None]*user_matrix.size
        self.fps = fps
        self.total_time = 0
        self.start_time = 0
        self.end_time = 0
        self.sequence = None
        self.max_step = 0
        self.screenwidth = 1200
        self.screenheight = 680
        self.win = pygame.display.set_mode((self.screenwidth, self.screenheight))
        
        self.kasa_radius = int(300)

    def set_sequence(self, sequence):
        self.sequence = sequence
        self.max_step = len(sequence)

    def create_binary(self, file_name):
        # Navigate to the parent folder of the current folder
        parent_folder = os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "/KiraKiraKasa/PygameAnimationCreator"
        with open(os.path.join(parent_folder, "animation_files/"+file_name+".txt"), 'wb') as f:
            for row in self.sequence:
                row = row.flatten()
                
                for val in row:
                    if val == 10: #
                        val = 11
                    packed_value = struct.pack('B', val)
                    f.write(packed_value)
                f.write(b'\n')


    def create_txt(self, file_name):
        with open(os.path.join(parent_folder, "animation_files/"+file_name+"text.txt"), "w") as f:
            for rows in self.sequence:
                for color in rows:
                    f.write(np.array2string(color) + "\t")
                f.write("\n")

    def run_preview(self, start_time=0):
        sequence_step = 0 + start_time*self.fps
        pygame.display.set_caption("KiraKiraKasa Animation Simulator")
        clock = pygame.time.Clock()
        

        self.draw_background()
        pygame.display.update()

        
        timer_start = time.time()

        is_running = True
        while is_running:
            clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
            

            self.read_sequence_step(sequence_step)
            self.draw_leds()
            self.print_time(timer_start, start_time)
            pygame.display.flip()
            sequence_step += 1


            if sequence_step >= self.max_step:
                is_running = False
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_SPACE]:
            #    pass
        
        pygame.quit()
        print("pygame closed correclty")
    
    def draw_background(self):
        color = [30,30,30]
        position = [int(self.screenwidth/2), int(self.screenheight/2)]
        #radius = 300
        pygame.draw.circle(self.win, color, position, int(self.kasa_radius))

    def read_sequence_step(self, sequence_step):
        for led in self.leds:
            next_color = self.sequence[int(sequence_step), led.idx]
            led.color = next_color
            


    

    def draw_leds(self):
        for led in self.leds:
            led.draw()

    def print_time(self, timer_start, start_time):
        text_color = (200,200,200)
        background_color = (10,10,10)
        font = pygame.font.Font(None, 36)
        elapsed_time = time.time() - timer_start + start_time
        elapsed_time_formatted = time.strftime("%M:%S", time.gmtime(elapsed_time))
        text = font.render(elapsed_time_formatted, True, text_color)
        text_width, text_height = font.size(elapsed_time_formatted)
        text_x = 100
        text_y = 100
        rect_width = text_width + 20
        rect_height = text_height + 20
        rect_x = text_x - 10
        rect_y = text_y - 10
        pygame.draw.rect(self.win, background_color, (rect_x, rect_y, rect_width, rect_height))
        self.win.blit(text, (text_x, text_y))

    def create_circular_layout(self, spacing=17, led_radius=4):
        row_elements = len(self.user_matrix[0])
        row_cnt = len(self.user_matrix)
        deg_between_columns = 45
        x_center = int(self.screenwidth/2)
        y_center = int(self.screenheight/2)
        x_start = x_center
        y_start = y_center

        i = 0
        for row in self.user_matrix:
            #x_pos = x_start
            y_start = y_start - spacing
            for c, idx in enumerate(row):
                x_pos = (x_start-x_center)*self.cos(deg_between_columns*c) - (y_start-y_center)*self.sin(deg_between_columns*c) + x_center
                y_pos = (x_start-x_center)*self.sin(deg_between_columns*c) + (y_start-y_center)*self.cos(deg_between_columns*c) + y_center
                
                
                pos = np.array([x_pos, y_pos]).astype(int)
                self.leds[i] = LedCreator(pos, idx, self.win, led_radius)
                i += 1


    def sin(self, deg):
        rad = math.radians(deg)
        return math.sin(rad)

    def cos(self, deg):
        rad = math.radians(deg)
        return math.cos(rad)

    def create_square_layout(self, spacing=17, led_radius=4):
        row_elements = len(self.user_matrix[0]) - 1
        row_cnt = len(self.user_matrix) - 1
        x_center = int(self.screenwidth/2)
        y_center = int(self.screenheight/2)
        x_start = x_center - row_elements/2 * spacing #- self.led_radius/2
        y_start = y_center - row_cnt/2 * spacing #- self.led_radius/2

        y_pos = y_start 
        i = 0
        for row in self.user_matrix:
            x_pos = x_start
            for idx in row:
                pos = np.array([x_pos, y_pos]).astype(int)
                self.leds[i] = LedCreator(pos, idx, self.win, led_radius)
                i += 1
                x_pos = x_pos + spacing
            y_pos = y_pos + spacing

        