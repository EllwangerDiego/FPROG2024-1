import random
import time

# Variáveis
turno = 1
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

jogador = posJogador1

curso_jogador1 = "nada"
curso_jogador2 = "nada"


#FUNCOES

#ROLETA

def Roleta():
    roleta = random.randint(1, 6)
    jogador = jogador + roleta
    return jogador


#Dado

def Dado():
    global jogador
    global turno
    global posJogador1
    global posJogador2
    global perderodada
    if turno % 2 != 0:
        jogador = posJogador1
    else:
        jogador = posJogador2
    if turno % 2 != 0:
        if jogador == 1 or jogador == 3 or jogador == 10 or jogador == 17:
            roleta = random.randint(1, 6)
            if roleta == 1:
                jogador = min(jogador + 1, 21) 
            elif roleta == 3:
                jogador = max(jogador - 1, 0) 
            elif roleta == 6 and jogadores == 2:
                perderodada = True
                jogador = "Perdeu uma rodada"
    return jogador
    
#Morreu

def Morrer():
    global jogador
    global turno
    global jogador1Vivo, jogador2Vivo, posJogador1, posJogador2
    if jogador == 2 or jogador == 8 or jogador == 18: 
        if jogador == posJogador1:
            jogador1Vivo = False
        elif jogador == posJogador2:
            jogador2Vivo = False


#Desafio mat

def DesafioMatematico():
    global jogador
    global turno
    global posJogador1
    global posJogador2

    roleta = random.randint(1, 6)
    if posJogador1 == 4 or posJogador1 == 11 or posJogador1 == 19:
        print(roleta)
        time.sleep(2)
        if roleta == 1:
            #primos ate 100
            print("| 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 |")
            print("|------------------------------------------------------------|")
            print("|43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97   |")
        # restante do código...


        elif roleta == 2:
    #somatorio (inicio,fim)
            numeros = []  

            for i in range(1, 11):  
                numeros.append(i)  

            soma = sum(numeros)
            print()
            print(numeros)  
            print()
            print("A soma desses numeros e: {}".format(soma))
            print()

        elif roleta == 3:
    #fibonacci ate o decimo elemento
            fibonacci = [0, 1]


            for i in range(2, 10):
                proximo_numero = fibonacci[-1] + fibonacci[-2]  
                fibonacci.append(proximo_numero)  

            print()
            print("Sequência de Fibonacci até o décimo elemento:")
            print()
            print(fibonacci)
            print()

        elif roleta == 4:
    #Area de um circulo com raio 2.5

            raio = 2.5
            pi = 3.14159

            area = pi * (raio ** 2)

            print()
            print("A área do círculo com raio de 2.5 é:", area)
            print()

        elif roleta == 5:
            #imprimir o fatorial de 5
            fatorial = 1

            for i in range(1, 5 + 1):
                fatorial *= i

            print()
            print("O fatorial de 5 é", fatorial)
            print()

        elif roleta == 6:
            #imprimir os 5 primeiros numeros divisiveis por 2 e por 5
            numeros_encontrados = []
            numero = 1

            while len(numeros_encontrados) < 5:
                
                if numero % 2 == 0 and numero % 5 == 0:
                    numeros_encontrados.append(numero)  
                numero += 1 

            print()
            print("Os 5 primeiros números divisíveis por 2 e por 5 são:", numeros_encontrados)
            print()

#JOGADOR 2 MAT

    if posJogador2 == 4 or posJogador2 == 11 or posJogador2 == 19:
        print(roleta)
        time.sleep(2)
        if roleta == 1:
            #primos ate 100
            print("| 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 |")
            print("|------------------------------------------------------------|")
            print("|43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97   |")
        # restante do código...


        elif roleta == 2:
    #somatorio (inicio,fim)
            numeros = []  

            for i in range(1, 11):  
                numeros.append(i)  

            soma = sum(numeros)
            print()
            print(numeros)  
            print()
            print("A soma desses numeros e: {}".format(soma))
            print()

        elif roleta == 3:
    #fibonacci ate o decimo elemento
            fibonacci = [0, 1]


            for i in range(2, 10):
                proximo_numero = fibonacci[-1] + fibonacci[-2]  
                fibonacci.append(proximo_numero)  

            print()
            print("Sequência de Fibonacci até o décimo elemento:")
            print()
            print(fibonacci)
            print()

        elif roleta == 4:
    #Area de um circulo com raio 2.5

            raio = 2.5
            pi = 3.14159

            area = pi * (raio ** 2)

            print()
            print("A área do círculo com raio de 2.5 é:", area)
            print()

        elif roleta == 5:
            #imprimir o fatorial de 5
            fatorial = 1

            for i in range(1, 5 + 1):
                fatorial *= i

            print()
            print("O fatorial de 5 é", fatorial)
            print()

        elif roleta == 6:
            #imprimir os 5 primeiros numeros divisiveis por 2 e por 5
            numeros_encontrados = []
            numero = 1

            while len(numeros_encontrados) < 5:
                
                if numero % 2 == 0 and numero % 5 == 0:
                    numeros_encontrados.append(numero)  
                numero += 1 

            print()
            print("Os 5 primeiros números divisíveis por 2 e por 5 são:", numeros_encontrados)
            print()
    

#SE FORMOU

def SeFormou():
    

    roleta_jogador1 = random.randint(1, 6)
    roleta_jogador2 = random.randint(1, 6)
    if posJogador1 == 5:
        jogador1Formado == True
        curso_jogador1 = "nada"

        if roleta_jogador1 == 1:
            curso_jogador1 = "Direito"
        elif roleta_jogador1 == 2:
            curso_jogador1 = "Medicina"
        elif roleta_jogador1 == 3:
            curso_jogador1 = "Jogos Digitais"
        elif roleta_jogador1 == 4:
            curso_jogador1 = "Segurança da Informação"
        elif roleta_jogador1 == 5:
            curso_jogador1 = "Logística"
        else:
            curso_jogador1 = "Engenharia Mecanica"

    print("Curso do Jogador 1:", curso_jogador1)
    return curso_jogador1

    if posJogador2 == 5:
        jogador2Formado == True
        curso_jogador2 = "nada"

        if roleta_jogador2 == 1:
            curso_jogador2 = "Direito"
        elif roleta_jogador2 == 2:
            curso_jogador2 = "Medicina"
        elif roleta_jogador2 == 3:
            curso_jogador2 = "Jogos Digitais"
        elif roleta_jogador2 == 4:
            curso_jogador2 = "Segurança da Informação"
        elif roleta_jogador2 == 5:
            curso_jogador2 = "Logística"
        else:
            curso_jogador2 = "Ciências Contábeis"


    print("Curso do Jogador 2:", curso_jogador2)

#TEVE FILHO

def Filho():
    roleta = random.randint(1,6)
    if posJogador1 == 6 or posJogador1 == 9 or posJogador1 == 13:
        if roleta == 5:
            filhosJogador1 == 2
        else:
            filhosJogador1 == 1

    if posJogador2 == 6 or posJogador2 == 9 or posJogador2 == 13:
        if roleta == 5:
            filhosJogador2 == 2
        else:
            filhosJogador2 == 1

#CASOU

def Casar ():
    if posJogador1 == 7 or posJogador1 == 16:
        jogador1Casado == True

    if posJogador2 == 7 or posJogador2 == 16:
        jogador2Casado == True

#FAMOSO

def Famoso ():
    if posJogador1 == 15:
        jogador1Famoso == True

    if posJogador2 == 15:
        jogador2Famoso == True

#DIVORCIO

def Divorcio ():
    if posJogador1 == 12:
        jogador1Casado == False
        jogador1Divorciado == True

    if posJogador2 == 12:
        jogador2Casado == False
        jogador2Divorciado == True

#LOTERIA

def Loteria ():
    if posJogador1 == 14:
        roleta = random.randint(1,6)
        if roleta == 1:
            dinheiroJogador1 == dinheiroJogador1 + 2.5
        elif roleta == 2:
            dinheiroJogador1 == dinheiroJogador1 + 5000
        elif roleta == 3:
            dinheiroJogador1 == dinheiroJogador1 + 50000
        elif roleta == 4:
            dinheiroJogador1 == dinheiroJogador1 + 500000
        elif roleta == 5:
            dinheiroJogador1 == dinheiroJogador1 + 5000000
        elif roleta == 6:
            dinheiroJogador1 == dinheiroJogador1 + 100000000

    if posJogador2 == 14:
        roleta = random.randint(1,6)
        if roleta == 1:
            dinheiroJogador2 == dinheiroJogador2 + 2.5
        elif roleta == 2:
            dinheiroJogador2 == dinheiroJogador2 + 5000
        elif roleta == 3:
            dinheiroJogador2 == dinheiroJogador2 + 50000
        elif roleta == 4:
            dinheiroJogador2 == dinheiroJogador2 + 500000
        elif roleta == 5:
            dinheiroJogador2 == dinheiroJogador2 + 5000000
        elif roleta == 6:
            dinheiroJogador2 == dinheiroJogador2 + 100000000
    return dinheiroJogador1, dinheiroJogador2

#MAQUINA DO TEMPO

def Resetar():
    if posJogador1 == 20:
        jogador1Casado = False 
        jogador1Divorciado = False 
        jogador1Formado = False 
        jogador1Famoso = False 
        jogador1Vivo = True
        filhosJogador1 = 0
        dinheiroJogador1 = 0
        posJogador1 = 0
    
    if posJogador2 == 20:
        jogador2Casado = False 
        jogador2Divorciado = False 
        jogador2Formado = False 
        jogador2Famoso = False 
        jogador2Vivo = True
        filhosJogador2 = 0
        dinheiroJogador2 = 0
        posJogador2 = 0


















def main1():
    print()

    while jogador1Vivo == True:
        if jogador1Vivo == True:
            global turno
            global jogador
            Roleta()
            print(jogador)
            time.sleep(2)
            Dado()
            print(jogador)
            time.sleep(2)
            Morrer()
            print(jogador)
            time.sleep(2)
            DesafioMatematico()
            print(jogador)
            time.sleep(2)
            SeFormou()
            print(jogador)
            time.sleep(2)
            Filho()
            print(jogador)
            time.sleep(2)
            Casar()
            print(jogador)
            time.sleep(2)
            Famoso()
            print(jogador)
            time.sleep(2)
            Divorcio()
            print(jogador)
            time.sleep(2)
            Loteria()
            print(jogador)
            time.sleep(2)
            Resetar()
            print(jogador)
            time.sleep(2)
    
            


def main2():

    while jogador1Vivo == True and jogador2Vivo == True:
        if jogador1Vivo == True and jogador == posJogador1:
            global turno
            global jogador
            Roleta()
            posJogador1 = jogador
            Dado()
            posJogador1 = jogador
            Morrer()
            DesafioMatematico()
            SeFormou()
            Filho()
            Casar()
            Famoso()
            Divorcio()
            Loteria()
            Resetar()
            if perderodada == True:
                pass
            else:
                jogador = posJogador1

        
        if jogador2Vivo == True and jogador == posJogador2:
            global turno
            global jogador
            Roleta()
            posJogador2 = jogador
            Dado()
            posJogador2 = jogador
            Morrer()
            DesafioMatematico()
            SeFormou()
            Filho()
            Casar()
            Famoso()
            Divorcio()
            Loteria()
            Resetar()
            if perderodada == True:
                pass
            else:
                jogador = posJogador1

    
    print()

    while jogador1Vivo and jogador2Vivo:
        # jogador 1
        if jogador1Vivo:
            posJogador1 = Roleta(posJogador1)
            posJogador1 = Dado(posJogador1, jogadores)
            Morrer(1)
            # Chame outras funções para o jogador 1
        # jogador 2
        if jogadores == 2 and jogador2Vivo:
            posJogador2 = Roleta(posJogador2)
            posJogador2 = Dado(posJogador2, jogadores)
            Morrer(2)


#MAIN#
print()
jogadores = int(input("Digite aqui a quantidade de jogadores: "))
print()

if jogadores == 1:
    main1()

elif jogadores == 2:
    main2()


