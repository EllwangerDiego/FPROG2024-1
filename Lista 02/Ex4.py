GrauA = input('Digite aqui a nota do Grau A: ')
GrauB = input('Digite aqui a nota do Grau B: ')

media = GrauA + (GrauB * 2) 
mediaA = media / 3


print ('Sua média anual foi: ', mediaA)

if mediaA < 7:
    print ('Você está abaixo da média')
else:
    print ('Você está acima da média')