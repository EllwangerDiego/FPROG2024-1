import random
import time

def calcular_media(grau_a, grau_b):
    return (grau_a + (grau_b * 2)) / 3


matriz_notas = []
for _ in range(10):
    grau_a = round(random.uniform(0.0, 10.0), 2)  
    grau_b = round(random.uniform(0.0, 10.0), 2)  
    media_unisinos = calcular_media(grau_a, grau_b)
    
    linha = ["{:.2f}".format(grau_a), "{:.2f}".format(grau_b), "{:.2f}".format(media_unisinos)]
    matriz_notas.append(linha)


print()
print("Matriz de Notas:")
print()
print("[Grau A | Grau B | Media]")
for linha in matriz_notas:
    print(linha)
    time.sleep(0.5)
print()
