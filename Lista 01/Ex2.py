# 2. Escreva um programa em linguagem Python que solicite o nome do usuário e, em seguida, 
# imprima uma mensagem de boas-vindas na tela, utilizando o nome fornecido.

print('')
nome = input('Digite aqui seu nome: ')
print('')

print('Seja bem vindo(a)', nome,'!!!')
print('')

idade = input ('Qual a sua idade? ')

if idade < 18:
    print (nome), ('Você é menor de idade')

else:
    print (nome), ('Você é maior de idade')
