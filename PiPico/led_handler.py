import neopixel2
import machine

class led_handler:
    
    def __init__(self, pin, num_of_leds):
        self.neopixel_leds = neopixel2.NeoPixel(machine.Pin(pin), num_of_leds)
        self.num_of_leds = num_of_leds
        
    def set_leds_color(self, idx, color):
        self.neopixel_leds[idx] = color
    
    def light_leds(self):
        self.neopixel_leds.write()
    
    def light_all_leds(self, color):
        for idx in range(self.num_of_leds):
            self.set_leds_color(idx, color)
        self.light_leds()
