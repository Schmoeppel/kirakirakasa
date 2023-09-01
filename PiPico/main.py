from time import sleep
import time

from machine import Pin, SPI
import sdcard
import os
from utime import sleep_ms

from led_handler import led_handler


def init_sd():
    # Initialize the SD card
    spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
    sd=sdcard.SDCard(spi,Pin(13))

    # Create an instance of MicroPython Unix-like Virtual File System (VFS),
    vfs=os.VfsFat(sd)
     
    # Mount the SD card
    os.mount(sd,'/sd')

    # Debug print SD card directory and files
    print(os.listdir('/sd'))


init_sd()

num_of_leds = 136
led_handler = led_handler(4, num_of_leds)
button = Pin(0, Pin.IN, Pin.PULL_UP)   #Internal pull-up

global next_led_data
next_led_data = [0]

cur_animation = 0
animation_path = "/sd/animation_"+str(cur_animation)+".txt"

f = open(animation_path, "rb")

# Main loop
t0 = time.ticks_ms()
while True:
    if button.value() == 0:       #key press
        f.close()
        cur_animation += 1
        animation_path = "/sd/animation_"+str(cur_animation)+".txt"
        f = open(animation_path, "rb")
    #sleep(0.001)
    data = f.readline()
    next_led_data = [x for x in data]

    if (next_led_data == []): # sequence ended
        f.close()
        f = open(animation_path, "rb")
        data = f.readline()
        next_led_data = [x for x in data]
        #break
    
    led_idx = 0
    for led_color in range(0, num_of_leds*3-2, 3):
        
        color = [next_led_data[led_color], next_led_data[led_color+1], next_led_data[led_color+2]]
        led_handler.set_leds_color(led_idx, color)
        led_idx += 1
    led_handler.light_leds()
    
    
t1 = time.ticks_ms()

print("Time it took: " + str(t1-t0))


    
    
    


 

