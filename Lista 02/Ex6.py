#A loja de eletrônicos TechMundo vende uma certa quantidade de smartphones e uma quantidade
#de tablets a cada dia. Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
#do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
#um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
#arrecadado.

print()
smartphone = float(input('Digite aqui a quantidade de Smartphones vendidos no dia: '))
print()

tablets = float(input('Digite aqui a quantidade de Tablets vendidos no dia: '))
print()
print('#--------------------------------------------------------------------#')
print()
STotal = smartphone * 1000

TTotal = tablets * 1500
import time

Total = smartphone * 1000 + tablets * 1500
print('Foi vendido R$', STotal, 'em Smartphones')
time.sleep (3)
print()
print('R$', TTotal, 'em Tablets')
time.sleep (3)
print()

print('O total arrecadado foi de: ', Total)
print()