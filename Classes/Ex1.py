class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        self.area = base * altura
        print()
        print(f"base = {self.base}")
        print(f"altura = {self.altura}")
        print(f"area = {self.area}")
        print()

    
    def calcula_area(self) -> float:
        return self.base * self.altura
        
    

def main():
    print()
    b = float(input("Informe a base do retângulo: "))
    a = float(input("Informe a altura do retângulo: "))
    print()
    r = Retangulo(b, a)
    r.calcula_area()

if __name__ == '__main__':
    main()
    