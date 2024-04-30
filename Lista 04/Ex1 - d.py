x = 95
import time

print(x)
while x <=95 and x >=25:
    x = x - 1
    if x % 2 != 0:
        time.sleep(0.5)
        print(x)