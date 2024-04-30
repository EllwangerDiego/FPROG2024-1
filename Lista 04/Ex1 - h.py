

numeros = []
print()
n = int(input("Digite aqui a quantidade de numeros que voce deseja somar: "))
print()
for i in range (n):
    numero = int(input("Digite aqui um numero: "))
    numeros.append(numero)

soma = sum(numeros)
print("A soma eh: ",soma)

