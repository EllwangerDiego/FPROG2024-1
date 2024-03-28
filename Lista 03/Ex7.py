# Implementar um programa que calcula o desconto previdenciário de um funcionário. O programa
# deve, dado um salário retornar o valor do desconto proporcional ao mesmo. O cálculo de desconto
# segue a regra: o desconto deve 11% do valor do salário. Entretanto, o valor máximo de desconto é
# 318,20. Sendo assim, ou o método retorna 11% sobre o salário ou 318,20.

print()
salario = float(input('Digite aqui o seu salário: '))
print()
desconto = 0.11

aa = salario * desconto


if aa > 318.20:
    print('Vai ser retornado o valor de R$ 318,20')
else:
    print('Vai ser retornado o valor de R$ ', aa)

print()


