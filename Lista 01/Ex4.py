print ('')
print ('Qual é o verdadeiro nome do super-herói Batman?')

alternativaA = ('a) Bruce Wayne')
alternativaB = ('b) Clark Kent')
alternativaC = ('c) Peter Parker')
alternativaD = ('d) Tony Stark')
alternativaE = ('e) Steve Rogers')

print('')
print (alternativaA)
print (alternativaB) 
print (alternativaC) 
print (alternativaD) 
print (alternativaE)
print ('')

resposta = 'a'

respostaUsuario = input('Digite aqui sua resposta: ')
print ('')

print('')
if respostaUsuario == resposta:
    print ('Parabéns, você acertou!!!')
    print ('')
else:
    print ('Você errou, a alternativa correta é a letra:', resposta)
    print('')