# animation creator
import numpy as np


class AnimationCreator:
    def __init__(self, num_leds):
        self.num_leds = num_leds
        colors = 3
        shape = (1, self.num_leds, colors)
        self.animation_sequence = np.zeros(shape).astype(np.uint8)
        self.empty_line = np.zeros(shape).astype(np.uint8)
        self.animation_row_pointers = np.zeros(num_leds).astype(np.uint32)
        self.row_cnt = 1
        self.fps = 30
        




    #create animation_sequence
    #



    def set_light(self, led_idx, color):
        self.set_led_in_seq(led_idx, color)

    def fade_light(self, led_idx, end_color, dur):
        pass

    def turn_off_led(self, led_idx):
        self.set_led_in_seq(led_idx, [0,0,0])

    def turn_off_all_leds(self):
        for led_idx in range(self.num_leds):
            self.turn_off_led(led_idx)

    def wait(self, led_idx, dur):
        row = self.animation_row_pointers[led_idx]
        last_row = row - 1
        last_color = self.animation_sequence[last_row][led_idx]
        time_steps = int(round(dur*self.fps, 0))
        for i in range(time_steps):
            self.set_led_in_seq(led_idx, last_color)

    def wait_for_all_leds(self):
        pass

    def get_sequence(self):
        return self.animation_sequence

    def pattern_idx2strip_idx(self):
        pass

    def set_led_in_seq(self, led_idx, color):
        row = self.animation_row_pointers[led_idx]
        if row > self.row_cnt-1:
            self.add_empty_line()
        self.animation_sequence[row][led_idx] = color
        self.animation_row_pointers[led_idx] += 1

    def add_empty_line(self):
        self.animation_sequence = np.vstack((self.animation_sequence, 
                                            self.empty_line))
        self.row_cnt += 1
        
    def print_animation(self):
        print(self.animation_sequence)