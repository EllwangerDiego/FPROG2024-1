lista = []

print()
num = int(input("Digite aqui a quantidade de itens que deseja adicionar na lista: "))
print()

while num != 0:
    num = num - 1
    item = input("Digite aqui o item a ser adicionado: ")
    print()
    lista.append(item)

print()
print("Sua lista:")
print()
print(lista)
print()