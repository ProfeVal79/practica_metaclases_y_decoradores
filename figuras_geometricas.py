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

#instancia
c = Cuadrado(lado = 5)
r = Circulo(radio = 3)

formas = [c, r]
print(f"Sistema de Geometría Dinámico")
for f in formas:
    f.calcular_area()
    f.calcular_perimetro()

