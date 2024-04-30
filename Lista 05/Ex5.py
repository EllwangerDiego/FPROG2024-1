x = 1
import time
def somar():
    print()
    n1 = float(input("Digite aqui um numero: "))
    print()
    n2 = float(input("Digite outro numero para somar: "))
    print()
    nf = n1 + n2
    print("{} + {} == {}".format(n1,n2,nf))
    print()
        
def subtrair():
    print()
    n1 = float(input("Digite aqui um numero: "))
    print()
    n2 = float(input("Digite outro numero para subtrair: "))
    print()
    nf = n1 - n2
    print("{} - {} == {}".format(n1,n2,nf))
    print()

def multiplicar():
    print()
    n1 = float(input("Digite aqui um numero: "))
    print()
    n2 = float(input("Digite outro numero para multiplicar: "))
    print()
    nf = n1 * n2
    print("{} X {} == {}".format(n1,n2,nf))
    print()

def dividir():
    print()
    n1 = float(input("Digite aqui um numero: "))
    print()
    n2 = float(input("Digite outro numero para dividir: "))
    print()
    if n2 == 0:

        print("ERRO")
    else:
        nf = n1 / n2
        print("{} / {} = {}".format(n1,n2,nf))
        print()

def escolha():
    global x
    escolha = input("Voce deseja realizar outra operacao? (S/N) ")
    if escolha == "S" or escolha == "s":
        x = 1
        main()
    if escolha == "N" or escolha == "n":
        x = 0
    
    
def main():
    global x       
    while x == 1:
        print()
        print("1) Somar")
        print("2) Subtrair")
        print("3) Multiplicar")
        print("4) Dividir")
        print()
        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1 or opcao == "somar" or opcao == "Somar":
            somar()
            print()
            escolha()

        elif opcao ==2 or opcao =="subtrair" or opcao == "Subtrair":
            subtrair()
            print()
            escolha()

        elif opcao == 3 or opcao == "multiplicar" or opcao == "Multiplicar":
            multiplicar()
            print()
            escolha()

        elif opcao ==4 or opcao == "Dividir" or opcao == "dividir":
            dividir()
            print()
            escolha()


main()
if x == 0:
    print()
    print("Encerrando o programa...")
    time.sleep(1.5)

