solteiro = []
casado = []
divorciado = []
viuvo = []
x = 4

while x != 0:
    print()
    nome = input("Digite aqui o nome: ")
    print()
    print("|--------------------|")
    print("|   1. Solteiro(a)   |")
    print("|   2. Casado(a)     |")
    print("|   3. Divorciado(a) |")
    print("|   4. Viúvo(a)      |")
    print("|--------------------|")
    print()
    opcao = int(input("Digite aqui um número de 1 a 4 para seu estado civil: "))
    print()

    if opcao == 1:
        solteiro.append(nome)
    if opcao == 2:
        casado.append(nome)
    if opcao == 3:
        divorciado.append(nome)
    if opcao == 4:
        viuvo.append(nome)
    x = x - 1

print("Solteiros: ")
print(solteiro)
print()

print("Casados:")
print(casado)
print()

print("Divorciados: ")
print(divorciado)
print()

print("Viúvos: ")
print(viuvo)
print()

