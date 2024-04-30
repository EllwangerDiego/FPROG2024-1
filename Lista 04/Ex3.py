print()
x = 1
while x == 1:
    print()
    n = int(input("Digite um numero inteiro entre 1 e 9: "))
    print("---------------------------------")

    for x in range (1,11):
        tabuada = n * x

        print(n, "x", x, "=", n * x)
        print("---------------------------------")
    a = input("Deseja calcular outro numero? (s/n) ")
    if a == "s":
        x = 1
    elif a == "n":
        x = 0
    

