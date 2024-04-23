# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# 1 - À vista em dinheiro, recebe 15% de desconto
# 2 - À vista no cartão de crédito, recebe 10% de desconto
# 3 - Em duas vezes, preço normal de etiqueta sem juros
# 4 - Em três vezes, preço normal de etiqueta mais juros de 10%

print()
ValorP = float(input("Digite aqui o valor total do produto: "))
print()
print("|--------------------------------------------|")
print("|      QUAL SERÁ O MÉTODO DE PAGAMENTO?      | ") 
print("|                                            | ") 
print("|      1) À vista em dinheiro                | ")              
print("|      2) À vista no cartão de crédito       |")
print("|      3) Em duas vezes                      |")
print("|      4) Em três vezes                      |")
print("|--------------------------------------------|")
print()



i = 1
while i == 1:
    opcao = int(input("Digite aqui um valor de 1-4 correspondente ao seu método de pagamento: "))
    print()
    if opcao == 1:
        ValorD = ValorP * 0.15
        ValorF = ValorP - ValorD
        print("O valor final será: R$ ",ValorF)
        i = 2
        print()
        
    elif opcao == 2:
        ValorD = ValorP * 0.10
        ValorF = ValorP - ValorD
        print("O valor final será: R$ ",ValorF)
        i = 2
        print()

    elif opcao == 3:
        ValorD = ValorP * 1
        ValorF = ValorP 
        V2 = ValorF / 2
        i = 2
        print("O valor final será: R$ ",ValorF)
        print("Cada parcela ficara por: R$ ", V2)
        print()

    elif opcao == 4:
        ValorD = ValorP * 1
        ValorF = ValorP 
        J = ValorF * 0.1
        V3 = ValorF / 3
        VD3 = V3 + J
        i = 2
        print("O valor final será: R$ ",ValorF)
        print("Cada parcela ficara por: R$ ", VD3)
        print()
