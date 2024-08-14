import random
import math

tamanho = 5
v = []

print()
print("Digite {} valores para preencher o vetor:".format(tamanho))
print()
for i in range(tamanho):
    valor = int(input(f"Digite o {i+1}º valor: "))
    v.append(valor)

print()
print("Valores do vetor: {}".format(v))
print()

primeiro = v[0]
segundo = v[1]
terceiro = v[2]
quarto = v[3]
quinto = v[4]

x1 = primeiro * 1
x2 = segundo * 2
x3 = terceiro * 3
x4 = quarto * 4
x5 = quinto * 5

print("Os valores dos numeros multiplicados pela sua posicao e: {}, {}, {}, {}, {}.".format(x1,x2,x3,x4,x5))
print()