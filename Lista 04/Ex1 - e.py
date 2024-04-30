import random
numeros = []
for i in range(15):
    numero = int(input("Digite aqui um numero: "))
    numeros.append(numero)

soma = sum(numeros)
print("A soma eh: ",soma)
media = soma / 2
print("A media eh", media)