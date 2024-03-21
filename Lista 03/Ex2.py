#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A + C.

a = int(input('Digite um número: '))
print()
b = int(input('Digite outro número: '))
print()
c = int(input('Digite outro número: '))
print()

if a + b < a + c:
    print('A soma dos números', a, '+', b, ' é menor que a soma de', a, '+', c )
    print('')
elif a + b == a + c:
    print('A soma de', a, '+', b, 'é igual a soma de', a, '+', c)

else:
    print('A soma dos números', a, '+', b, ' é maior que a soma de', a, '+', c )
    print()