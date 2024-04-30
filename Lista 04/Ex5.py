
print()
Notas = []
xalunos = int(input("Digite aqui a quantidade de alunos: "))
falunos = xalunos


while xalunos > 0:
    print()
    GrauA = int(input("Digite aqui a nota do Grau A: "))
    print()
    GrauB = int(input("Digite aqui a nota do Grau B: "))
    print()
    NotaF = (GrauA + (GrauB*2)) /3


    print("Sua nota final foi ",NotaF)
    if NotaF >= 6:
        print()
        Notas.append(NotaF)
        print("Voce foi aprovado!")
        print()
    elif NotaF < 6:
        print("Voce esta abaixo da media :(  ")
        print()
        escolha = input("Digite aqui qual grau voce deseja recuperar no Grau C: (A/B) ")
        print()
        if escolha == "A":
            GrauC = int(input("Digite aqui a nota do Grau C: "))
            NotaF = (GrauC + (GrauB*2)) /3
        elif escolha =="B":
            GrauC = int(input("Digite aqui a nota do Grau C: "))
            NotaF = (GrauA + (GrauC * 2)) /3
            if NotaF >= 6:
                print()
                Notas.append(NotaF)
                print("Sua nota final foi ",NotaF)
                print()
                print("Voce foi aprovado!")
                print()
            elif NotaF < 6:
                print()
                Notas.append(NotaF)
                print("Sua nota final foi ",NotaF)
                print()
                print("Voce foi reprovado!")
                print()

    xalunos = xalunos - 1

if falunos > 1:
    media = sum(Notas)/falunos
    print("A media das notas foi: ", media)
    print()
    