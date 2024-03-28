# Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
# de cada moeda em relação ao real. Depois apresente o seguinte menu:
# 1) Converter de Real para Euro
# 2) Converter de Real para Dólar
# 3) Converter de Euro para Dólar
# 4) Converter de Euro para Real
# 5) Converter de Dólar para Euro
# 6) Converter de Dólar para Real
# Leia o valor a ser convertido na moeda de origem e imprima na tela a quantidade na moeda
# destino.

print()
euro = float(input('Digite aqui a cotação do euro em relação ao real: '))
print()
dolar = float(input('Digite aqui a cotação do dolar em ralação ao real: '))
print()

print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
print()

opcao = int(input('Digite aqui o número da operação que você deseje fazer: '))
print()

if opcao == 1:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = valor1 / euro
    print('R$',valor1, 'ficará', valor2,'euros')
    print()
elif opcao == 2:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = valor1 / dolar
    print('R$',valor1,'ficará USD', valor2)
elif opcao == 3:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = euro / dolar
    valor3 = valor1 / valor2
    print (valor1 ,' euros, ficará USD', round (valor3,2))
    print()
elif opcao == 4:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = valor1 / euro
    print(valor1, 'euros ficará R$', round(valor2,2 ))
    print ()
elif opcao == 5:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = dolar / euro
    valor3 = valor1 / valor2
    print ('USD', valor1 ,' ficará EUR', round (valor3,2))
    print()
elif opcao == 6:
    valor1 = float(input('Digite aqui o valor que você deseja converter: '))
    print()
    valor2 = valor1 / dolar
    print('USD', valor1, ' ficará R$', round(valor2,2 ))
    print ()

else:
    print('Digite um número entre 1 e 6')
    print()