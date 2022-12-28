# animation creator

class AnimationCreator:
    def __init__(self, num_leds):
        self.num_leds = num_leds
        self.animation_sequence = 0
        self.animation_row_pointers = 0
        self.highest_pointer = 0
        self.fps = 30



    #create animation_sequence
    #function to automatically add line
    #function to set led in line of row_pointer
    #



    def set_light(self, led_idx, color):
        pass

    def fade_light(self, led_idx, end_color, dur):
        pass

    def turn_off_led(self, led_idx):
        pass

    def wait(self, led_idx, dur):
        pass

    def wait_for_all_leds(self):
        pass

    def get_sequence(self):
        pass

    def pattern_idx2strip_idx(self):
        pass

    def update_highest_pointer(self):
        pass
