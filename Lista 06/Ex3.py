import random


vezes = int(input("Digite quantas vezes você quer girar o dado: "))


giradas = []


for _ in range(vezes):
    resultado = random.randint(1, 6)  
    giradas.append(resultado)  


print(f"Resultados das {vezes} giradas:")
print(giradas)


print("\nPercentual de cada face:")
for face in range(1, 7):  
    percentual = (giradas.count(face) / vezes) * 100
    print(f"Face {face}: {percentual:.2f}%")
print()
