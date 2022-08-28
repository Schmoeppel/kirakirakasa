from machine import Pin, SPI
import sdcard
import os
import time

#https://bytesnbits.co.uk/multi-thread-coding-on-the-raspberry-pi-pico-in-micropython/

# Initialize the SD card
spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
sd=sdcard.SDCard(spi,Pin(13))

# Create a instance of MicroPython Unix-like Virtual File System (VFS),
vfs=os.VfsFat(sd)
 
# Mount the SD card
os.mount(sd,'/sd')


t0 = time.ticks_ms()

'''
for i in range(1):
    with open("/sd/test_file.txt", "r") as f:
        data = f.readlines()
   '''

'''
with open("/sd/test_file.txt", "rb") as f:
    for line in range(99):
        data = f.readline()
   '''

f = open("/sd/test_file.txt", "rb")
#for i in range(901):
#    next(f)
data = f.readline()
#f.close()
    
int_values = [x for x in data]

t1 = time.ticks_ms()
print(data)
print(int_values)

print(t1-t0)
