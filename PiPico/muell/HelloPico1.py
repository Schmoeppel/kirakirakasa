import machine
import utime

led_pin =machine.Pin(25, machine.Pin.OUT)
print("Hello picos")

bakadeline = "bakadeline"

while True:
    
    led_pin.value(1)
    print(bakadeline)
    bakadeline += " bakadeline"
    utime.sleep(0.01)
    led_pin.value(0)
    utime.sleep(0.01)