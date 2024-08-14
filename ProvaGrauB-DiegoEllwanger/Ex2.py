import random
import time
import sys 

x = 0

def gerarToupeiras():
    v = [
        ['-', "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"]
    ]
    
    #Criando uma variavel modificavel para guardar as casas escolhidas e futuramente, utiliza-la para nao cair 2 toupeiras na mesma casa
    escolhidas = []
    
    #Aqui vou escolher as 4 casas aleatorias e troca-las por "T", e com a variavel "escolhidas", vou identificar se ja foi escolhida ou nao essa posicao,
    #para nao ter 2 toupeiras no mesmo lugar

    for _ in range(4):
        while True:
            linha = random.randint(0, 3)
            coluna = random.randint(0, 3)
            if (linha, coluna) not in escolhidas:
                escolhidas.append((linha, coluna))
                break
        
        v[linha][coluna] = "T"
    
    #Aqui estou imprimindo a matriz, e adicionando um espacamento entre os "-" ou "T"
    print()
    print("Mapa das Toupeiras: ")
    print()
    for linha in v:
        for elemento in linha:
            print(elemento + " ", end="")
        print()
    print()

# Iniciando o programa, fazendo com que o usuario tenha que escolher se deseja gerar toupeiras ou fechar o programa
print()
print("BOA TARDE!")
time.sleep(3)
print()
def main():
    print()
    print("|----------------------------------------------|")
    print("|                                              | ") 
    print("|             O que você deseja?               | ") 
    print("|                                              | ") 
    print("|    1) Gerar Toupeiras                        | ")              
    print("|    2) Sair                                   |")
    print("|                                              |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print()
    print()

    decisao = int(input("Digite aqui a opção que você deseja: "))
    if decisao == 1:
        gerarToupeiras()
        time.sleep(5)
        main()
    if decisao == 2:
        time.sleep(1)
        print("Encerrando o programa...")
        time.sleep(3)
        sys.exit
    if decisao != 1 and decisao !=2:
        print()
        print("Digite 1 ou 2 para a opcao desejada!")
        time.sleep(3)
        main()

main()
        




