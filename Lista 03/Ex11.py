
# Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
# cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50,
# R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao
# solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram
# exibidas informações sobre as demais cédulas):
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

print()

notas = [100,50,20,10,5,1,0.5,0.10,0.05]
venda = float(input('Digite aqui o valor total da compra: '))
cliente = float(input('Digite aqui o valor recebido pelo cliente: '))
troco = cliente - venda
somatroco = [0,0,0,0,0,0,0,0,0]
tamanhosomatroco = 0



for i in range(9):
    while troco >= notas[i]:
        somatroco[i]+=1
        tamanhosomatroco+=1
        troco -= notas[i]






for i in range(9):
        if somatroco[i] != 0:
            print(str(somatroco[i]),"nota(s) de R$ ",str(notas[i]),".")