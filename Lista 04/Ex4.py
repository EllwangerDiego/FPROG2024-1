
print()
divisor = int(input("Digite aqui o valor do divisor: "))
print()
Aintervalo = int(input("Digite aqui o inicio do intervalo: "))
print()
Bintervalo = int(input("Digite aqui o fim do intervalo: "))
print()

for i in range (Aintervalo,Bintervalo):
    if i % divisor == 0:
        print("-----------------------------")
        print(i,"eh divisivel por ", divisor)
print("-----------------------------")