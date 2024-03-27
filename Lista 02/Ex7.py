#Um criador de pássaros deseja saber a quantidade de ração diária necessária para alimentar seus pássaros. Cada pássaro consome 30 gramas de ração por dia. 
#Escreva um programa que leia o número de pássaros que o criador possui e calcule a quantidade total de ração necessária por dia. 

print()
passaros = float(input('Digite aqui a quantidade de pássaros que você possui: '))
print()

quantidade = passaros * 30

kg = quantidade / 1000
print('---------------------------------------------')
print(quantidade)
print('---------------------------------------------')

if quantidade > 1000:    
    print('O total de ração diária necessária para alimentar seus pássaros é de: ', kg, 'kg')
    print()
else:
    print('O total de ração diária necessária para alimentar seus pássaros é de: ', quantidade, 'gramas')
    print()


