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

'''
with open('/sd/test_file.txt', 'w') as f:
    for i in range(1000):
        f.write('123\r\n')
        '''
        
#newFileByteArray = bytearray(newFileBytes)
num = 255
with open('/sd/test_file.txt', 'wb') as f:
    for line in range(1000):
        num = line
        if num > 100:
            num = 100
        for i in range(600):
            f.write(num.to_bytes(1, 'big'))
        f.write("\n")

print(os.listdir('/sd'))
    
