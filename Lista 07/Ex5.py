import random
import math

matriz = []

print()
for i in range (4):
    linha = []
    for j in range(6):
        linha.append(random.randint(-19,10))
    matriz.append(linha)

for linha in matriz:
    print(linha)
print()

flatten_matriz = [elemento for linha in matriz for elemento in linha]
maior_valor = max(flatten_matriz)
menor_valor = min(flatten_matriz)

print("O maior valor na matriz é:", maior_valor)
print("O menor valor na matriz é:", menor_valor)
print()