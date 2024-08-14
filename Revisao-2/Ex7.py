x = 6
z = 6


while x != 0:
    print()
    senha = input("Digite aqui sua senha composta apenas por dígitos e deve ter entre 5 e 10 valores: ")
    a = senha.isdigit()

    if a == False:
        print()
        print("Digite apenas números!")
        x = x - 1
        z = x

    else:

        print()
        y = len(senha)

        if y < 5:
            print("Digite uma senha com mais de 5 digitos e menos de 10!")
            print()
            x = x - 1
            z = x

        if y > 10:
            print("Digite uma senha com menos de 10 dígitos e mais de 5! ")
            print()
            x = x - 1
            z = x

        if y > 4 and y < 11:
            print("Senha definida com sucesso! ")
            x = 0
            print()
            print(senha)
            print()
        
        if z == 0:
            print()
            print("Suas tentativas acabaram!")
            print()

