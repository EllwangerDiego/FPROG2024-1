num = int(input("Digite aqui um numero: "))

def tabuada():
    for i in range(11):
        x = num * i
        print("{} X {} = {}".format(num,i,x))

tabuada()