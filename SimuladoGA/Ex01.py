#Faça uma função que verifique se um número inteiro é primo ou não, retornando True ou False. 

print()
n = int(input('Digite um numero: '))
print()

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, 'não é primo')
            break
    else:
        print(n, 'é primo')
elif n == 0:
    print(n, 'é zero')
elif n == 1:
    print(n, 'é um')
else:
    print(n, 'é negativo')
