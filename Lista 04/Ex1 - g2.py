import random

x = 0
while x <20:
    y = random.randint(-10,10)
    if y == 0:
        print(y, "eh nulo")
        
    elif y % 2 == 0:
        print(y, "eh um numero par")
        
    else:
        print(y, "eh um numero impar")
       
    x = x + 1
