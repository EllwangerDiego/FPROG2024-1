##################### FUNCOES #######################
def tabuada(n):
    for i in range (1,11):
        res = n * i
        print(n, "x", i, "=", n * i)


################# PROGRAMA PRINCIPAL ##################

for i in range (0,11):
    tabuada (i)
    print("------------------------------------")