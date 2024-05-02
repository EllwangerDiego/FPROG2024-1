import random
import time
import sys

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

perderodada = False



#FUNCOES


#ROLETA

def Roleta():
    global jogador
    roleta = random.randint(1, 6)
    jogador = jogador + roleta
    print("Girou a roleta e saiu o numero {}".format(roleta))
    time.sleep(1.5)
    return jogador



#Dado

def Dado():
    global jogador
    global turno
    global posJogador1
    global posJogador2
    global perderodada
    
    if jogador == 1 or jogador == 3 or jogador == 10 or jogador == 17:
        print()
        print("Dado: Vai ser girada outra roleta, se cair o numero 1, o jogador anda mais 1 casa; Se cair o numero 3, o jogador volta 1 casa; ")
        print("E se cair o numero 6, o jogador perde uma rodada.")
        print()
        time.sleep(10)
        roleta = random.randint(1, 6)
        if roleta == 1:
            print()
            print("Caiu o numero 1, o jogador agora esta na casa", jogador)
            print()
            jogador = min(jogador + 1, 21) 
        elif roleta == 3:
            print()
            print("Caiu o numero 3, o jogador agora esta na casa", jogador)
            print()
            jogador = max(jogador - 1, 0) 
        elif roleta == 6 and jogadores == 2:
            print()
            print("Caiu o numero 6, o jogador perde uma rodada")
            print()
            perderodada = True
            jogador = "Perdeu uma rodada"
        else:
            print()
            print(roleta, "foi o numero sorteado, nao acontece nada")
            print()
            time.sleep(5)

            
    return jogador
    

#Morreu

def Morrer():
    global jogador
    global turno
    global jogador1Vivo, jogador2Vivo, posJogador1, posJogador2
    if jogador == 2 or jogador == 8 or jogador == 18: 
        if jogador == posJogador1:
            jogador1Vivo = False 
            print()
            print ("O Jogador 1 morreu :( ")
            print()
            print(" O Jogador 2 venceu!!!!")
            print("")
            print("Encerrando o jogo...")
            time.sleep(2)
            sys.exit()

            
        elif jogador == posJogador2:
            jogador2Vivo = False 
            print()
            print ("O Jogador 2 morreu :( ")
            print()
            print(" O Jogador 1 venceu!!!!")
            print("")
            print("Encerrando o jogo...")
            time.sleep(2)
            sys.exit()
            


#DESAFIO MATEMATICO

def DesafioMatematico():
    global turno
    global posJogador1
    global posJogador2

    
    time.sleep(2.5)
    if jogador == 4 or jogador == 11 or jogador == 19:
        print ("O jogador caiu na casa {}, ""Desafio Matematico,"" o que significa que vai ser girado outra roleta".format(jogador))
        print ("Se cair o numero 1, vai ser motrado na tela os numeros primos ate 100;")
        print ("Se cair o numero 2, vai ser feito o somatorio dos numeros de 1 ate 10;")
        print ("Se cair o numero 3, vai ser mostrado a serie de Fibonacci ate o decimo elemento")
        print ("Se cair o numero 4, vai ser calculado e mostrado a area de um circulo com raio 2.5")
        print ("Se cair o numero 5, vai ser mostrado o fatorial do numero 5")
        print ("Se cair o numero 6, Vai ser mostrado os 5 primeiros numeros divisiveis por 2 e por 5")
        time.sleep(30)
        print()
        print("Girando a roleta...")
        roleta = random.randint(1, 6)

        print()
        print("A roleta foi girada e caiu o numero {}".format(roleta))
        print()
        time.sleep (1.5)
        
        if roleta == 1:
            #primos ate 100
            print("| 2 | 3 | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 | 37 | 41 |")
            print("|------------------------------------------------------------|")
            print("|43 | 47 | 53 | 59 | 61 | 67 | 71 | 73 | 79 | 83 | 89 | 97   |")


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
    global jogador
    global posJogador2
    global posJogador1
    global curso_jogador1
    global curso_jogador2
    global jogador1Formado
    global jogador2Formado

    if jogador == 5 and jogador == posJogador1:
        print("O jogador 1 caiu na casa 5, o que significa que vai ser girado uma roleta para os 6 possiveis valores.")
        time.sleep(2.5)
        print("1) Direito")
        time.sleep(1.5)
        print("2) Medicina")
        time.sleep(1.5)
        print("3) Jogos Digitais")
        time.sleep(1.5)
        print("4) Segurança da Informação")
        time.sleep(1.5)
        print("5) Logística")
        time.sleep(1.5)
        print("6) Engenharia Mecanica")
        time.sleep(1.5)
        print()
        print("Girando a roleta...")
        print()
        roleta_jogador1 = random.randint(1, 6)
        print("A roleta foi girada e caiu no numero {}".format(roleta_jogador1))

        print()
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
        print()
        time.sleep(2)
        

    if posJogador2 == 5 and jogador == posJogador2:
        print("O jogador 2 caiu na casa 5, o que significa que vai ser girado uma roleta para os 6 possiveis valores.")
        time.sleep(2.5)
        print("1) Direito")
        time.sleep(1.5)
        print("2) Medicina")
        time.sleep(1.5)
        print("3) Jogos Digitais")
        time.sleep(1.5)
        print("4) Segurança da Informação")
        time.sleep(1.5)
        print("5) Logística")
        time.sleep(1.5)
        print("6) Engenharia Mecanica")
        time.sleep(1.5)
        print()
        print("Girando a roleta...")
        roleta_jogador2 = random.randint(1, 6)
        print()
        roleta_jogador2 = random.randint(1, 6)
        print("A roleta foi girada e caiu no numero {}".format(roleta_jogador2))
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
            curso_jogador2 = "Engenharia Mecanica"
        print("Curso do Jogador 2:", curso_jogador2)

    return curso_jogador1, curso_jogador2


#FILHOS

def Filho():
    global filhosJogador1
    global filhosJogador2
    global jogador
    global posJogador1
    global posJogador2
    
    if posJogador1 == 6 or posJogador1 == 9 or posJogador1 == 13:
        print()
        print("O jogador 1 caiu na casa {}, o que significa que ele teve um filho! Porem, vai ser girado uma roleta, se cair no numero 5, eles sao gemeos!!".format(posJogador1))
        print()
        time.sleep(5)
        print("Girando a roleta...")
        time.sleep(1.5)
        print()
        roleta = random.randint(1,6)
        print("A roleta foi girada e caiu no numero {}".format(roleta))
        time.sleep(2)
        print()
        if roleta == 5:
            filhosJogador1 == 2
            print()
            print("O Jogador 1 agora tem 2 filhos!!!")
            print()
        else:
            filhosJogador1 == 1
            print()
            print("O Jogador 1 agora tem 1 filho!!!")
            print()

    if posJogador2 == 6 or posJogador2 == 9 or posJogador2 == 13:
        print()
        print("O jogador 2 caiu na casa {}, o que significa que ele teve um filho! Porem, vai ser girado uma roleta, se cair no numero 5, eles sao gemeos!!".format(posJogador2))
        print()
        time.sleep(5)
        print("Girando a roleta...")
        time.sleep(1.5)
        print()
        roleta = random.randint(1,6)
        print("A roleta foi girada e caiu no numero {}".format(roleta))
        time.sleep(2)
        print()
        if roleta == 5:
            filhosJogador2 == 2
            print()
            print("O jogador 2 agora tem 2 filhos!!!")
            print()
        else:
            filhosJogador2 == 1
            print()
            print("O Jogador 2 agora tem 1 filho!!!")
            print()
    time.sleep(3)

    return filhosJogador1, filhosJogador2


#CASAR

def Casar ():
    global jogador1Casado
    global jogador2Casado
    global jogador
    global posJogador1
    global posJogador2
    time.sleep(2)

    if posJogador1 == 7 or posJogador1 == 16:
        print()
        print("O jogador 1 caiu na casa {} e se casou!!!".format(posJogador1))
        print()
        jogador1Casado == True

    if posJogador2 == 7 or posJogador2 == 16:
        print()
        print("O jogador 2 caiu na casa {} e se casou!!!".format(posJogador2))
        print()
        jogador2Casado == True
    time.sleep(2)


#FAMOSO

def Famoso ():
    if posJogador1 == 15:
        jogador1Famoso == True
        print()
        print("O jogador 1 caiu na casa 15 e agora virou um famoso!!!")
        print()
        time.sleep(2)
        

    if posJogador2 == 15:
        jogador2Famoso == True
        print()
        print("O jogador 2 caiu na casa 15 e agora virou um famoso!!!")
        print()
        time.sleep(2)


#DIVORCIO

def Divorcio ():
    if posJogador1 == 12 and jogador1Casado == True:
        jogador1Casado == False
        jogador1Divorciado == True
        print()
        print("O Jogador 1 caiu na casa 15 e divorciou-se :( ")
        print()
        time.sleep(2)

    if posJogador2 == 12 and jogador2Casado == True:
        jogador2Casado == False
        jogador2Divorciado == True
        print()
        print("O Jogador 2 caiu na casa 15 e divorciou-se :( ")
        print()
        time.sleep(2)

    elif posJogador2 == 12 and jogador2Casado == False:
        print()
        print("O jogador 2 nao eh casado, entao nao acontece nada")
        print()
        time.sleep(2)

    elif posJogador1 == 12 and jogador1Casado == False:
        print()
        print("O jogador 1 nao eh casado, entao nao acontece nada")
        print()
        time.sleep(2)

#LOTERIA

def Loteria ():
    global dinheiroJogador2
    global dinheiroJogador1
    if posJogador1 == 14:
        print()
        print("O jogador 1 ganhou na loteria!!!!")
        time.sleep(2)
        print("Vai ser girado uma roleta, e seu status sera atualizado de acordo com o numero que tirar")
        print()
        print("1) R$ 2,50")
        print("2) R$ 5.000,00")
        print("3) R$ 50.000,00")
        print("4) R$ 500.000,00")
        print("5) R$ 5.000.000,00")
        print("6) R$ 100.000.000,00")
        print()
        time.sleep(10)
        print("Girando a roleta...")
        print()
        time.sleep(2)
        roleta = random.randint(1,6)
        print("O numero sorteado foi {}".format(roleta))
        print()
        
        if roleta == 1:
            dinheiroJogador1 = dinheiroJogador1 + 2.5
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)
        elif roleta == 2:
            dinheiroJogador1 = dinheiroJogador1 + 5000
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)
        elif roleta == 3:
            dinheiroJogador1 = dinheiroJogador1 + 50000
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)
        elif roleta == 4:
            dinheiroJogador1 = dinheiroJogador1 + 500000
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)
        elif roleta == 5:
            dinheiroJogador1 = dinheiroJogador1 + 5000000
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)
        elif roleta == 6:
            dinheiroJogador1 = dinheiroJogador1 + 100000000
            print("O Jogador 1 agora tem R$ ", dinheiroJogador1)
            print()
            time.sleep(3)

    if posJogador2 == 14:
        print()
        print("O jogador 2 ganhou na loteria!!!!")
        time.sleep(2)
        print("Vai ser girado uma roleta, e seu status sera atualizado de acordo com o numero que tirar")
        print()
        print("1) R$ 2,50")
        print("2) R$ 5.000,00")
        print("3) R$ 50.000,00")
        print("4) R$ 500.000,00")
        print("5) R$ 5.000.000,00")
        print("6) R$ 100.000.000,00")
        print()
        time.sleep(10)
        print("Girando a roleta...")
        print()
        time.sleep(2)
        roleta = random.randint(1,6)
        print("O numero sorteado foi {}".format(roleta))
        print()
        
        if roleta == 1:
            dinheiroJogador2 = dinheiroJogador2 + 2.5
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
        elif roleta == 2:
            dinheiroJogador2 = dinheiroJogador2 + 5000
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
        elif roleta == 3:
            dinheiroJogador2 = dinheiroJogador2 + 50000
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
        elif roleta == 4:
            dinheiroJogador2 = dinheiroJogador2 + 500000
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
        elif roleta == 5:
            dinheiroJogador2 = dinheiroJogador2 + 5000000
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
        elif roleta == 6:
            dinheiroJogador2 = dinheiroJogador2 + 100000000
            print("O Jogador 2 agora tem R$ ", dinheiroJogador2)
            print()
            time.sleep(3)
    return dinheiroJogador1, dinheiroJogador2


#MAQUINA DO TEMPO

def Resetar():
    global jogador
    global jogador1Casado
    global jogador1Divorciado 
    global jogador1Formado 
    global jogador1Famoso 
    global jogador1Vivo 
    global filhosJogador1 
    global dinheiroJogador1 
    global posJogador1 

    
    global jogador2Casado
    global jogador2Divorciado 
    global jogador2Formado 
    global jogador2Famoso 
    global jogador2Vivo 
    global filhosJogador2 
    global dinheiroJogador2 
    global posJogador2 

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
            global posJogador1
            global posJogador2
            print("Vai ser girado a roleta...")
            time.sleep(1.5)
            Roleta()
            print()
            print("O Jogador 1 agora esta na casa", jogador)
            print()
            time.sleep(1.5)
            posJogador1 = jogador
            time.sleep(2)
            if jogador == 1 or jogador == 3 or jogador == 10 or jogador == 17:
                Dado()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 2 or jogador == 8 or jogador == 18:
                Morrer()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 4 or jogador == 11 or jogador == 19:
                DesafioMatematico()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 5:
                SeFormou()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 6 or jogador == 9 or jogador == 13:
                Filho()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 7 or jogador == 16:
                Casar()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 15:
                Famoso()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 12:
                Divorcio()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 14: 
                Loteria()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 20:
                Resetar()
                posJogador1 = jogador
            

def main2():
    global turno
    global jogador
    global posJogador1
    global posJogador2
    global perderodada

    while jogador1Vivo == True and jogador2Vivo == True:
        if jogador1Vivo == True and jogador == posJogador1:
            print()
            print("--------JOGADOR 1 --------")
            print()
            print("Vai ser girado a roleta...")
            time.sleep(1.5)
            Roleta()
            print()
            print("O Jogador 1 agora esta na casa", jogador)
            print()
            time.sleep(1.5)
            posJogador1 = jogador
            time.sleep(2)
            if jogador == 1 or jogador == 3 or jogador == 10 or jogador == 17:
                Dado()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 2 or jogador == 8 or jogador == 18:
                Morrer()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 4 or jogador == 11 or jogador == 19:
                DesafioMatematico()
                posJogador1 = jogador
                
                time.sleep(2)
            elif jogador == 5:
                SeFormou()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 6 or jogador == 9 or jogador == 13:
                Filho()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 7 or jogador == 16:
                Casar()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 15:
                Famoso()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 12:
                Divorcio()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 14: 
                Loteria()
                posJogador1 = jogador

                time.sleep(2)
            elif jogador == 20:
                Resetar()
                posJogador1 = jogador

            if posJogador1 > 20:
                print()
                print("O Jogador 1 VENCEU!!!")
                print()
                time.sleep(5)
                print("Encerrando o programa...")
                sys.exit
            
            if perderodada == True:
                pass
            else:
                jogador = posJogador2

        
        if jogador2Vivo == True and jogador == posJogador2:
            print()
            print("--------JOGADOR 2 --------")
            print()
            print("Vai ser girado a roleta...")
            time.sleep(1.5)
            Roleta()
            print()
            print("O Jogador 2 agora esta na casa", jogador)
            print()
            time.sleep(1.5)
            posJogador2 = jogador
            time.sleep(2)
            if jogador == 1 or jogador == 3 or jogador == 10 or jogador == 17:
                Dado()
                posJogador2 = jogador
                
                time.sleep(2)
            elif jogador == 2 or jogador == 8 or jogador == 18:
                Morrer()
                posJogador2 = jogador
                
                time.sleep(2)
            elif jogador == 4 or jogador == 11 or jogador == 19:
                DesafioMatematico()
                posJogador2 = jogador
                
                time.sleep(2)
            elif jogador == 5:
                SeFormou()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 6 or jogador == 9 or jogador == 13:
                Filho()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 7 or jogador == 16:
                Casar()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 15:
                Famoso()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 12:
                Divorcio()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 14: 
                Loteria()
                posJogador2 = jogador

                time.sleep(2)
            elif jogador == 20:
                Resetar()
                posJogador2 = jogador

            if posJogador2 > 20:
                print()
                print("O Jogador 2 VENCEU!!!")
                print()
                time.sleep(5)
                print("Encerrando o programa...")
                sys.exit
            
            if perderodada == True:
                pass
            else:
                jogador = posJogador1



#MAIN#
print()
jogadores = int(input("Digite aqui a quantidade de jogadores: "))
print()

if jogadores == 1:
    main1()

elif jogadores == 2:
    main2()