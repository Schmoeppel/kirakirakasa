from time import sleep
import time

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

    # remove all existing files
    #for file in os.listdir('/sd'):
    #    os.remove("/sd/" + file)

    # Debug print SD card directory and files
    print(os.listdir('/sd'))


init_sd()



num_of_leds = 136
led_handler = led_handler(4, num_of_leds)

global next_led_data
next_led_data = [0]

f = open("/sd/test_file.txt", "rb")

read_line_num = 0

#while True:
#    led_handler.light_all_leds([100, 0, 0])

# Main loop
t0 = time.ticks_ms()
while True:
    #print(read_line_num)
    read_line_num+=1
    #print(next_led_data)
    sleep(0.02)
    data = f.readline()
    #print(data)
    #print("read next line")
    #f.close()
    next_led_data = [x for x in data]
    #next_led_data = [int.from_bytes(x, 'big') for x in data]
    
    
    if (next_led_data == []):
        f.close()
        break
    
    led_idx = 0
    for led_color in range(0, num_of_leds*3-2, 3):
        
        #print(led_color)
        #print(next_led_data)
        color = [next_led_data[led_color], next_led_data[led_color+1], next_led_data[led_color+2]]
        led_handler.set_leds_color(led_idx, color)
        led_idx += 1
    led_handler.light_leds()
    
    
t1 = time.ticks_ms()

print("Time it took: " + str(t1-t0))


    
    
    


 
