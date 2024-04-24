#Faça um programa que sorteie um número de 1 a 10 e peça para o usuário tentar adivinhar. O usuário tem 3 chances de acertar. Indique se o usuário 
#acertou ou errou a cada tentativa

import random
R = random.randint(1,10)
print(R)
cont = 0


while cont < 3:
    print()
    U = int(input("Digite aqui um numero entre 1 e 10: "))
    print()
    if U == R:
       print('Voce acertou')
       print()
       cont = cont + 3

    elif cont < 2:
        print('Voce errou, tente novamente')
        cont = cont + 1
    else:
        print("Acabaram suas tentativas")
        print()
        cont = cont + 1
