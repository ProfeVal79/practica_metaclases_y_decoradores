def __init__(self, tipo, marca, modelo, ruedas, color):
   self.tipo = tipo
   self.marca = marca
   self.modelo = modelo
   self.ruedas = ruedas
   self.color = color

def detalles(self):
    return f"Detalles del vehiculo:\n Tipo: {self.tipo}\n Marca: {self.marca}\n Modelo: {self.modelo}\n Cantidad de Ruedas: {self.ruedas}\n Color: {self.color}"

Vehiculo = type("Vehiculo", (), {"__init__": __init__, "detalles": detalles})

def __init__auto(self, tipo, marca, modelo, ruedas, color, puertas, es_automatico):
    Vehiculo.__init__(self, tipo, marca, modelo, ruedas, color)
    self.puertas = puertas
    self.es_automatico = es_automatico
   

def detalles_auto(self):
    detalles_base = Vehiculo.detalles(self)
    transmision = "Automatico" if self.es_automatico else "Manual"
    return f"{detalles_base}\n Puertas: {self.puertas}\n Transmision: {transmision}"

Auto = type("Auto", (Vehiculo, ), {"__init__": __init__auto, "detalles": detalles_auto})

def __init__moto(self, tipo, marca, modelo, ruedas, color, cilindrada, tipo_manubrio):
    Vehiculo.__init__(self, tipo, marca, modelo, ruedas, color)
    self.cilindrada = cilindrada
    self.tipo_manubrio = tipo_manubrio
    

def detalles_moto(self):
    detalles_base = Vehiculo.detalles(self) 
    return f"{detalles_base}\n Cilindrada: {self.cilindrada} cc\n Manubrio: {self.tipo_manubrio}"

Moto = type("Moto", (Vehiculo, ), {"__init__": __init__moto, "detalles": detalles_moto})




mi_auto = Auto("Auto", "Toyota", "Corolla", 4, "Gris", 4, False)
print(mi_auto.detalles())
print("_" * 25)
mi_moto = Moto("Motocicleta", "Honda", "CB650R", 2, "Negro", 650, "Deportivo")
print(mi_moto.detalles())
print("_" * 25)
otro_auto = Auto("Camioneta", "Toyota", "Hilux", 4, "Blanco", 4, True)
print(otro_auto.detalles())