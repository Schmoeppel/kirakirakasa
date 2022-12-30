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


    def set_light(self, led_idx, color):
        self._set_led_in_seq(led_idx, color)

    def fade_light(self, led_idx, end_color, dur):
        row = self.animation_row_pointers[led_idx]
        last_row = row - 1
        cur_color = self.animation_sequence[last_row][led_idx]
        time_steps = int(round(dur*self.fps, 0))
        color_step = ((end_color - cur_color)/time_steps).astype(np.float)
        #next_color = np.zeros(3).astype(np.float)
        next_color = cur_color.astype(np.float)
        
        for step in range(time_steps):
            next_color = next_color + color_step
            self._set_led_in_seq(led_idx, next_color.astype(np.uint8))

    def turn_off_led(self, led_idx):
        self._set_led_in_seq(led_idx, [0,0,0])

    def turn_off_all_leds(self):
        for led_idx in range(self.num_leds):
            self.turn_off_led(led_idx)

    def wait(self, led_idx, dur):
        row = self.animation_row_pointers[led_idx]
        last_row = row - 1
        cur_color = self.animation_sequence[last_row][led_idx]
        time_steps = int(round(dur*self.fps, 0))
        for i in range(time_steps):
            self._set_led_in_seq(led_idx, cur_color)

    def wait_for_all_leds(self):
        max_pointer = np.max(self.animation_row_pointers)
        for led_idx in range(self.num_leds):
            if self.animation_row_pointers[led_idx] < max_pointer:
                time_steps = max_pointer - self.animation_row_pointers[led_idx]
                self.wait(led_idx, time_steps/self.fps)

    def get_sequence(self):
        return self.animation_sequence

    def _set_led_in_seq(self, led_idx, color):
        if isinstance(led_idx, int):
            led_idx = np.array([led_idx])
        
        led_idx = led_idx.flatten()
        for single_led in led_idx:
            row = self.animation_row_pointers[single_led]
            if row > self.row_cnt-1:
                self._add_empty_line()
            self.animation_sequence[row][single_led] = color
            self.animation_row_pointers[single_led] += 1

    def _add_empty_line(self):
        self.animation_sequence = np.vstack((self.animation_sequence, 
                                            self.empty_line))
        self.row_cnt += 1
        
    def print_animation(self):
        print(self.animation_sequence)