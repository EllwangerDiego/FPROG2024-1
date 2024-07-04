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

soma2 = sum(matriz[1])

print("A soma dos elementos da segunda linha eh: \n{}".format(soma2))
print()
soma5 = sum(matriz[i][4] for i in range(4))
print("A soma dos elementos da quinta coluna eh: \n{}".format(soma5))
print()

multiplicacao = [matriz[0][j] * matriz[3][j] for j in range(6)]
soma_multi = sum(multiplicacao)
print("A multiplicação dos elementos da primeira linha pelos elementos da quarta linha eh: \n{}".format(multiplicacao))
print()
print("A soma dos elementos resultantes da multiplicação eh: \n{}".format(soma_multi))
print()

soma_linhas_impares = 0
for i in range(len(matriz)):
    if i % 2 != 0:  
        soma_linhas_impares += sum(matriz[i])

print("A soma dos elementos das linhas com índices ímpares é: \n{}".format(soma_linhas_impares))
print()