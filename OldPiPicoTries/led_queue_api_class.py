import neopixel2
import machine

#led_queue_api(num_of_leds)

class led_queue_api:
    
    
    def __init__(self, pin, num_of_leds):
        self.neopixel_leds = neopixel2.NeoPixel(machine.Pin(pin), num_of_leds)

        self.led_list = [None] *num_of_leds
        for i in range(num_of_leds):
            self.led_list[i] = {"cur_color": [0,0,0],
                          "next_color": [[0,0,0]],
                          "dur": [1]}

    def run_nxt_animation_step(self):
        
        for i, led in enumerate(self.led_list):
            #print(led["next_color"])
            #calc difference for color to reach
            color_difference = [element1 - element2 for (element1, element2) in zip(led["next_color"][0], led["cur_color"])]
            #divide difference by steps
            color_difference_step = [round(x / led["dur"][0]) for x in color_difference]
            #add step difference to cur_color
            led["cur_color"] = [element1 + element2 for (element1, element2) in zip(led["cur_color"], color_difference_step)]
            #color led
            self.neopixel_leds[i] = led["cur_color"]
            #lower led
            led["dur"][0] = led["dur"][0] - 1
            if led["dur"][0] <= 0:
                if len(led["dur"]) == 1:
                    led["dur"][0] = 1
                else:
                    led["next_color"].pop(0)
                    led["dur"].pop(0)
        # lower dur
        # gegebenenfalls pop entry

    
    def add_animation(self, led_idx, color, duration):
        # todo: add check if input has right format
        self.led_list[led_idx]["next_color"].append(color)
        
        self.led_list[led_idx]["dur"].append(duration)
    
    def par_all_led_timings(self):
        pass
    
    def write_leds(self):
        self.neopixel_leds.write()


'''
led_animation.add_animation(led_idx=0, color=[10,10,10], duration=2)
#print(led_animation.led_list[0]["cur_color"])

print(led_animation.led_list)

led_animation.run_nxt_animation_step()

print(led_animation.led_list)
led_animation.run_nxt_animation_step()

print(led_animation.led_list)
led_animation.run_nxt_animation_step()

print(led_animation.led_list)

#led_animation.run_nxt_animation_step()
'''

'''
num_of_leds = 100
led_animation = led_queue_api(4, num_of_leds)


for i in range(num_of_leds):
    led_animation.add_animation(i, [255, 0, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 255, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 0, 255], 100)

from time import sleep
for i in range(500):
    led_animation.run_nxt_animation_step()
    led_animation.write_leds()
    sleep(0.1)
    
print("done")
'''