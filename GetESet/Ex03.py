lista_funcionarios = []

class Empresa():
    def __init__(self, nome, funcionarios):
        self.nome = nome
        self.funcionarios = funcionarios
        


        
    def main(self):
        x = 2
        r = Empresa(a, b)
        a = input("Digite aqui o nome da empresa: ")
        while x != 0:
            b = input("Digite aqui o nome dos funcionarios, um de cada vez: ")
            lista_funcionarios.append(b)
            x = x - 1

        
        
    
    def imprime_info(self):
        print(f"Nome da Empresa = {self.nome}")
        print(f"Funcionarios = {lista_funcionarios}")



if __name__ == '__main__':
    a = []
    b = []
    r = Empresa(a, b)
    r.main()
    r.imprime_info()
