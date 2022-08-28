from time import sleep
import _thread
 
 
def core0_thread():
    counter = 0
    while True:
        print(counter)
        print("core0")
        counter += 2
        sleep(1)
 
 
def core1_thread():
    counter = 1
    while True:
        print(counter)
        print("core1")
        counter += 2
        sleep(2)
 
 
second_thread = _thread.start_new_thread(core1_thread, ())
 
core0_thread()