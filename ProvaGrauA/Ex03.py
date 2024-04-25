
#DEFININDO VARIAVEIS PARA A QUANTIDADE DE INGREDIENTES DISPONIVEIS

pf = 100
pfv = True
ec = 50
ecv = True
rd = 45
rdv = True
ol = 30
fs = 200
fsv = True
ea = 20
eav = True
lu = 15
luv = True
import time

print()
print("BOA TARDE!")
x = 0
while x == 0:
    time.sleep(3)
    print()
    print()
    print("|----------------------------------------------|")
    print("|                                              | ") 
    print("|             O que você deseja?               | ") 
    print("|                                              | ") 
    print("|    1) Preparar poção                         | ")              
    print("|    2) Consultar os ingredientes disponíveis  |")
    print("|    3) Sair                                   |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print()
    print()
    cont = 0
    opcao = 0
    p = 0
    while p == 0:
        opcao = int(input("Digite aqui a opção que você deseja: "))
        if opcao == 1:
            print()
            print()
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|  OPÇÃO    |   POÇÃO                       |   INGREDIENTES                        |")
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|     1     |   Poção de Cura               |   Pó de Fênix (30g)                   |")
            print("|           |                               |   Essência Celestial (20 ml)          |")
            print("|           |                               |   Flores secas (20g)                  |")
            print("|           |                               |   Lágrimas de unicórnio (10 ml)       |")
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|     2     |   Poção Força da Floresta     |   Orvalho Lunar (20 ml)               |")
            print("|           |                               |   Raiz de Dragão (30g)                |")
            print("|           |                               |   Flores secas (30g)                  |")            
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|     3     |  Poção Sabedoria da Riqueza   |   Essência Celestial (30 ml)          |")
            print("|           |                               |   Pó de Fênix (50g)                   |")
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|     4     |   Poção Sorte no Amor         |   Orvalho Lunar (10 ml)               |")
            print("|           |                               |   Flores secas (50g)                  |")
            print("|           |                               |   Lágrimas de unicórnio (5 ml)        |") 
            print("|-----------|-------------------------------|---------------------------------------|")
            print("|     5     |   Poção Malvada               |   Elixir amargo (10 ml)               |")
            print("|           |                               |   Raiz de Dragão (15g)                |")
            print("|---------- |-------------------------------|---------------------------------------|")
            print()
            opcao2 = int(input("Digite aqui a opção da poção que você deseja fazer: "))
            print()

#OPCAO 1
            if opcao2 == 1:
            
                cont = 10
                if pf >= 30 and ec >= 20 and fs >= 20 and lu >= 10: 
                    pf = pf - 30 
                    ec = ec - 20
                    fs = fs - 20
                    lu = lu - 10
                    print("Poção criada com sucesso! ")

                elif pf < 30:
                    print("Você não possui a quantidade de Pó de Fênix necessária ")
                    pfv = False
                    print()
                    
                elif ec < 20: 
                    print("Você não possui a quantidade de Essência Celestial necessária ")
                    ecv = False
                    print()
                    
                elif fs < 20:
                    print("Você não possui a quantidade de Flores secas necessária ")
                    fsv = False
                    print()
                    
                elif lu < 10:
                    print("Você não possui a quantidade de Lágrimas de unicórnio necessária ")
                    luv = False
                    print()

                p = 1 
#OPCAO 2
            elif opcao2 == 2:
            
                cont = 10
                if ol >= 20 and rd >= 30 and fs >= 30: 
                    ol = ol - 20 
                    rd = rd - 30
                    fs = fs - 30
                    print("Poção criada com sucesso! ")
            

                elif ol < 20:
                    print("Você não possui a quantidade de Orvalho Lunar necessária ")
                    olv = False
                    print()
                    
                elif rd < 30: 
                    print("Você não possui a quantidade de Raiz de Dragão necessária ")
                    rdv = False
                    print()
                    
                elif fs < 30:
                    print("Você não possui a quantidade de Flores secas necessária ")
                    fsv = False
                    print()
                    
                
                p = 1 

#OPCAO 3
            elif opcao2 == 3:
                cont = 10
                if ec >= 30 and pf >= 50: 
                    ec = ec - 30 
                    pf = pf - 50
                    print("Poção criada com sucesso! ")
                    
            

                elif ec < 30:
                    print("Você não possui a quantidade de Essência Celestial necessária ")
                    ecv = False
                    print()
                    
                elif pf < 50: 
                    print("Você não possui a quantidade de Pó de Fênix necessária ")
                    pfv = False
                    print()
                    
                
                p = 1 
#OPCAO 4                    
            elif opcao2 == 4:
                cont = 10
                if ol >= 10 and fs >= 50 and lu >= 5: 
                    ol = ol - 10 
                    fs = fs - 50
                    lu = lu - 5
                    print("Poção criada com sucesso! ")
            

                elif ol < 10:
                    print("Você não possui a quantidade de Orvalho Lunar necessária ")
                    olv = False
                    print()
                    
                elif fs < 50: 
                    print("Você não possui a quantidade de Flores secas necessária ")
                    fsv = False
                    print()
                    
                elif lu < 5:
                    print("Você não possui a quantidade de Lágrimas de unicórnio necessária ")
                    luv = False
                    print()
                    
                
                p = 1           
#OPCAO 5
            elif opcao2 == 5:
                cont = 10
                if ea >= 10 and rd >= 15: 
                    ea = ea - 10 
                    rd = rd - 15
                    print("Poção criada com sucesso! ")
                    
            

                elif ea < 10:
                    print("Você não possui a quantidade de Elixir amargo necessária ")
                    eav = False
                    print()
                    
                elif rd < 15: 
                    print("Você não possui a quantidade de Raiz de Dragão necessária ")
                    rdv = False
                    print()
                    
                
                p = 1 




        elif opcao == 2:
            print()
            print("|----------------------------|----------------|")
            print("|   INGREDIENTES             |   QUANTIDADE   |")
            print("|----------------------------|----------------|")
            print("|   Pó de Fênix              |   ",pf, "g       |")
            print("|----------------------------|----------------|")
            print("|   Essência Celestial       |   ",ec,"ml       |")
            print("|----------------------------|----------------|")
            print("|   Raiz de Dragão           |   ",rd,"g        |")
            print("|----------------------------|----------------|")
            print("|   Orvalho Lunar            |   ",ol,"ml       |")
            print("|----------------------------|----------------|")
            print("|   Flores secas             |   ",fs,"g       |")
            print("|----------------------------|----------------|")
            print("|   Elixir amargo            |   ",ea," ml      |")
            print("|----------------------------|----------------|")
            print("|   Lágrimas de unicórnios   |   ",lu," ml      |")
            print("|----------------------------|----------------|")
            print()
            x = 0
            p = 1
            
        elif opcao == 3:
            print()
            print("Encerrando o programa")
            print()
            x = 1
            p = 1

