class Calculadora:
    def __init__(self, memoria: 0, cor, x, y):
        self.memoria = memoria
        self.cor = cor
        self.x = x
        self.y = y
        self.soma = []



    def main(self):
        print()
        b = 0
        a = input("Informe a cor da calculadora: ")
        print()
        print(f"memoria = {self.memoria}")
        print(f"cor = {self.cor}")
        print()
        print()
        x = []
        y = []
        r = Calculadora(b, a, x, y)
        print()
        print()
        print("|----------------------------------------------|")
        print("|                                              | ") 
        print("|             O que você deseja?               | ") 
        print("|                                              | ") 
        print("|    1) Somar                                  | ")              
        print("|    2) Subtrair                               |")
        print("|    3) Multiplicar                            |")
        print("|    4) Dividir                                |")
        print("|    5) Elevar ao Quadrado                     |")
        print("|    6) Elevar ao Cubo                         |")
        print("|                                              |")
        print("|----------------------------------------------|")
        print()
        print()
        opcao = int(input("Digite aqui a opção desejada: "))
        if opcao == 1:
            r.somar()
        if opcao == 2:
            r.subtrair()
        if opcao == 3:
            r.multiplica()
        if opcao == 4:
            r.divide()
        if opcao == 5:
            r.quadrado()
        if opcao == 6:
            r.cubo()
        
        print()
        r.imprime_info()
        print()
    
    def somar(self) -> float:
        self.x = float(input("Digite aqui o primeiro valor: "))
        self.y = float(input("Digite aqui o segundo valor: "))
        self.soma = self.x + self.y
        print("A soma é: ", self.soma)
    
    def subtrair(self) -> float:
        self.x = float(input("Digite aqui o primeiro valor: "))
        self.y = float(input("Digite aqui o segundo valor: "))
        self.subtrair = self.x - self.y
        print("A subtração é: ", self.subtrair)
    
    def multiplica(self) -> float:
        self.x = float(input("Digite aqui o primeiro valor: "))
        self.y = float(input("Digite aqui o segundo valor: "))
        self.multiplica = self.x * self.y
        print("A multiplicação é: ", self.multiplica)

    def divide(self) -> float:
        self.x = float(input("Digite aqui o primeiro valor: "))
        self.y = float(input("Digite aqui o segundo valor: "))
        self.divide = self.x / self.y
        print("A divisão é: ", self.divide)
    
    def quadrado(self) -> float:
        self.x = float(input("Digite aqui o valor: "))
        self.quadrado = self.x * self.x
        print(self.x, " elevado ao quadrado é: ", self.quadrado)
    
    def cubo(self) -> float:
        self.x = float(input("Digite aqui o valor: "))
        self.cubo = self.x * self.x * self.x
        print(self.x, " elevado ao cubo é: ", self.cubo)

    def imprime_info(self):
        print(f"Cor = {self.cor}")
        print(f"Memoria = {self.memoria}")
        

    

    


class FuncionarioCaixa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
  
    def imprime_info(self):
        print(f"Nome = {self.nome}")
        print(f"Endereço = {self.endereco}")
    
    def main2(self):
        print()
        b = input("Informe o seu nome: ")
        a = input("Informe o seu endereço: ")
        p = FuncionarioCaixa (a, b)


        escolha = int(input("Deseja iniciar a calculadora? Digite 1 para sim e 2 para não: "))
        if escolha == 1:
            b = []
            a = []
            x = []
            y = []
            r = Calculadora(b, a, x, y)
            r.main()
            p.imprime_info()
            print()


if __name__ == '__main__':
    b = []
    a = []
    p = FuncionarioCaixa(a, b)
    p.main2()
