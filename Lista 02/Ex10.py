# O lojista gostou tanto do seu programa anterior que encomendou outro. Dessa vez ele quer que você calcule quanto cada cliente gastou na loja apenas
# informando o número de camisetas, calças e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o valor da compra 
# e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do desconto e o valor da compra. 

print()
camiseta = 25
calca = 100
cinto = 40

qcamiseta = float(input('Type here the amount of t-shirt that you want to buy: '))
print()
qcalca = float(input('Type here the amount of pants that you want to buy: '))
print()
qcinto = float(input('Type here the amount of belt that you want to buy: '))
print()

VC = qcamiseta * 25
VCa = qcalca * 100
VCi = qcinto * 40

VF = VC + VCa + VCi

print('#--------------------------------------------------#')
print()
print ('The total price withouth discount is: R$ ', VF)
print()
D = VF * 0.1

VFD = VF - D

print('With the discount, you will save: R$ ',D)
print()
print('The total with the discount is: R$ ',VFD)
print()




                