lista = []
class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
    
    def set_nome(self):
        self.nome = input("Digite aqui seu nome: ")
        return self.nome
    
    def set_idade(self):
        return self.idade
    
    def set_altura(self):
        return self.altura
    
    def set_peso(self):
        return self.peso
    
    def visualizar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Altura: {self.altura}")
        print(f"Peso: {self.peso}")

def main():
    nome = input("Digite aqui seu nome: ")
    lista.append(nome)
 
    idade = input("Digite aqui sua idade: ")
    lista.append(idade)

    altura = input("Digite aqui sua altura: ")
    lista.append(altura)

    peso = input("Digite aqui seu peso: ")
    lista.append(peso)
    
    print("\n", lista, "\n")

main()