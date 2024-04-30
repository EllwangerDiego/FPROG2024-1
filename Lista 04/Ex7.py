print()
nomes = []

x = 5
while x > 0:
    nome = input("Digite aqui {} nome(s): ".format(x))
    nomes.append(nome)
    print()
    x = x - 1

nomes.sort()
print("Nomes em ordem alfabetica: ")
for nome in nomes:
    print("-------------------------")
    print(nome)
print("-------------------------")
print()
