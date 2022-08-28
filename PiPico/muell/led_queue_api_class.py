import neopixel2
import machine

from machine import Pin, SPI

#import os


#led_queue_api(num_of_leds)

class led_queue_api:
    
    
    def __init__(self, pin, num_of_leds):
        self.neopixel_leds = neopixel2.NeoPixel(machine.Pin(pin), num_of_leds)
        self.num_of_leds = num_of_leds
        #self.current_folder = "sd"
        self.max_lines = 4
        
        #self.led_list = [[[0]*4]*1]*num_of_leds
        #self.cur_led_light = [[0]*3]*num_of_leds
        
        self.cur_led_light = [None]*num_of_leds
        self.led_list = [None] *num_of_leds
        for i in range(num_of_leds):
            self.led_list[i] = [[0,0,0,0]]
            self.cur_led_light = [0,0,0]
        for n in range(self.max_lines):
            self.led_list[n].append([1,0,0,0])
            #self.cur_led_light.append([0,0,0])
        
        #self.sequence_pointer = [0]*num_of_leds

        #self.led_list = [None] *num_of_leds
        #for i in range(num_of_leds):
        #    self.led_list[i] = {"cur_color": [0,0,0],
        #                  "next_color": [[0,0,0]],
        #                  "dur": [1]}

    def run_nxt_animation_step(self):
        
        for i, led in enumerate(self.led_list):
            cur_r = self.cur_led_light[i][0]
            cur_g = self.cur_led_light[i][1]
            cur_b = self.cur_led_light[i][2]
            
            nxt_r = led_list[i][0][0]
            nxt_g = led_list[i][0][1]
            nxt_b = led_list[i][0][2]
            
            remaining_steps = led_list[i][0][3]
            
            #print(led["next_color"])
            #calc difference for color to reach
            #color_difference = [element1 - element2 for (element1, element2) in zip(led["next_color"][0], led["cur_color"])]
            dif_r = nxt_r - cur_r
            dif_g = nxt_g - cur_g
            dif_b = nxt_b - cur_b
            
            #divide difference by steps
            #color_difference_step = [round(x / led["dur"][0]) for x in color_difference]
            dif_r_step = round(dif_r/remaining_steps)
            dif_g_step = round(dif_g/remaining_steps)
            dif_b_step = round(dif_b/remaining_steps)
            
            #add step difference to cur_color
            #led["cur_color"] = [element1 + element2 for (element1, element2) in zip(led["cur_color"], color_difference_step)]
            self.cur_led_light[i][0] += dif_r_step
            self.cur_led_light[i][1] += dif_g_step
            self.cur_led_light[i][2] += dif_b_step
            
            #color led
            #self.neopixel_leds[i] = led["cur_color"]
            self.neopixel_leds[i] = [self.cur_led_light[i][0], self.cur_led_light[i][1], self.cur_led_light[i][2]]
            
            #lower led
            led["dur"][0] = led["dur"][0] - 1
            if led["dur"][0] <= 0:
                if len(led["dur"]) == 1:
                    led["dur"][0] = 1
                else:
                    led["next_color"].pop(0)
                    led["dur"].pop(0)
            led_list[i][0][3] = led_list[i][0][3] - 1
            if led_list[i][0][3] <= 0:
                    if len(led_list[i]) == 1:
                        led_list[i][0][3] = 1
                    else:
                        led_list[i].pop(0)
            
        # lower dur
        # gegebenenfalls pop entry

    
    def add_animation(self, led_idx, color, duration):
        # todo: add check if input has right format
        #self.led_list[led_idx]["next_color"].append(color)
        #self.led_list[led_idx]["dur"].append(duration)
        new_r = color[0]
        new_g = color[1]
        new_b = color[2]
        
        self.led_list[led_idx].append([color[0], color[1], color[2], duration] )
        
#[color[0], color[1], color[2], duration]        
    
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