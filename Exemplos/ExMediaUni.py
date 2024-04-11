##################### FUNCOES #######################
def mediaUnisinos (grauA, grauB):
    media = (grauA + grauB * 2) / 3
    return media

################# PROGRAMA PRINCIPAL ##################

grauA = float(input('Digite aqui sua média do Grau A: '))
grauB = float(input('Digite aqui sua média do Grau B: '))

grauFinal = mediaUnisinos(grauA, grauB)
print('Grau final é: ', grauFinal)
