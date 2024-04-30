print()
GrauA = float(input("Digite aqui a nota do Grau A: "))
print()
GrauB = float(input("Digite aqui a nota do Grau B: "))
print()

def mediaUnisinos():
    NotaF = (GrauA + (GrauB * 2))/3
    print("Sua media final foi: ", NotaF)
    print()

mediaUnisinos()