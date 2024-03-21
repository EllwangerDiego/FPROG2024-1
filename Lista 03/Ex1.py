#Escreva um programa que leia dois números e efetue uma divisão, mas somente se o divisor for
#diferente de zero; quando isto ocorrer, é mostrada uma mensagem de erro apropriada.

NDiv = float(input('Digite um número: '))
print()
Divisor = float(input('Digite o valor do divisor: '))
print()

if (Divisor == 0):
    print('error')
    print()
else: 
    resultado = NDiv / Divisor
    print('O resultado desta operação é:', resultado)
