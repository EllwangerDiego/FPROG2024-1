#Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas pelos clientes. Faça um programa que leia o valor da 
#compra e escreva o valor da compra com o desconto.  

print()
Valor = float(input('Digite aqui o valor total de sua compra: R$ '))
print()
ValorD = Valor * 0.15
ValorF = Valor - ValorD
print('O valor final com desconto é de: R$', ValorF)
print()