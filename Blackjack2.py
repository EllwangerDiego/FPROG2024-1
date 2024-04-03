import time
import random


nome = "Luca"
fichas = 10
fichas = int(fichas)
baralho = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
winner = 0
winner = int(winner)
loser = 0
loser = int(loser)
aposta = 1
aposta = int(aposta)
question = " "




def introdução():

    pronto = " "

    nome = input("\n\nBem vindo ao jogo Black Jack, qual o seu nome? ")
    time.sleep(1)
    print("\nÉ um prazer ter você como nosso convidado! ")
    time.sleep(1)
    jogou = input("\n"+nome+", você já jogou esse jogo antes? ")

    jogou = jogou.upper()

    if jogou == "SIM":
        print("\nÓtimo, então vamos direto à diversão ")
        time.sleep(1)
    elif jogou == "NÃO":
        print("\nEntão vamos para as regras primeiro: ")
        time.sleep(2)
        print("\nComeçe dizendo quanto você quer apostar,\nvocê irá começar com 10 fichas,\nem cada jogada podera decidir\n quanto de risco quer tomar.")
        time.sleep(10)
        print("\nSeu objetivo, é claro, é sair com a maior quantidade de fichas que conseguir.")
        time.sleep(4)
        print("\nO jogo funciona da seguinte forma: \nNo blackjack, o objetivo é chegar o mais próximo possível de 21 sem ultrapassa-lo.\n Você joga contra a mesa e pode pedir mais cartas \ndepois das duas dadas à você inicialmente ou parar e \nver se você ganha da mesa com a mão que tem. \nSe suas cartas somarem mais que 21, você perde. \nSe somarem menos que as do dealer, você também perde.\n Se suas cartas somarem mais que as do dealer sem ultrapassar 21,você ganha! \nAlém disso o Ás pode valer 1 ou 11 e cartas acima de 10 valem como 10.")
        pronto = input("Digite 'pronto' quando quiser continuar: ")
        time.sleep(1)
    return nome



def inicio_jogo():
    
    
    A = random.choice (baralho)
    B = random.choice(baralho)
    C = random.choice(baralho)
    D = random.choice(baralho)
    E = ""
    F = ""
    G = ""
    H = ""

    if A == "A":
        E = 11 
    elif A == "2":
        E = 2
    elif A == "3":
        E = 3
    elif A == "4":
        E = 4
    elif A == "5":
        E = 5
    elif A == "6":
        E = 6
    elif A == "7":
        E = 7
    elif A == "8":
        E = 8
    elif A == "9":
        E = 9
    elif A == "10":
        E = 10
    elif A == "J":
        E = 10
    elif A == "Q":
        E = 10
    elif A == "K":
        E = 10



    if B == "A":
        F = 11 
    elif B == "2":
        F = 2
    elif B == "3":
        F = 3
    elif B == "4":
        F = 4
    elif B == "5":
        F = 5
    elif B == "6":
        F = 6
    elif B == "7":
        F = 7
    elif B == "8":
        F = 8
    elif B == "9":
        F = 9
    elif B == "10":
        F = 10
    elif B == "J":
        F = 10
    elif B == "Q":
        F = 10
    elif B == "K":
        F = 10


    if C == "A":
        G = 11 
    elif C == "2":
        G = 2
    elif C == "3":
        G = 3
    elif C == "4":
        G = 4
    elif C == "5":
        G = 5
    elif C == "6":
        G = 6
    elif C == "7":
        G = 7
    elif C == "8":
        G = 8
    elif C == "9":
        G = 9
    elif C == "10":
        G = 10
    elif C == "J":
        G = 10
    elif C == "Q":
        G = 10
    elif C == "K":
        G = 10

    
    if D == "A":
        H = 11 
    elif D == "2":
        H = 2
    elif D == "3":
        H = 3
    elif D == "4":
        H = 4
    elif D == "5":
        H = 5
    elif D == "6":
        H = 6
    elif D == "7":
        H = 7
    elif D == "8":
        H = 8
    elif D == "9":
        H = 9
    elif D == "10":
        H = 10
    elif D == "J":
        H = 10
    elif D == "Q":
        H = 10
    elif D == "K":
        H = 10


    while 1 == 1: 
        xyz = int(input("\nQuantas fichas você vai apostar? "))
        if xyz > fichas:
            print("\nVocê não  tem fichas o suficiente")
        else:
            break  
    time.sleep(1)
    print("\nPreparando o jogo...")
    time.sleep(3)
    print("\n||-----------------------||")
    print("Suas cartas são: "+A+" e "+B)
    print("A soma de suas cartas é "+str(E+F)+".")
    print("||-----------------------||")
    time.sleep(2)
    print("\n||-----------------------||")
    print("As cartas da mesa são: "+C+" e "+D)
    print("A mesa está com "+str(G+H)+".")
    print("||-----------------------||")
    return E,F,G,H,xyz,A,B,C,D



def meio_do_jogo(EFGH):
    
    mamamia = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    mamamias = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
    mesa = EFGH[2]+EFGH[3] 
    mesa = int(mesa)
    pessoa = EFGH[0]+EFGH[1]
    pessoa = int(pessoa)

    for i in range(5,10):
        resposta = input("\n"+nome+", você gostaria de mais uma carta? ")
        resposta = resposta.upper()
        if resposta == "NÃO":
            for j in range(5,10):
                if mesa <17:
                    print("Embaralhando...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    mamamias[j] = random.choice(baralho)
                    T = 5
                    if mamamias[j] == "A":
                        T = 11 
                    elif mamamias[j] == "J":
                        T = 10
                    elif mamamias[j] == "Q":
                        T = 10
                    elif mamamias[j] == "K":
                        T = 10
                    else: 
                        mamamias[j] = T
                    mesa = mesa + T
                    print("\n||------------------------------||")
                    print("As cartas da mesa são "+str(EFGH[7])+"  "+str(EFGH[8])+"  "+ str(mamamias[5])+"  "+ str(mamamias[6])+" "+ str(mamamias[7])+" "+ str(mamamias[8]))
                    if mesa > 21:
                        if EFGH[2] == 11:
                            mesa -= 10
                        if EFGH[3] == 11:
                            mesa -= 10
                        if mamamias[5] == "A":
                            mesa -= 10
                        if mamamias[6] == "A":
                            mesa -= 10
                        if mamamias [7] == "A":
                            mesa -= 10
                        if mamamias [8] == "A":
                            mesa -= 10
                    print("A soma da mesa é " +str(mesa)+ "." )
                    print("||------------------------------||")
                    if mesa > 21:
                        return "Pessoa"
                else:
                     if mesa > pessoa and mesa <22:
                        return "Mesa"
                     elif pessoa > mesa and pessoa <22:
                        return "Pessoa"
                     else:
                        return "Empate"




        else:
            print("Embaralhando...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            mamamia[i] = random.choice(baralho)
            T = 5
            if mamamia[i] == "A":
                T = 11 
            elif mamamia[i] == "J":
                T = 10
            elif mamamia[i] == "Q":
                T = 10
            elif mamamia[i] == "K":
                T = 10
            else: 
                mamamia[i] = T
            pessoa = pessoa + T
            print("\n||------------------------------||")
            print("Suas cartas são: "+str(EFGH[5])+"  "+str(EFGH[6])+"  "+ str(mamamia[5])+"  "+ str(mamamia[6])+"  "+ str(mamamia[7])+"  "+ str(mamamia[8]))
            if pessoa > 21:
                if EFGH[0] == 11:
                    pessoa -= 10
                if EFGH[1] == 11:
                    pessoa -= 10
                if mamamia[5] == "A":
                    pessoa -= 10
                if mamamia[6] == "A":
                    pessoa -= 10
                if mamamia [7] == "A":
                    pessoa -= 10
                if mamamia [8] == "A":
                    pessoa -= 10
            print("A soma delas é " +str(pessoa)+ "." )
            print("||------------------------------||")
            if pessoa > 21: 
                return "Mesa"
                break
            
        

nome = introdução()

while 1 == 1:
    EFGH = inicio_jogo()
    EFGH = list(EFGH)
    EFGH[4] = int(EFGH[4])
    aposta = EFGH[4]
    cha = meio_do_jogo(EFGH)
    if cha == "Mesa":
        fichas -= aposta
        time.sleep(1)
        print("\n---------------------------")
        print("A Mesa ganhou! Você tem "+str(fichas)+ " fichas.")
        print("---------------------------")
    elif cha == "Pessoa" :
        fichas += aposta
        time.sleep(1)
        print("\n---------------------------")
        print("Você ganhou! Você tem "+str(fichas)+ " fichas.")
        print("---------------------------")
    else:
        print("\n---------------------------")
        print("Empate! Você tem "+str(fichas)+ " fichas.")
        print("---------------------------")
    if fichas == 0:
        time.sleep(1)
        print("---------------------------")
        print("Você perdeu tudo, até a próxima")
        print("---------------------------")
        break
    else:
        time.sleep(3)
        question = input("\nGostaria de jogar novamente?")
        question = question.upper()
        if question == "NÃO":
            print("\nBoa escolha, você leva para casa "+str(fichas)+" fichas. Até a próxima.\n\n\n\n")
            break

#(EFGH[0])