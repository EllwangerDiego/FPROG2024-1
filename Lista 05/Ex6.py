#FUNCOES
import random
import time
import sys
y = 1
x = 3
ic = 9
ir = 2
il = 0

def novamente():
    y = 1
    time.sleep(1.5)

def encerrar():
    print("Encerrando o programa...")
    time.sleep(1.5)
    sys.exit()

def abrir():
    global x
    global ic
    global ir
    global il
    comum = random.randint(0,100)
    raro = random.randint(0,100)
    legend = random.randint(0,100)

    if comum <= 80:
        print("Você coletou 1 item comum!")
        ic = ic + 1
    else:
        x -= 1
        
    if raro <= 19:
        print("Você coletou 1 item raro!")
        ir = ir + 1
    else:
        x -= 1
        
    if legend == 1:
        print("Você coletou 1 item lendário!")
        il = il + 1

    else:
        x -= 1
    
    if x == 0:
        print("Você não coletou nada!")
    novamente()

def consultar():
    global ic
    global ir
    global il
    print("Itens comuns: {} ".format(ic))
    print("Itens raros: {} ".format(ir))
    print("Itens lendários: {} ".format(il))
    novamente()

def main():
    print()
    print("1) Abrir caixa ")
    print("2) Consultar itens ")
    print("3) Sair ")
    print()
    escolha = int(input("Digite aqui a opcao desejada: "))
    if escolha == 1:
        abrir()
    if escolha == 2:
        consultar()
    if escolha == 3:
        encerrar()

        
#MAIN
while y == 1:
    main()