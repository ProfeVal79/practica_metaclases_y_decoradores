def dice(self):
    return "guauuu"
Animal = type("Animal",() ,{"cantidad_patas":4, "especie" : "mamifero" })
Perro = type("Perro", (Animal, ), dict(raza = "Dogo", nombre = "Firulais", dice = dice))
Gato = type("Gato", (Animal, ), dict(raza = "Siames", nombre = "minino", dice = "miauu"))
Raton = type("Raton", (Animal, ), dict(raza = "Casero", nombre = "Juan", dice = "Squeak"))
Conejo = type("Conejo", (Animal, ), dict(raza = "Balier", nombre = "Orejas", dice = "Crup - crup"))

p = Perro()
g = Gato()
r = Raton()
c = Conejo()
print(f"Hola soy {g.nombre}, mi raza es {g.raza} soy {g.especie} tengo {g.cantidad_patas} patas y digo {g.dice}")
print(f"hola soy {p.nombre} mi raza es {p.raza}, soy {p.especie} tengo {p.cantidad_patas} patas y digo {p.dice()}")
print(f"hola soy {r.nombre} mi raza es {r.raza}, soy {r.especie} tengo {r.cantidad_patas} patas y digo {r.dice}")
print(f"hola soy {c.nombre} mi raza es {c.raza}, soy {c.especie} tengo {c.cantidad_patas} patas y digo {c.dice}")

Persona = type("Persona", (),{"nombre": "Pedro", "edad": 45, "sexo": "hombre"})
Empleado = type("Empleado", (Persona, ), dict(puesto = "administración", antiguedad = 40, salario = "$1200000"))

h = Persona()
print(f"hola soy {h.nombre} tengo {h.edad} y soy {h.sexo}")

e = Empleado()
print(f"mi nombre es {e.nombre}, soy empleado en {e.puesto} mi antigüedad es {e.antiguedad} años y mi salario es {e.salario}")

print(Persona.__name__)
