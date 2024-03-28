#Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
#disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
#um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
#soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
#que o programa venceu 

print()
pi = input("Você aposta em par ou impar? ")

print()
aposta = int(input('Digite aqui um número inteiro de 0 a 5: '))
print()

import random
a = random.randint (0,5)

b = aposta + a

print('A soma dos números foi: ', b)
print()
if b % 2 == 0 and pi == 'par':
    print('Parabéns, você ganhou!')
    print()
elif b % 2 != 0 and pi == 'impar':
    print('Parabéns, você ganhou!')
    print()
else: 
    print('Você perdeu!')
    print()



