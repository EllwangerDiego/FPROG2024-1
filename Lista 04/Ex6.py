
import random
numeros= []

for i in range(5):
    x = random.randint(0,100)
    numeros.append(x)

print()
print(numeros)
print()

MaiorNum = max(numeros)
MenorNum = min(numeros)

print("O maior numero eh {}".format(MaiorNum))
print()
print("O menor numero eh {}".format(MenorNum))
print()
soma = sum(numeros)
print("A soma foi de {}".format (soma))
print()
media = soma/5
print("A media foi de {}".format (media))
print()

