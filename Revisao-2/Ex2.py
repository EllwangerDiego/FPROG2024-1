
print()
t1 = int(input("Digite aqui um valor: "))
print()
t2 = int(input("Digite aqui outro valor: "))
print()

if t1 < t2:
    while t1 != t2:
        print(t1)
        t1 = t1 + 1
    print(t2)
else:
    while t2 != t1:
        print(t2)
        t2 = t2 + 1
    print(t1)
print()