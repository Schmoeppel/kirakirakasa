import machine
import random
from time import sleep
import micropython
import time

from led_queue_api_class import led_queue_api
#import led_queue_api_class

num_of_leds = 2
led_animation = led_queue_api(4, num_of_leds)

#print(random.randint(0,10)) 

'''
for i in range(num_of_leds):
    led_animation.add_animation(i, [100, 0, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 100, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 0, 100], 100)
'''



for n in range(0):
    for i in range(num_of_leds):
        #red_color = random.randint(0,250)
        #green_color = random.randint(0,250)
        #blue_color = random.randint(0,250)
        #dur = random.randint(1,60)
        #led_animation.add_animation(i, [red_color, green_color, blue_color], dur)
        #led_animation.led_list[0][0].append(2)    
        led_animation.add_animation(i, [10, 10, 10], 5)

#led_animation.add_animation(0, [10, 10, 10], 5)

a = 3
#test_list = [999]*30335

#print(micropython.mem_info())
micropython.mem_info(1)

print(led_animation.led_list)

print("code ended")

'''
while(1):
    led_animation.run_nxt_animation_step()
    led_animation.write_leds()
    sleep(0.01)
'''