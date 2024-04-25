#Faça uma função divisivel por 2 que receba como parâmetro um número inteiro, e retorne True se o
#número é divisível por 2, e False caso contrário.

divisivel = True
print()
n = int(input("Digite aqui um número inteiro: "))
print()

if n % 2 == 0:
    divisivel = True
    print("É um número divisível por 2 ")
    print()
    nf = n / 2
    print("O resultado dessa divisão é: ", nf)
    print() 
else:
    divisivel = False
    print("Não é um número divisível por 2")
    print()