x = 20
import time
print(x)
while x >= 20 and x <= 50:
    x = x + 1
    if x % 2 == 0:
        time.sleep(0.5)
        print(x)