# Dados não precisam ser tão “quadrados”, ou cúbicos para ser mais exato. Faça um programa que
# simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
# começo do programa quantas faces quer, para depois fazer o sorteio.

d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d16 = 16

print('1) D4')
print('2) D6')
print('3) D8')
print('4) D10')
print('5) D12')
print('6) D16')
print()

import random

dado = int(input('Digite aqui um número entre 1 e 6 para escolher qual dado você deseja: '))
print()

if dado == 1:
    a = random.randint(1,4)
    print('O número sorteado foi: ', a)
    print()

elif dado == 2:
    a = random.randint(1,6)
    print('O número sorteado foi: ', a)
    print()

elif dado == 3:
    a = random.randint(1,8)
    print('O número sorteado foi: ', a)
    print()

elif dado == 4:
    a = random.randint(1,10)
    print('O número sorteado foi: ', a)
    print()

elif dado == 5:
    a = random.randint(1,12)
    print('O número sorteado foi: ', a)
    print()

elif dado == 6:
    a = random.randint(1,12)
    print('O número sorteado foi: ', a)
    print()