import random

def inicializar_matriz(linhas, colunas):
    return [[" " for _ in range(colunas)] for _ in range(linhas)]

def imprimir_tabuleiro(matriz):
    print("  A B C D E F G H")
    for i, linha in enumerate(matriz):
        print(f"{i+1} {' '.join(linha)}")

def converter_coordenada(coordenada):
    coluna, linha = coordenada.split()
    return int(linha) - 1, ord(coluna.upper()) - ord('A')

def configurar_navios():
    controle = inicializar_matriz(8, 8)
    # Configuração fixa dos navios (para simplificação)
    navios = {
        'P': [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], # Porta-aviões
        'N': [(2, 0), (2, 1), (2, 2), (2, 3)],         # Navio de 4 canos
        'T': [(4, 0), (4, 1), (4, 2)],                 # Navio de 3 canos
        'D': [(6, 0), (6, 1)],                         # Navio de 2 canos
        'S': [(7, 7)]                                  # Submarino
    }
    for tipo, posicoes in navios.items():
        for x, y in posicoes:
            controle[x][y] = tipo
    return controle

def verificar_vitoria(controle):
    for linha in controle:
        if any(c in "PNTDS" for c in linha):
            return False
    return True

def main():
    controle = configurar_navios()
    exibicao = inicializar_matriz(8, 8)
    
    print("Tabuleiro de Jogo:")
    imprimir_tabuleiro(exibicao)
    
    while not verificar_vitoria(controle):
        coordenada = input("Digite a posição para atacar (ex: A 5): ")
        try:
            x, y = converter_coordenada(coordenada)
            if controle[x][y] in "PNTDS":
                print("Acertou um navio!")
                exibicao[x][y] = "X"
                controle[x][y] = " "
            else:
                print("Água!")
                exibicao[x][y] = "O"
            imprimir_tabuleiro(exibicao)
        except (ValueError, IndexError):
            print("Coordenada inválida, tente novamente.")
    
    print("Parabéns! Você afundou todos os navios!")

if __name__ == "__main__":
    main()
