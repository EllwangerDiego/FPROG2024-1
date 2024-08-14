import random
import time
n = 5

#Criando a matriz, sorteando numeros entre 0 e 100 e imprimindo ela
matriz = []
for _ in range(n):
    num = round(random.randint(0, 100))  
    linha = [num]
    matriz.append(linha)

print()
print("Matriz")
print(matriz)
print()
time.sleep(2)

#Sorteando 2 numeros da matriz
numero1 = random.randint(0, n - 1)  
numero2 = random.randint(0, n - 1)  

num1 = matriz[numero1]  
num2 = matriz[numero2] 

print()
print("Os numeros aleatorios sorteados da matriz foram:")
print(num1, num2)
print()
time.sleep(2)

#invertendo os valores dos numeros
matriz[numero1], matriz[numero2] = matriz[numero2], matriz[numero1]

print("Invertendo os 2 numeros selecionados na matriz: ")
print(matriz)
print()
time.sleep(2)
