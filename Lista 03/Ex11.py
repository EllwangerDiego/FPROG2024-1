# Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
# cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50,
# R$ 20, R$ 10 e R$ 5 e R$ 1. Seu programa deve mostrar apenas as notas utilizadas. Por exemplo, ao
# solicitar R$18, o programa deve informar apenas a seguinte informação (note que não foram
# exibidas informações sobre as demais cédulas):
# 1 nota(s) de R$ 10.
# 1 nota(s) de R$ 5.
# 3 nota(s) de R$ 1.

print()

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
nota5 = 5
nota1= 1

venda = float(input('Digite aqui o valor total da compra: '))
cliente = float(input('Digite aqui o valor recebido pelo cliente: '))
troco = cliente - venda

if cliente != venda:
    print('Você deve dar R$', troco, 'de troco')
    print()
    