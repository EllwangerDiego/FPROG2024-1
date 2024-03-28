# Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
# da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
# for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
# tela o valor de venda.

print()
produto = float(input('Digite aqui o valor do produto: '))
print()

if produto <= 20:
    desconto1 = produto * 0.45
    desconto2 = produto +  desconto1
    print('Por ser um produto de até R$ 20,00, o lucro será de 45%, então você deverá vende-lo por: ', desconto2)
    print()
elif produto <= 50 and produto > 20:
    desconto1 = produto * 0.35
    desconto2 = produto + desconto1
    print('Por ser um produto de valor de até R$ 50,00 e superior a R$ 20,00 o lucro será de 35%, então você deverá vende-lo por: ', desconto2)
    print()
else:
    desconto1 = produto * 0.25
    desconto2 = produto + desconto1
    print('Por ser um valor superior a R$ 50,00 o lucro será de 25%, então você deverá vende-lo por: R$ ', desconto2)
    print()
