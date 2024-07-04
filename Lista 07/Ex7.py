import random

matriz = []
print()
for _ in range(5):
    num1 = round(random.uniform(-10, 10))
    num2 = round(random.uniform(-10, 10))
    num3 = round(random.uniform(-10, 10))
    num4 = round(random.uniform(-10, 10))
    num5 = round(random.uniform(-10, 10))

    linha = [num1, num2, num3, num4, num5]
    matriz.append(linha)


for linha in matriz:
    print(linha)
    print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] *= -1

print("Matriz após multiplicação por -1:")
print()
for linha in matriz:
    print(linha)
    print()