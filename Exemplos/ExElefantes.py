##################### FUNCOES #######################
print()
print ('-----------------PLAY-----------------')
print()
def musicaElefantes(n):
    for i in range (1, n):
        
        print()
        print(i, "elefante(s) incomoda(m) muito a gente, ")
        print(i + 1, "elefante(s) " , end="" )
        for j in range (0, i+1):
            print("incomodam, " , end="")
        print ('muito mais!')
        print()


################# PROGRAMA PRINCIPAL ##################

musicaElefantes(5)