import csv
import time
import sys

def filtrar_por_periodo(linhas, indice_data, ano_inicio, ano_fim):
    filtrados = []
    for linha in linhas[1:]:
        data_str = linha[indice_data].strip()
        if data_str != '-' and data_str != '':
            try:
                dia, mes, ano = map(int, data_str.split('/'))
                if ano_inicio <= ano <= ano_fim:
                    filtrados.append(linha)
            except ValueError:
                continue
    return filtrados

def exibir_tabela_formatada(linhas):
    if not linhas or len(linhas) == 1:
        print("Nenhum dado encontrado.")
        return

    largura_num = len(str(len(linhas))) + 2
    
    # Calcula a largura máxima de cada coluna
    colunas_largura = [max(len(str(valor)) for valor in coluna) for coluna in zip(*linhas)]

    # Formata o cabeçalho
    cabecalho = linhas[0]
    cabecalho_formatado = f"{'   ':<{largura_num}} " + "  ".join(f"{valor:{colunas_largura[i]}}" for i, valor in enumerate(cabecalho))
    print(cabecalho_formatado)

    # Formata cada linha de dados
    for i, linha in enumerate(linhas[1:], start=1):
        linha_formatada = f"{i:<{largura_num}} " + "  ".join(f"{valor:{colunas_largura[j]}}" for j, valor in enumerate(linha))
        print(linha_formatada)

def filtragem_dados(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=',')
        linhas = list(arquivo_csv)
    
    while True:
        print()
        print("Escolha a opção de filtragem:")
        print("1) Consultar gatos resgatados por período")
        print("2) Consultar gatos adotados por período")
        print("0) Sair")
        print()
        opcao = input("Digite a opção desejada: ")

        if opcao == '0':
            break
        if opcao != '1' and opcao != '2':
            print("Opção inválida. Tente novamente.")
            continue

        ano_inicio = int(input("Digite o ano de início: "))
        ano_fim = int(input("Digite o ano de fim: "))
        
        if opcao == '1':
            indice_data_resgate = linhas[0].index("Data Resgate")
            filtrados = filtrar_por_periodo(linhas, indice_data_resgate, ano_inicio, ano_fim)
            print("\nGatos resgatados no período:")
            exibir_tabela_formatada([linhas[0]] + filtrados)
            break
        elif opcao == '2':
            indice_data_adocao = linhas[0].index("Data de Adocao")
            filtrados = filtrar_por_periodo(linhas, indice_data_adocao, ano_inicio, ano_fim)
            print("\nGatos adotados no período:")
            exibir_tabela_formatada([linhas[0]] + filtrados)
            break


def exibir_tabela_csv(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        
        linhas = list(arquivo_csv)
        if not linhas:
            print("O arquivo está vazio.")
            return None
        
        # Determina a largura máxima de cada coluna
        colunas_largura = [max(len(str(valor)) for valor in coluna) for coluna in zip(*linhas)]
        
        # Calcula a largura necessária para a numeração das linhas
        num_linhas = len(linhas) - 1
        largura_num = len(str(num_linhas)) + 2  # 2 espaços adicionais para formatação
        
        # Formata o cabeçalho (primeira linha) com espaçamento para os números
        cabecalho = linhas[0]
        cabecalho_formatado = " " * largura_num + "  ".join(f"{valor:<{colunas_largura[i]}}" for i, valor in enumerate(cabecalho))
        print(cabecalho_formatado)
        
        # Imprime as linhas numeradas
        for idx, linha in enumerate(linhas[1:], start=1):
            linha_formatada = f"{idx:<{largura_num}}" + "  ".join(f"{valor:{colunas_largura[i]}}" for i, valor in enumerate(linha))
            print(linha_formatada)
        
        return linhas




def tabela():
    print()
    caminho_arquivo = "cadastro.csv"
    exibir_tabela_csv(caminho_arquivo)
    print()


def alterar_status(caminho_arquivo):
    linhas = exibir_tabela_csv(caminho_arquivo)
    
    if not linhas:
        return
    
    while True:
        try:
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()
            escolha = int(input("Escolha o número da linha que deseja alterar (0 para sair): "))
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            if escolha < 0 or escolha >= len(linhas) or escolha == 0:
                if escolha == 0:
                    return 
                raise ValueError
            break
        except ValueError:
            print("Escolha inválida. Por favor, digite um número válido ou 0 para sair.")
    
    linha_escolhida = linhas[escolha]
    
    print("\nLinha escolhida:")
    largura_num = len(str(len(linhas) - 1)) + 2

    # Cabeçalho formatado
    cabecalho = linhas[0]
    colunas_largura = [max(len(str(valor)) for valor in coluna) for coluna in zip(*linhas)]
    cabecalho_formatado = f"{'N° ':<{largura_num}} " + "  ".join(f"{valor:{colunas_largura[i]}}" for i, valor in enumerate(cabecalho))
    print(cabecalho_formatado)

    # Linha escolhida formatada
    linha_escolhida_formatada = f"{escolha:<{largura_num}} " + "  ".join(f"{valor:{colunas_largura[j]}}" for j, valor in enumerate(linha_escolhida))
    print(linha_escolhida_formatada)
    time.sleep(2)
    
    # Alterando a informação desejada
    print("\nColunas:")
    for i, coluna in enumerate(cabecalho):
        print(f"{i + 1}: {coluna}")
    print()
    while True:
        try:
            coluna_para_alterar = int(input("Digite o número da coluna que deseja alterar (ou '0' para sair): "))
            print()
            
            if coluna_para_alterar == 0:
                break

            if 1 <= coluna_para_alterar <= len(cabecalho):
                indice_coluna = coluna_para_alterar - 1
                novo_valor = input(f"Digite o novo valor para a coluna '{cabecalho[indice_coluna]}': ")
                print()
                linha_escolhida[indice_coluna] = novo_valor
            else:
                print("Número de coluna inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Salva as alterações de volta no arquivo CSV
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=',')
        escritor_csv.writerows(linhas)
    
    print("Alterações salvas com sucesso.")


def consultar_info(caminho_arquivo):
    linhas = exibir_tabela_csv(caminho_arquivo)
    
    if not linhas:
        return
    
    while True:
        try:
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()
            escolha = int(input("Escolha o número da linha que deseja consultar (0 para sair): "))
            print()
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print()

            if escolha < 0 or escolha >= len(linhas) or escolha == 0:
                if escolha == 0:
                    return
                raise ValueError
            break
        except ValueError:
            print("Escolha inválida. Por favor, digite um número válido ou 0 para sair.")
    
    linha_escolhida = linhas[escolha]
    

    print("\nLinha escolhida:")
    colunas_largura = [max(len(str(valor)) for valor in coluna) for coluna in zip(*linhas)]
    largura_num = len(str(len(linhas) - 1)) + 2

    # Formata o cabeçalho (primeira linha) com espaçamento para os números
    cabecalho = linhas[0]
    cabecalho_formatado =" " + " " * largura_num + "  ".join(f"{valor:{colunas_largura[i]}}" for i, valor in enumerate(cabecalho))
    print(cabecalho_formatado)

    # Formatar a linha escolhida
    linha_escolhida_formatada = f"{escolha:<{largura_num}} " + "  ".join(f"{valor:<{colunas_largura[i]}}" for i, valor in enumerate(linha_escolhida))
    print(linha_escolhida_formatada)





def adicionar_linha_csv(caminho_arquivo, linha):
    with open(caminho_arquivo, 'a', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=',')
        escritor_csv.writerow(linha)
    


# 4) Apresentar estatísticas gerais:
def apresentar_stats():
    print()
    print("Porcentagem de machos e femeas: ")
    print()
    time.sleep(1)
    caminho_arquivo = "cadastro.csv"
    calcular_porcentagem_genero(caminho_arquivo)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(2)
    print("Porcentagem de adotados: ")
    print()
    caminho_arquivo = "cadastro.csv"
    calcular_porcentagem_adotados(caminho_arquivo)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(2)
    print()
    caminho_arquivo = "cadastro.csv"
    calcular_fiv_fev(caminho_arquivo)
    


def calcular_porcentagem_genero(caminho_arquivo):
    total_gatos = 0
    masculinos = 0
    femininos = 0
    
    with open(caminho_arquivo, "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        
        # Ignora o cabecalho
        next(arquivo_csv)
        
        
        for linha in arquivo_csv:
            if linha[1] == 'M' or linha[1] == 'm':  
                masculinos += 1
            elif linha[1] == 'F' or linha[1] == 'f':  
                femininos += 1
            
            total_gatos += 1  
    
    # confere se tem gatos na tabela
    if total_gatos > 0:
        # Calcula a porcentagem
        porcentagem_masculinos = (masculinos / total_gatos) * 100
        porcentagem_femininos = (femininos / total_gatos) * 100
        
        print(f"Porcentagem de gatos masculinos: {porcentagem_masculinos:.2f}%")
        print(f"Porcentagem de gatos femininos: {porcentagem_femininos:.2f}%")
    else:
        print("Não há gatos no arquivo.")


def calcular_porcentagem_adotados(caminho_arquivo):
    total_gatos = 0
    adotados = 0
    nao_adotados = 0
    
    # Abrir o arquivo CSV
    with open(caminho_arquivo, "r", newline='', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=",")
        
        # Ignorar o cabeçalho
        next(arquivo_csv)
        
        # Iterar pelas linhas do arquivo CSV
        for linha in arquivo_csv:
            if linha[9].strip().lower() in ['sim', 's']:
                adotados += 1
            else:
                nao_adotados += 1
            
            total_gatos += 1  # Conta o total de gatos
    
    # Verifica se há gatos para evitar divisão por zero
    if total_gatos > 0:
        # Calcula a porcentagem de gatos adotados e não adotados
        porcentagem_adotados = (adotados / total_gatos) * 100
        porcentagem_nao_adotados = (nao_adotados / total_gatos) * 100
        
        # Formata e imprime os resultados
        print(f"Porcentagem de gatos adotados: {porcentagem_adotados:.2f}%")
        print(f"Porcentagem de gatos não adotados: {porcentagem_nao_adotados:.2f}%")
    else:
        print("Não há gatos no arquivo.")

def calcular_fiv_fev(caminho_arquivo):
        with open(caminho_arquivo, "r", newline='') as arquivo:
            arquivo_csv = csv.reader(arquivo, delimiter=",")
            linhas = list(arquivo_csv)
            
            total_felinos = len(linhas) - 1  # Exclui o cabeçalho
            
            # Inicializa contadores
            negativos_para_ambos = 0
            apenas_fiv_positivo = 0
            apenas_felv_positivo = 0
            ambos_positivo = 0
            nao_testados = 0
            nao_testados_fiv = 0
            nao_testados_felv = 0
            
            # Percorre as linhas para contar cada categoria
            for linha in linhas[1:]:
                fiv = linha[6].strip().lower()
                felv = linha[7].strip().lower()
                
                if fiv == '-':
                    nao_testados_fiv = nao_testados_fiv + 1

                if felv == '-':
                    nao_testados_felv = nao_testados_felv + 1
                
                if fiv == '-' and felv == '-':
                    nao_testados = nao_testados + 1

                if fiv == 'nao' and felv == 'nao':
                    negativos_para_ambos = negativos_para_ambos + 1

                elif fiv == 'sim' and felv == 'nao':
                    apenas_fiv_positivo = apenas_fiv_positivo + 1

                elif fiv == 'nao' and felv == 'sim':
                    apenas_felv_positivo = apenas_felv_positivo + 1

                elif fiv == 'sim' and felv == 'sim':
                    ambos_positivo = ambos_positivo + 1
            
            # Calcula as porcentagens
            
            porcentagem_negativos_para_ambos = (negativos_para_ambos / total_felinos) * 100
            porcentagem_apenas_fiv_positivo = (apenas_fiv_positivo / total_felinos) * 100
            porcentagem_apenas_felv_positivo = (apenas_felv_positivo / total_felinos) * 100
            porcentagem_ambos_positivo = (ambos_positivo / total_felinos) * 100
            porcentagem_nao_testados = (nao_testados / total_felinos) * 100
            porcentagem_nao_testados_fiv = (nao_testados_fiv / total_felinos) * 100
            porcentagem_nao_testados_felv = (nao_testados_felv / total_felinos) * 100

            
            # Exibe os resultados
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos negativos para FIV+ e FELV+: {porcentagem_negativos_para_ambos:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos apenas FIV+: {porcentagem_apenas_fiv_positivo:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos apenas FELV+: {porcentagem_apenas_felv_positivo:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos com ambos FIV+ e FELV+: {porcentagem_ambos_positivo:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos nao testados para FIV+: {porcentagem_nao_testados_fiv:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos nao testados para FELV+: {porcentagem_nao_testados_felv:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(f"Porcentagem de felinos nao testados para FIV+ e FELV+: {porcentagem_nao_testados:.2f}%")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    


def cadastrar_felino():
    time.sleep(0.5)
    print()
    print("Você escolheu a opção cadastrar um felino")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    
    nome = input("Digite aqui o nome do gato: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    sexo = input("Digite o sexo do gato (M/F): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    
    idade = input("Digite a idade do gato: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    raca = input("Digite a raça do gato: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    cor_predominante = input("Digite a cor predominante do gato: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    castrado = input("O gato é castrado? (Sim/Não): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    fiv = input("O gato tem FIV+? (Sim/Não): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    felv = input("O gato tem FELV+? (Sim/Não): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    data_resgate = input("Digite a data de resgate do gato (DD/MM/AAAA): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    adotado = input("O gato foi adotado? (Sim/Não): ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    adocao = input("Digite a data de adocao do gato (DD/MM/AAAA) ou (-) caso nao teve: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    ultima_vacinacao = input("Digite a data da última vacinação do gato (DD/MM/AAAA) ou (-) caso nao teve ou não saiba: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    ultima_desvermifugacao = input("Digite a data da última desvermifugação do gato (DD/MM/AAAA) ou (-) caso nao teve ou não saiba: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    ultimo_antipulgas = input("Digite a data do último antipulgas do gato (DD/MM/AAAA)  ou (-) caso nao teve ou não saiba: ")
    time.sleep(1)
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()

    
    nova_linha = [nome, sexo, idade, raca, cor_predominante, castrado, fiv, felv, data_resgate, adotado, adocao, ultima_vacinacao, ultima_desvermifugacao, ultimo_antipulgas]
    caminho_arquivo = "cadastro.csv"
    adicionar_linha_csv(caminho_arquivo, nova_linha)
    print("Gato cadastrado com Sucesso!")
    print()
    time.sleep(2)



def main():
    print()
    print("|----------------------------------------------|")
    print("|                                              | ") 
    print("|             O que você deseja?               | ") 
    print("|                                              | ") 
    print("|    1) Cadastrar felino                       | ")              
    print("|    2) Alterar Status de felino               |")
    print("|    3) Consultar informações sobre felino     |")
    print("|    4) Apresentar estatísticas gerais         |")
    print("|    5) Filtragem de dados                     |")
    print("|    6) Salvar                                 |")
    print("|    7) Sair do programa                       |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print()
    print()

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    decisao = int(input("Digite aqui a opção que você deseja: "))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    if decisao == 1:
        cadastrar_felino()
        time.sleep(3)
        voltar_menu()

    if decisao == 2:
        caminho_arquivo = "cadastro.csv"
        alterar_status(caminho_arquivo)
        time.sleep(3)
        voltar_menu()
    
    if decisao == 3:
        caminho_arquivo = "cadastro.csv"
        consultar_info(caminho_arquivo)
        time.sleep(3)
        voltar_menu()
    
    if decisao == 4:
        apresentar_stats()
        time.sleep(3)
        voltar_menu()
    
    if decisao == 5:
        caminho_arquivo = "cadastro.csv"
        filtragem_dados(caminho_arquivo)
        time.sleep(3)
        voltar_menu()
    
    if decisao == 6:
        caminho_arquivo = "cadastro.csv"
        linhas = (caminho_arquivo)
        salvar(caminho_arquivo, linhas)
        time.sleep(3)
        voltar_menu()

    if decisao == 7:
        time.sleep(1)
        caminho_arquivo = "cadastro.csv"
        linhas = (caminho_arquivo)
        salvar(caminho_arquivo, linhas)
        time.sleep(1.5)
        print("Encerrando o programa...")
        time.sleep(3)
        sys.exit

    if decisao != 1 and decisao !=2 and decisao !=3 and decisao !=4 and decisao !=5 and decisao !=6 and decisao !=7:
        print()
        print("Digite 1, 2, 3, 4, 5, 6, 7 para a opcao desejada!")
        time.sleep(3)
        main()


# COMANDO PARA VOLTAR AO MENU INICIAL
def voltar_menu():
    x = 1
    while x == 1:
        print()
        voltar = int(input("Digite 1 para quando voce desejar voltar ao menu principal: "))
        print()
        if voltar == 1:
            main()
            x = x - 1
        else:
            x = x

def salvar(caminho_arquivo, linhas):
    linhas = exibir_tabela_csv(caminho_arquivo)
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo, delimiter=',')
        escritor_csv.writerows(linhas)
    
    print()
    print("Alterações salvas com sucesso.")

#MAIN

print()
print("BOA TARDE!")
time.sleep(3)
print()
main()


