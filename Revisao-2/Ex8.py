joio = []
trigo = []

joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio",
"joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio",
"joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio",
"joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "joio",
"trigo", "joio", "joio", "joio"]

a = len(joioETrigo)
j = joioETrigo.count("joio")
t = joioETrigo.count("trigo")
j1 = j
t2 = t


while j != 0:
    joio.append("joio")
    j = j - 1

while t != 0:
    trigo.append("trigo")
    t = t - 1

print()
print("Joio: ", j1)
print(joio)
print()

print(("Trigo: ", t2))
print(trigo)
print()

