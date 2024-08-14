
print()
v = [
    [1,  5,  9,  2,  5],
    [7,  4, 13, 21,  6],
    [8, -3,  5,  7, 12]
     ]

for linha in v:
    print(linha)

print()

for i in range(len(v)):
    for j in range(len(v[i])):
        v[i][j] *= 7

for linha in v:
    print(linha)

print()