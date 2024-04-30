import random

def sorteio():
    print()
    inicio = int(input("Digite aqui um numero de inicio de parametro: "))
    print()
    final = int(input("Digite aqui um numero de final de parametro: "))
    print()
    sorteio = random.randint(inicio,final)
    print("O numero sorteado foi {}".format(sorteio))

sorteio()