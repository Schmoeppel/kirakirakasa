from time import sleep
import time
import _thread

from machine import Pin, SPI
import sdcard
import os


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
 
class Flag:
    core0_is_using_data = False
 
    @classmethod
    def set_core0_is_using_data_flag(cls):
        cls.core0_is_using_data = True
 
    @classmethod
    def clear_core0_is_using_data_flag(cls):
        cls.core0_is_using_data = False
 
    @classmethod
    def get_core0_is_using_data_flag(cls):
        return cls.core0_is_using_data

 
def core0_thread():
    # run main code
    # create txt file
    # run loop in which leds are updated
    global next_led_data
    next_led_data = [0]
    num = 255
    with open('/sd/test_file.txt', 'wb') as f:
        for line in range(10):
            num = line
            if num > 100:
                num = 100
            for i in range(5):
                f.write(num.to_bytes(1, 'big'))
            f.write("\n")
    print(os.listdir('/sd'))
    flg.clear_core0_is_using_data_flag()
    while True:
        if flg.get_core0_is_using_data_flag():
            print(next_led_data)
            flg.clear_core0_is_using_data_flag()
        #break
 
 
def core1_thread():
    global next_led_data
    # run code in which new lines are read from the txt file
    while flg.get_core0_is_using_data_flag():
        pass
    
    a=True
    f = open("/sd/test_file.txt", "rb")
    while a==True:
        if not flg.get_core0_is_using_data_flag():
            #f = open("/sd/test_file.txt", "rb")
            data = f.readline()
            print("read next line in core1")
            #f.close()
            next_led_data = [x for x in data]
            #f.close()
            flg.set_core0_is_using_data_flag()
            #a=False
    f.close()
 
 
flg = Flag()
flg.set_core0_is_using_data_flag()
second_thread = _thread.start_new_thread(core1_thread, ())


core0_thread()
