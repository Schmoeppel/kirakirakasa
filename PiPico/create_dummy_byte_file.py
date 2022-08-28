from machine import Pin, SPI
import sdcard
import os

num_of_leds = 136


def create_dummy_byte_file():
    # Create txt file
    num_of_steps = 1000
    color = 0
    
    with open('/sd/test_file.txt', 'wb') as f:
        for step in range(num_of_steps):
            color += 1
            if color > 110:
                color = 1
            if color == 10:
                color = 11
            for rgb_color in range(num_of_leds*3):
                f.write(color.to_bytes(1, 'big'))
            f.write("\n")
            print(step)
    #print(os.listdir('/sd'))
            
            
def init_sd():
    # Initialize the SD card
    spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
    sd=sdcard.SDCard(spi,Pin(13))

    # Create a instance of MicroPython Unix-like Virtual File System (VFS),
    vfs=os.VfsFat(sd)
     
    # Mount the SD card
    os.mount(sd,'/sd')

    for file in os.listdir('/sd'):
        os.remove("/sd/" + file)

    # Debug print SD card directory and files
    print(os.listdir('/sd'))
    
    
init_sd()
create_dummy_byte_file()