import neopixel2
import machine
import my_test_lib
import utime
from time import sleep
import transcribe_led_matrix


led_num = 140

kasa = neopixel2.NeoPixel(machine.Pin(4), led_num)

'''
def get_led_from_matrix(rc):
    
    matrix = [[16, 51, 84, 119, 17, 50, 85,  118],
              [15, 52, 83, 120, 18, 49, 86,  117],
              [14, 53, 82, 121, 19, 48, 87,  116],
              [13, 54, 81, 122, 20, 47, 88,  115],
              [12, 53, 80, 123, 21, 46, 89,  114],
              [11, 52, 79, 124, 22, 45, 90,  113],
              [10, 51, 78, 125, 23, 44, 91,  112],
              [9,  50, 77, 126, 24, 43, 92,  111],
              [8,  49, 76, 127, 25, 42, 93,  110],
              [7,  48, 75, 128, 26, 41, 94,  109],
              [6,  47, 74, 129, 27, 40, 95,  108],
              [5,  46, 73, 130, 28, 39, 96,  107],
              [4,  45, 72, 131, 29, 38, 97,  106],
              [3,  44, 71, 132, 30, 37, 98,  105],
              [2,  43, 70, 133, 31, 36, 99,  104],
              [1,  42, 69, 134, 32, 35, 100, 103],
              [0,  41, 68, 135, 33, 34, 101, 102]]
    
    return_values = []
    led_num = len(rc[0])
    for n in range(led_num):
        r = rc[0][n]
        c = rc[1][n]
        return_values.append(matrix[r][c])
        print(matrix[r][c])
    return return_values

'''

# create matrix
matrix_first_row = [16, 51, 84, 119, 17, 50, 85, 118]
change = [-1, 1, -1, 1, 1, -1, 1, -1]

matrix_next_row = matrix_first_row
matrix = []
matrix.append(matrix_first_row)
for i in range(16):
    difference = []
    zip_object = zip(matrix_next_row, change)
    for list1_i, list2_i in zip_object:
        difference.append(list1_i+list2_i)
    matrix_next_row = difference
    matrix.append(matrix_next_row)
######################
    
def color_ring(ring_num, color):
    ring_leds = matrix[ring_num]
    for led in ring_leds:
        kasa[led] = color
        
def color_column(column_num, color):
    column_leds = []
    for i in range(17):
        column_leds.append(matrix[i][column_num])
    for led in column_leds:
        
        kasa[led] = color

def color_single_led(ring, column, color):
    led = matrix[ring][column]
    kasa[led] = color
    
def turn_off_all():
    all_leds = [j for sub in matrix for j in sub]
    for led in all_leds:
        kasa[led] = (0, 0, 0)
        
def turn_on_all(color):
    all_leds = [j for sub in matrix for j in sub]
    for led in all_leds:
        kasa[led] = color

# Draw a red gradient.
while(1):
    while(0):
        color_ring(16, (0,0,200))
        color_column(1, (0,200,0))
        color_single_led(16, 0, (200, 0, 0))
        kasa.write()
    
    while(0):
        for i in range(17):
            turn_off_all()
            color_ring(i, (0,200,0))
            kasa.write()
            sleep(1)
    
    while(1):
        brightness = 30
        pause = 0.001
        factor = 3
        for i in range(brightness):
            #turn_off_all()
            turn_on_all((0,1+factor*i,0))
            kasa.write()
            sleep(pause)
        for i in range(brightness):
            turn_on_all((0,1+factor*brightness-i*factor,0))
            kasa.write()
            sleep(pause)
        
        
    for i in range(led_num):
        kasa[i] = (0, 100, 0)
        utime.sleep(0.05)
        kasa.write()
    
    for i in range(led_num):
        kasa[i] = (i * 0, 0, 0)
    kasa.write() 
    
    

# Update the strip.
n.write()