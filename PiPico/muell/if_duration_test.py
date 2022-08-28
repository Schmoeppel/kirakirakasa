import time

a = 10
i = 0


t0 = time.ticks_ms()

while(i<200*1000):
    i += 1
    if ((a >=5)):
        pass

t1 = time.ticks_ms()

print(t1-t0)