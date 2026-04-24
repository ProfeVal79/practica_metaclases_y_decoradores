def decorador_voz(func):
    def envoltura(self):
     print(f"{self.__class__.__name__} se prepara...")
     func(self)
     print("fin de la comunicación")
    return envoltura


def __init__(self, nombre, edad = -1):
        self.nombre = nombre
        self.edad = edad
        self.texto_hablar = getattr(self, "texto_hablar", "algo") #getattr--> funcion que sirve para acceder al valor de un atributo

@decorador_voz
def hablar(self):
    print(f"soy {self.nombre} y digo {self.texto_hablar}")

Animal = type("Animal", (), {"__init__": __init__, "hablar": hablar})

Perro = type("Perro", (Animal, ), {"texto_hablar": "Guauu"})
Gato = type("Gato", (Animal, ), {"texto_hablar": "Miauu"})
Vaca = type("Vaca", (Animal, ), {"texto_hablar": "Muuuuu"})
Cabra = type("Cabra", (Animal, ), {"texto_hablar": "Beeee!!"})
Oveja = type("Oveja", (Animal, ), {"texto_hablar": "Meee!!"})
Gallo = type("Gallo", (Animal, ), {"texto_hablar": "Kikirikii!!"})

#Instancias: 

p = Perro("Firulais", 6)
g = Gato("Michi", 3)
v = Vaca("Florencia", 4)
c = Cabra("Esmeralda", 3)
o = Oveja("Lourdes", 2)
ga = Gallo("Clorindo", 1)
#p.hablar()
#g.hablar()
#v.hablar()
#c.hablar()
#o.hablar()
#ga.hablar()
# Aplicación de Polimorfismo
granja = [p, g, v, c, o, ga]
for animal in granja:
    animal.hablar()