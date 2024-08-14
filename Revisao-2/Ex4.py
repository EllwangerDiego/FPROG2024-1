print()
quant = 0
texto = []
vogais = "a"

texto = input("Digite aqui uma frase: ")
tamanho = len(texto)
a = texto.count("a")
e = texto.count("e")
i = texto.count("i")
o = texto.count("o")
u = texto.count("u")


quant = quant + a + e + i + o + u
    
        

print()
print(f"Existem {quant} vogais nessa frase.")
print()
