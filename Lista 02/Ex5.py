#Um motorista deseja encher o tanque do seu carro com gasolina. Escreva um algoritmo para ler o
#preço do litro da gasolina e o valor que o motorista tem disponível para abastecer. Calcule quantos
#litros ele conseguiu colocar no tanque e exiba na tela.

ValorLitro = 5.58

print()
print ('Boa tarde, o litro da gasolina está saindo por: R$ ',ValorLitro )
print('')
quantidade = float(input('Digite aqui o valor que você deseja abastecer: R$ '))

litro = quantidade / ValorLitro

round (litro,2)
print('')
print('Com este valor, você conseguirá colocar: ', round (litro,2),'litros')
print('')

pagamento = input('Qual será a forma de pagamento? ' )


if pagamento == 'credito':
    print('')
    print('Certo, vou buscar a maquininha, 10 segundos, ja volto')
    print()
    import time
    time.sleep(10)
    print('Pode inserir o cartão')
    print()
    time.sleep(5)
    print('Muito obrigado, tenha uma boa tarde!')
    print()
    
elif pagamento =='debito':
    print()
    print('Certo, vou buscar a maquininha, 10 segundos, ja volto')
    print()
    import time
    time.sleep(10)
    print('Pode inserir o cartão')
    print()
    time.sleep(5)
    print('Muito obrigado, tenha uma boa tarde!')
    print()
 
else: 
    print()
    import time
    time.sleep(5)
    print ('Muito obrigado, tenha uma boa tarde!')
print('')
