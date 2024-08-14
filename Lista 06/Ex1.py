import random
import math

v = [random.randint(10, 90) for _ in range(10)]

print()
print(v)
print()

n50 = v.count(50)
soma = sum(v)
tamanho = len(v)
media = soma / tamanho
maior = max(v)
menor = min(v)
produto = math.prod(v)
vinv = v[::-1]
vPares = [num for num in v if num % 2 == 0]
vImpares = [num for num in v if num % 2 != 0]

if 50 in v:
    print("Existe o número 50 neste vetor")
    print()
    print("O numero 50 aparece {} vezes".format(n50))
    print()
else:
    print("Nao existe o numero 50 neste vetor")
    print()

print("A soma dos 10 numeros e: {}; E sua media e: {}".format(soma, media))
print()
print("O maior numero do vetor e {}; O menor numero e: {}".format(maior, menor))
print()
print("O produto dos vetores e: {}".format(produto))
print()
print("Vetor em ordem inversa: {}".format(vinv))
print()
print("Vetor com numeros pares: {}".format(vPares))
print()
print("Vetor com numeros impares: {}".format(vImpares))
print()
