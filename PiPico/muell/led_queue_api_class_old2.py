#09.07.2022

import neopixel2
import machine

from machine import Pin, SPI
import sdcard
import os


#led_queue_api(num_of_leds)

class led_queue_api:
    
    
    def __init__(self, pin, num_of_leds):
        self.neopixel_leds = neopixel2.NeoPixel(machine.Pin(pin), num_of_leds)
        self.num_of_leds = num_of_leds
        self.current_folder = "sd"

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
        #self.led_list[led_idx]["next_color"].append(color)
        #self.led_list[led_idx]["dur"].append(duration)
        self.led_list[led_idx]["next_color"].append(color)
        file_name = "/sd/led" + str(led_idx) + ".txt"
        file = open(file_name,"a")
        #100,0,0,100\r\n     r,g,b,dur\r\n
        # Write sample text
        file.write(f"{color[0]},{color[1]},{color[2]},{duration}\r\n")
        file.close()
    
    def par_all_led_timings(self):
        pass
    
    def write_leds(self):
        self.neopixel_leds.write()
        
    def create_txt_files_on_sd(self):
        # Create / Open a file in write mode.
        # Write mode creates a new file.
        # If  already file exists. Then, it overwrites the file.
        for i in range(self.num_of_leds):
            file_name = self.current_folder + "/led" + str(i) + ".txt"
            file = open(file_name,"w")
            file.close()
        print(os.listdir(self.current_folder))
    
    def delete_all_txt_files_on_sd(self):
        for file in os.listdir('/sd'):
            os.remove("/sd/" + file)
        print(os.listdir('/sd'))
    
    def set_cur_folder(self, folder_name):
        self.current_folder = folder_name
        
    def init_sd_card(self):
        # Initialize the SD card
        spi=SPI(1,baudrate=40000000,sck=Pin(10),mosi=Pin(11),miso=Pin(12))
        sd=sdcard.SDCard(spi,Pin(13))
        # Create a instance of MicroPython Unix-like Virtual File System (VFS),
        vfs=os.VfsFat(sd)
         
        # Mount the SD card
        os.mount(sd,'/sd')

        # Debug print SD card directory and files
        print(os.listdir('/sd'))

    def print_sd_sequence(self, led):
        with open(f"/sd/led{led}.txt") as file:
            lines = file.readlines()
        #print(lines)
        '''
        file = open(f"/sd/led{led}.txt", "r")
        if file != 0:
            print("Reading from SD card")
            read_data = file.read()
            print (read_data)
        file.close()
        '''
        
    def read_nxt_line_from_txt_sequence(led):
        with open(f"/sd/led{led}.txt") as file:
            line = file.readline()
        print(line)
        return [r,g,b], dur
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
