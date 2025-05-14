class Ingresso:
    def __init__(self,valor):
        self.valor = valor

    def imprimeValor(self):
        print(f'Valor do ingresso: R${self.valor:.2f}')


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor*1.5)

    def imprimeValor(self):
        print(f'Valor do ingresso VIP: R${self.valor:.2f}')

class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calculoArea(self, base, altura):
        self.area = base * altura
        print(f'Area do retangulo = {self.area}')

    def calculoPerimetro(self, base, altura):
        self.perimetro = (base + altura) * 2
        print(f'Perimetro = {self.perimetro}')

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculoArea(self):
        self.area = (self.base * self.altura)/2
        print(f'Area do retangulo = {self.area}')

    def calculoPerimetro(self):
        self.perimetro = self.base * 3
        print(f'Perimetro = {self.perimetro}')