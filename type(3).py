def __init__(self, nombre, edad, f_nac, nacionalidad, DNI):
    self.nombre = nombre
    self.edad = edad
    self.f_nac = f_nac
    self.nacionalidad = nacionalidad
    self.DNI = DNI


def saludar(self):
    return f"Hola soy {self.nombre} y tengo {self.edad} años"

Persona = type("Persona", (), {"__init__": __init__ , "Presentarse": saludar, "especie": "Humano"})

def mi_cuenta(self, nro_cuenta, titular, saldo_inicial = 0):
    self.nro_cuenta = nro_cuenta
    self.titular = titular
    self.saldo_inicial = saldo_inicial
def mostrar_detalle(self):
    print(f"Nro de cuenta:{self.nro_cuenta}\nTitular: {self.titular.nombre}\nsaldo: ${self.saldo_inicial}")

Cuenta = type("Cuenta", (), {"__init__": mi_cuenta, "detalle": mostrar_detalle})

#instancias:
p1 = Persona("Carlos Peréz", 48, "12/03/1978", "Argentina", "26908549")
#print(p1.Presentarse())
print(f"{p1.Presentarse()}, naci el {p1.f_nac} en {p1.nacionalidad}, mi DNI es:{p1.DNI}")
cuenta_1 = Cuenta("456/65", p1, 500000)
print("Detalle de cuenta bancaria:")
cuenta_1.detalle()