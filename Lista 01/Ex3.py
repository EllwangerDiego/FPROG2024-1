print ('')
print ('Qual é o verdadeiro nome do super-herói Batman?')

print('')
print ('a) Bruce Wayne') 
print ('b) Clark Kent') 
print ('c) Peter Parker') 
print ('d) Tony Stark') 
print ('e) Steve Rogers')
print ('')

resposta = 'a'

respostaUsuario = input('Digite aqui sua resposta: ')
print ('')

print('')
if respostaUsuario == 'a':
    print ('Parabéns, você acertou!!!')
    print ('')
else:
    print ('Você errou, a alternativa correta é a letra:', resposta)
    print('')

