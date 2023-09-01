"""
Kirakirakasa
==============

This project controls an LED strip to illuminate an umbrella with preprogrammed patterns from an SD card using a PiPico.

Author:
- Thomas Killus (TKillussecond@gmail.com)

License:
- This project is licensed under the MIT License. See the LICENSE file for details.
"""

from machine import Pin, SPI
import sdcard
import os

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
LED_PIN = 4
BUTTON_PIN = 0
led_handler = led_handler(LED_PIN, num_of_leds)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)   #Internal pull-up

global next_led_data
next_led_data = [0]

cur_animation = 0
animation_path = "/sd/animation_"+str(cur_animation)+".txt"

f = open(animation_path, "rb")

# Main loop
while True:
    if button.value() == 0:       #key pressed, play next animation
        f.close()
        cur_animation += 1
        animation_path = "/sd/animation_"+str(cur_animation)+".txt"
        f = open(animation_path, "rb")

    data = f.readline()
    next_led_data = [x for x in data]

    if (next_led_data == []): # sequence ended, restart
        f.close()
        f = open(animation_path, "rb")
        data = f.readline()
        next_led_data = [x for x in data]
    
    led_idx = 0
    for led_color in range(0, num_of_leds*3-2, 3):
        
        color = [next_led_data[led_color], next_led_data[led_color+1], next_led_data[led_color+2]]
        led_handler.set_leds_color(led_idx, color)
        led_idx += 1
    led_handler.light_leds()


    
    
    


 

