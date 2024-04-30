#FUNCOES#
import random
import time

#Dado
def Dado1(Jogador1):
    roleta = random.randint(1,6)
    if roleta == 1:
        posJogador1 + 1
    if roleta == 3:
        posJogador1 = -1
    if roleta == 6 and jogadores == 2:
        Jogador1 

def Dado2(Jogador2):
    roleta = random.randint(1,6)
    if roleta == 1:
        posJogador2 + 1
    if roleta == 3:
        posJogador2 = -1
    if roleta == 6 and jogadores == 2:
        Jogador2 








posJogador1 = 0
posJogador2 = 0

filhosJogador1 = 0 
filhosJogador2 = 0 

dinheiroJogador1 = 0 
dinheiroJogador2 = 0

jogador1Casado = False 
jogador1Divorciado = False 
jogador1Formado = False 
jogador1Famoso = False 
jogador1Vivo = True

jogador2Casado = False 
jogador2Divorciado = False 
jogador2Formado = False 
jogador2Famoso = False 
jogador2Vivo = True



#MAIN#

print()
jogadores = int(input("Digite aqui a quantidade de jogadores: "))
print()

while jogador1Vivo == True and jogador2Vivo == True:
    print()