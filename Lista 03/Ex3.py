#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
#o resultado.

n = float(input('Digite um número: '))
print()

if n > 0:
    print('O dobro desse número é:', n * 2)
    print()
else:
    print('O triplo desse número é: ', n * 3)
    print()