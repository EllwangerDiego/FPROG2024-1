
f = open('qst1.txt', 'w')

nome = input("Digite aqui seu nome: ")
idade = input("Digite aqui sua idade: ")
altura = input("Digite aqui sua altura: ")
peso = input("Digite aqui seu peso: ")

f.write(nome)
f.write('\n')
f.write(idade)
f.write('\n')
f.write(altura)
f.write('\n')
f.write(peso)
f.close()
f = open('qst1.txt', 'r')
x = f.read()
f.close()
print(x)