import machine
import random
from time import sleep

from led_queue_api_class import led_queue_api
#import led_queue_api_class

num_of_leds = 135
led_animation = led_queue_api(4, num_of_leds)

print(random.randint(0,10)) 

'''
for i in range(num_of_leds):
    led_animation.add_animation(i, [100, 0, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 100, 0], 100)
for i in range(num_of_leds):
    led_animation.add_animation(i, [0, 0, 100], 100)
'''

for i in range(100):
    for i in range(num_of_leds):
        red_color = random.randint(0,250)
        green_color = random.randint(0,250)
        blue_color = random.randint(0,250)
        dur = random.randint(0,60)
        led_animation.add_animation(i, [red_color, green_color, blue_color], 100)
    


while(1):
    led_animation.run_nxt_animation_step()
    led_animation.write_leds()
    sleep(0.01)