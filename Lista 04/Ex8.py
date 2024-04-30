x = 1
while x == 1:
    print()
    num = int(input("Digite aqui um numero: "))
    print()

    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print("O fatorial de", num, "é", fatorial)
    print()
    escolha = input("Voce deseja calcular outro numero? (S/N) ")
    print()
    if escolha == "S" or escolha == "s":
        x = 1
    elif escolha == "N" or escolha == "n":
        x = 0
        print("Encerrando o programa...")
