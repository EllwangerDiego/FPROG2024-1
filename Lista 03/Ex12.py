# A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um
# algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:
# Categoria Idade
# Infantil A 5-7 anos
# Infantil B 8-10 anos
# Juvenil A 11-13 anos
# Juvenil B 14-17 anos
# Sênior Maiores de 18 anos

print()

idade = int(input('Digite aqui a idade do nadador: '))

if idade > 4 and idade < 8:
    print()
    print('Sua categoria é: Infantil A')
    print()
elif idade > 7 and idade < 11:
    print()
    print('Sua categoria é: Infantil B')
    print()
elif idade > 10 and idade < 14:
    print()
    print('Sua categoria é: Juvenil A')
    print()
elif idade > 13 and idade < 18:
    print()
    print('Sua categoria é: Juvenil B')
    print()
elif idade > 17:
    print()
    print('Sua categoria é: Sênior')
    print()
elif idade < 5:
    print()
    print('Você não possui a idade mínima para participar ')
    print()
else:
    print()