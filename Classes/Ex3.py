o = 0

class IRSimplificado():
    def __init__(self, nome, nascimento, profissao, escolaridade, renda_mensal, dependentes):
        self.nome = nome
        self.nascimento = nascimento
        self.profissao = profissao
        self.escolaridade = escolaridade
        self.renda_mensal = renda_mensal
        self.dependentes = dependentes

    def calcular_idade(self):
        self.idade = 2024 - self.nascimento
    
    
    def aliquota_ir_max(self):
        if self.renda_mensal < 2259.20:
            print("Você não paga imposto de renda")

        if self.renda_mensal > 2259.20 and self.renda_mensal < 2826.65:
            o = 1
            print("Você paga 7,5% de imposto de renda")
            self.imposto_renda = self.renda_mensal * 0.075
            print(f"Você paga {self.imposto_renda} de imposto de renda")

        if self.renda_mensal > 2826.65 and self.renda_mensal < 3751.05:
            o = 2
            print("Você paga 15% de imposto de renda")
            self.imposto_renda = self.renda_mensal * 0.15
            print(f"Você paga {self.imposto_renda} de imposto de renda")
        
        if self.renda_mensal > 3751.05 and self.renda_mensal < 4664.68:
            o = 3
            print("Você paga 22.5% de imposto de renda")
            self.imposto_renda = self.renda_mensal * 0.225
            print(f"Você paga {self.imposto_renda} de imposto de renda")
        
        if self.renda_mensal > 4664.67:
            o = 4
            print("Você paga 27.5% de imposto de renda")
            self.imposto_renda = self.renda_mensal * 0.275
            print(f"Você paga {self.imposto_renda} de imposto de renda")
    
    def calcular_renda_anual(self):
        self.renda_anual = (self.renda_mensal - self.imposto_renda) * 12
    
    def valor_deducao(self):
        if o == 1:
            print("O valor de dedução é de R$ 169,44")
        if o == 2:
            print("O valor de dedução é de R$ 381,44")
        if o == 3:
            print("O valor de dedução é de R$ 662,77")
        if o == 4:
            print("O valor de dedução é de R$ 896,00")
        


    def imprime_info(self):
        print(f"Nome = {self.nome}")
        print(f"Idade = {self.idade}")
        print(f"Renda anual = {self.renda_anual}")

    

def main():
    
    print()
    n = input("Digite aqui seu nome: ")
    na = int(input("Digite aqui seu ano de nascimento: "))
    p = input("Digite aqui sua profissão: ")
    e = input("Digite aqui seu grau de escolaridade: ")
    rm = float(input("Digite aqui sua renda mensal: "))
    d = int(input("Digite aqui o número de dependentes: "))
    print()

    x = IRSimplificado(n, na, p, e, rm, d)
    x.calcular_idade()
    print()
    x.aliquota_ir_max()
    print()
    x.valor_deducao()
    print()
    x.calcular_renda_anual()
    print()
    x.imprime_info()
    print()

if __name__ == '__main__':
    main()
