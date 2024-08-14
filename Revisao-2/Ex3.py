x = 1
v = 0

def tabuada():
    x = 1
    v = 0
    print()
    num = int(input("Digite aqui um valor: "))
    print()
    while x < 11:
        v = num * x
        print(f"{num} X {x} = {v} ")
        x = x + 1

tabuada()
print()