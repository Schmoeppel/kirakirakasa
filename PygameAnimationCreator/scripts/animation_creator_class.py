# animation creator
import numpy as np


class AnimationCreator:
    def __init__(self, num_leds, fps=20, speed=1.0):
        self.num_leds = num_leds
        colors = 3
        shape = (1, self.num_leds, colors)
        self.animation_sequence = np.zeros(shape).astype(np.uint8)
        self.empty_line = np.zeros(shape).astype(np.uint8)
        self.animation_row_pointers = np.zeros(num_leds).astype(np.uint32)
        self.row_cnt = 1
        self.fps = fps
        self.speed = speed

    def set_light(self, led_idx, color):
        self._set_led_in_seq(led_idx, color)

    def fade_light(self, led_idx, end_color, dur):
        led_idx = self._idx2array(led_idx)
        time_steps = int(round(dur*self.fps/self.speed, 0))
        for idx in led_idx:
            cur_color = self.get_cur_color(idx)
            color_step = ((end_color - cur_color)/time_steps).astype(np.float)
            next_color = cur_color.astype(np.float)
            for step in range(time_steps):
                next_color = next_color + color_step
                self._set_led_in_seq(idx, next_color.astype(np.uint8))

    def turn_off_led(self, led_idx):
        self._set_led_in_seq(led_idx, [0,0,0])

    def turn_off_all_leds(self):
        for led_idx in range(self.num_leds):
            self.turn_off_led(led_idx)

    def wait(self, led_idx, dur):
        time_steps = int(round(dur*self.fps/self.speed, 0))
        led_idx = self._idx2array(led_idx)
        for idx in led_idx:
            cur_color = self.get_cur_color(idx)
            for i in range(time_steps):
                self._set_led_in_seq(idx, cur_color)
    
    def get_cur_color(self, idx):
        row = self.animation_row_pointers[idx]
        last_row = row - 1
        color = self.animation_sequence[last_row][idx]
        return color

    def wait_for_all_leds(self):
        max_pointer = np.max(self.animation_row_pointers)
        for led_idx in range(self.num_leds):
            if self.animation_row_pointers[led_idx] < max_pointer:
                time_steps = max_pointer - self.animation_row_pointers[led_idx]
                self.wait(led_idx, time_steps/self.fps*self.speed)

    def get_sequence(self):
        return self.animation_sequence

    def _set_led_in_seq(self, led_idx, color):
        led_idx = self._idx2array(led_idx)
        #color = self._color2array(color)
        
        
        #color = color.reshape(-1, color.shape[-1])

        for single_led in led_idx:
            row = self.animation_row_pointers[single_led]
            if row > self.row_cnt-1:
                self._add_empty_line()
            self.animation_sequence[row][single_led] = color
            self.animation_row_pointers[single_led] += 1

    def _idx2array(self, idx):
        if isinstance(idx, int):
            idx = np.array([idx])
        idx = idx.flatten()
        return idx

    #def _color2array(self, color):
    #    if color.ndim == 1:
    #        color = np.array([color])
    #    return color


    def _add_empty_line(self):
        self.animation_sequence = np.vstack((self.animation_sequence, 
                                            self.empty_line))
        self.row_cnt += 1
        
    def print_animation(self):
        print(self.animation_sequence)