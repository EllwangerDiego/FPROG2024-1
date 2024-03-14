print('')
GrauA = float(input('Digite aqui a nota do Grau A: '))
GrauB = float(input('Digite aqui a nota do Grau B: '))
print('')
media = GrauA + (GrauB * 2) 
mediaA = media / 3

mediaA = round(mediaA, 2)
print ('Sua média anual foi: ', mediaA)
print('')

if mediaA < 7:
    print ('Você está abaixo da média :(')
    print('')
else:
    print ('Você está acima da média!!! :D ')
    print('')