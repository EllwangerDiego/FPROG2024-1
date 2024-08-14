matriz = [[0, 0, 0], 
          [0, 0, 0, ], 
          [0, 0, 0, ]]

spar = mai = scol = 0

print()
for linha in range(0,3):
    for col in range(0,3):
        matriz[linha][col] = int(input("Digite aqui um valor para ({}, {}): ".format(linha,col)))

print()
print("-=" * 30)
for linha in range(0,3):
    for col in range(0,3):
        print(f'[{matriz [linha][col]:^5}]', end='')
        if matriz [linha] [col] % 2 ==0:
            spar += matriz[linha][col]
    print()
print("-=" * 30)
print()
print("A soma dos valores pares eh: {}".format(spar))
print()
for linha in range(0,3):
    scol += matriz[linha][2]
print("A soma dos valores da terceira coluna eh: {}".format(scol))
print()
for col in range(0, 3):
    if col == 0:
        mai = matriz[1][col]
    elif matriz[1][col] > mai:
        mai = matriz[1][col]
print("O maior valor da segunda linha eh: {}".format(mai))
print()


