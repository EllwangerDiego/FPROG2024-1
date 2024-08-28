lista = []


class Pessoa:
    def __init__(self, nome, idade, altura, irmaos, endereco, unico):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.irmaos = irmaos
        self.endereco = endereco
        self.filho_unico = unico
        
        
    
    def imprime_info(self):
        print(f"Nome = {self.nome}")
        print(f"Idade = {self.idade}")
        print(f"Altura = {self.altura}")
        print(f"Quantidade irmãos = {self.irmaos}")
        print(f"Endereço = {self.endereco}")
        
    
    def is_filho_unico(self):
        if self.irmaos == 0:
            unico = True
            print("É filho único")
            self.filho_unico = "É filho único"
        else:
            unico = False
            print("Não é filho único")
            self.filho_unico = "Não é filho único"
        

def main():
    print()
    n = input("Digite aqui seu nome: ")
    i = int(input("Digite aqui sua idade: "))
    a = float(input("Digite aqui sua altura: "))
    ir = int(input("Digite aqui a quantidade de irmãos que você possui: "))
    e = input("Digite aqui seu endereço: ")
    u = []

    lista.append(n)
    lista.append(i)
    lista.append(a)
    lista.append(ir)
    lista.append(e)
    lista.append(u)
    print()
    p = Pessoa(n, i, a, ir, e, u)
    p.imprime_info()
    p.is_filho_unico()
    print()



if __name__ == '__main__':
    x = 3
    while x != 0:
        main()
        x = x - 1
    print(lista)
    

