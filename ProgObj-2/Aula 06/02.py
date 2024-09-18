f = open('qst1.txt', 'r')
nome = f.readline()
idade = f.readline()
altura = f.readline()
peso = f.readline()

f.close()
print(f"\nNome: {nome}\nIdade: {idade}\nAltura: {altura}\nPeso: {peso}\n")

      
