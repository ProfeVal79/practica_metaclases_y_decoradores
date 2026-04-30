import math

def decorador_area(func):
    def envoltura(self):
        resultado = func(self)
        print(f"Cálculo de área para {self.__class__.__name__}")
        print(f"Resultado {resultado: .2f}")
    return envoltura

def decorador_perimetro(func):
    def envoltura(self):
        resultado = func(self)
        print(f"cálculo perímetro para {self.__class__.__name__}")
        print(f"Resultado {resultado: .2f}")
    return envoltura

def __init__(self, **kwargs):   #usamos kwargs para que cada figura reciba lo que necesite (lado, radio,etc)
    for clave, valor in kwargs.items():
        setattr(self, clave, valor)
@decorador_area
def calcular_area(self):
    return self.formula_area()

@decorador_perimetro
def calcular_perimetro(self):
  return self.formula_perimetro()

Figura = type("Figura", (), {"__init__": __init__, "calcular_area": calcular_area, "calcular_perimetro": calcular_perimetro})
Cuadrado = type("Cuadrado", (Figura, ), {"formula_area": lambda self: self.lado ** 2, "formula_perimetro": lambda self: self.lado * 4})
Circulo = type("Circulo", (Figura, ), {"formula_area": lambda self: math.pi * (self.radio ** 2), "formula_perimetro": lambda self: 2 * math.pi * self.radio})
Triangulo = type("Triangulo", (Figura, ), {"formula_area": lambda self: (self.base * self.altura)/2, "formula_perimetro": lambda self: self.lado1 + self.lado2 + self.lado3})
Poligono_Regular = type("Poligono_Regular", (Figura, ), {"formula_area": lambda self: (self.n_lados * self.lado ** 2) / 4 * math.tan(math.pi / self.n_lados), "formula_perimetro": lambda self: self.n_lados * self.lado})

#lambda self: --> lambda es una palabra reservada de python que sirve para crear funciones anonimas (sin nombre) de una sola linea,
#lambda me permite "empaqutar" la formula y guardarla como valor dentro del diccionario. 
#instancia
c = Cuadrado(lado = 5)
r = Circulo(radio = 3)
t = Triangulo(base = 10, altura = 8, lado1 = 10, lado2 = 10, lado3 = 12)
penta = Poligono_Regular()
penta.n_lados = 5
penta.lado = 6


formas = [c, r, t, penta]
print(f"Sistema de Geometría Dinámico")
for f in formas:
    f.calcular_area()
    f.calcular_perimetro()

