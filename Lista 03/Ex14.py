# Criar um programa para identificar o valor a ser pago por um plano de saúde dada a idade do
# conveniado considerando que todos pagam R$ 300 e mais um adicional (se tiver dependentes)
# conforme a seguinte tabela:
# a) crianças com menos de 10 anos pagam R$100;
# b) dependentes com idade entre 10 e 30 anos pagam R$220;
# c) dependentes com idade entre 31 e 60 anos pagam R$ 395;
# d) dependentes com mais de 60 anos pagam R$ 480.

print()
valor1 = 300
criancas = 100
d1 = 220
d2 = 395
d3 = 480

print()
idade = float(input("Digite aqui a sua idade: "))
print()

if idade < 10:
    print("O valor do seu plano de saúde é de: ", criancas)
    print()

elif idade > 9 and idade < 31:
    valorF = valor1 + d1
    print("O valor do seu plano de saúde é de: ", valorF )
    print()

elif idade > 30 and idade < 61:
    valorF = valor1 + d2
    print("O valor do seu plano de saúde é de: ", valorF )
    print()

elif idade > 60:
    valorF = valor1 + d3
    print("O valor do seu plano de saúde é de: ", valorF )
    print()