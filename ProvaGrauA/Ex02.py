# Agora crie uma função divisivelPorN que receba como parâmetro dois números inteiros e retorne
#True se o primeiro é divisível pelo segundo, e False caso contrário. O segundo parâmetro não pode ser zero,
#então cheque isso dentro da função (se for zero, imprima uma mensagem dizendo que não é possível efetuar
#divisão por zero e retorne False).


divisivel = True

print()
n1 = int(input("Digite aqui um número: "))
print()
n2 = int(input("Digite aqui outro número: "))
print()

if n2 == 0:
    print("Não é possível efetuar uma divisão por zero")
    divisivel = False
    print()
elif n1 % n2 == 0:
    print("O primeiro número é divisível pelo segundo")
    nf = n1 / n2
    print("O resultado dessa divisão é: ", nf)
    divisivel = True
    print()
else:
    print("O primeiro número não é divisível pelo segundo")
    divisivel = False
    print()

