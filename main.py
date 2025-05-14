from biblioteca import *

valor = float(input('Digite o valor: '))

cinema = Ingresso(valor)
cinema.imprimeValor()

cineVip = VIP(valor)
cineVip.imprimeValor()

print()

base = float(input('Digite a base: '))
altura = float(input('Digite a altura: '))

r1 = Retangulo()
r1.calculoArea(base, altura)
r1.calculoPerimetro(base, altura)

t1 = Triangulo(base, altura)
t1.calculoArea()
t1.calculoPerimetro()
