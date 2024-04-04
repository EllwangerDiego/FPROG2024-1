senha = 1234
cont = 0

while cont < 3:
    print()
    senha = int(input('Digite aqui a sua senha de 4 digitos: '))
    print()

    if senha == 1234:
       print('Senha correta')
       print()
       cont = cont + 3

    elif cont < 2:
        print('Senha incorreta, tente novamente')
        
        cont = cont + 1
    else:
        print('Parabéns, você bloqueou a conta!!!!!!!!!!!!!!!!!')
        cont = cont + 1
        print()
