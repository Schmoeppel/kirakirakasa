#import machine
import machine
import random
from time import sleep
import micropython
import time

from led_queue_api_class import led_queue_api

#import micropython


#test_list = [999]*335
#rows, cols = (, 5)
#arr = [[0]*cols]*rows

#print(test_list[20000])

#linear
#test_list = [999]*200*30000*4

#one list
#test_list = [[[999]*4]*30000]*200

#one list correct init
test_list = [None]*200
for i in range(200):
    test_list[i] = [[999,999,99,990]]
    for n in range(10):
        test_list[i].append([989,999,99,990])

print(test_list)
#test_line_cnt = [0]*200

print(len(test_list))

#test_line_cnt = [30000 for element in test_line_cnt]




'''
test_list_ap = [[999]*4]*30000
test_list = []
for i in range(200):
    test_list.append(test_list_ap)

for i in range(1):
    #test_list[0][0].append(998)
    pass
'''

#print(test_list)

#print(test_list[0].append([999,999,999,998])
#print(test_list)


micropython.mem_info(1)