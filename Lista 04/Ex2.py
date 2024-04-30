import random
x=0
n = random.randint(1,10)
print()

while x <3:
    guess = int(input("Digite um numero entre 1 e 10: "))
    if guess == n:
        print("Voce acertou!")
        x = 4
    elif guess <n:
        print("O numero eh maior que ", guess)
        x = x + 1
    elif guess > n:
        print("O numero eh menor que ",guess)
        x = x + 1
print()
if x == 3:
    print("Suas tentativas acabaram :( ")
    print()
