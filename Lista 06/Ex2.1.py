# Definindo o tamanho do vetor
tamanho = 5

# Inicializando o vetor com valores vazios
vetor = []

# Solicitando ao usuário para inserir os valores
print(f"Digite {tamanho} valores para preencher o vetor:")
for i in range(tamanho):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)

# Imprimindo o resultado da multiplicação de cada valor pela sua posição
print("Resultado da multiplicação de cada valor pela sua posição:")
for i in range(tamanho):
    resultado = vetor[i] * i
    print(f"Posição {i}: {vetor[i]} * {i} = {resultado}")
