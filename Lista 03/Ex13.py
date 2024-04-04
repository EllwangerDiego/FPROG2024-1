# Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme
# as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou
# em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau
# A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o
# grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.


print()
GrauA = float(input('Digite aqui a nota do Grau A: '))
GrauB = float(input('Digite aqui a nota do Grau B: '))
print()
media = GrauA + (GrauB * 2) 
mediaA = media / 3

mediaA = round(mediaA, 2)
print ('Sua média anual foi: ', mediaA)
print()

if mediaA >= 6:
    print ('Você está acima da média!!! :D ')
    

    print()
else:
    print ('Você está abaixo da média :(')
    print()
    A = ('a')
    B = ('b')
    print()
    C = input('Se você deseja recuperar a nota do Grau A (digite "a"), se você deseja recuperar a nota do Grau B, ("digite b"):  ')
    print()
    GrauC = float(input('Digite aqui a nota do Grau C: '))
    print()
    if GrauC == A:
        print('')
        media2 = (GrauC + (GrauB * 2)) / 3
        print()
        if media2 >= 6:
            print('Você ficou acima da média!!! :D ')
            print()
        else:
            print()
    elif GrauC == B:
        print()
        media2 = (GrauA + (GrauC * 2)) / 3
        if media2 < 6:
            print('Você ficou abaixo da média :( ')
            print()
        else:
            print()
