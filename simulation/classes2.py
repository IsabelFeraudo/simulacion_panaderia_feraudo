import random
from numpy import log

class Evento:
    def __init__(self, id, rand=0, valor=0, valor_reloj=0, valor_formula=0):
        self.id = id
        self.rand = rand
        self.valor = valor
        self.valor_reloj = valor_reloj
        self.valor_formula = valor_formula

    def reset(self):
        self.rand = 0
        self.valor = 0
        self.valor_reloj = 0

class LlegadaCliente(Evento):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Llegada Cliente - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = -self.valor_formula * log(1 - self.rand)
        self.valor_reloj = reloj + self.valor

class FinAtencion(Evento):
    def __init__(self, panadero_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.panadero_id = panadero_id

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Fin Atencion - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = -self.valor_formula * log(1 - self.rand)
        self.valor_reloj = reloj + self.valor

class Horno:
    def __init__(self, temperatura=5, estado="Apagado", *args, **kwargs):
        self.temperatura = temperatura
        self.estado = estado

    def encender(self):
        self.estado = "Calentando"
        # Lógica para encender el horno y calcular la temperatura

    def hornear(self, cantidad_productos):
        self.estado = "Horneando"
        # Lógica para hornear productos y calcular la temperatura

class Panadero:
    def __init__(self, id, estado="Libre", *args, **kwargs):
        self.id = id
        self.estado = estado

    def atender_cliente(self, cliente):
        self.estado = "Ocupado"
        # Lógica para atender al cliente

class Cliente:
    def __init__(self, id, estado="Esperando atencion", cantidad_productos=0, *args, **kwargs):
        self.id = id
        self.estado = estado
        self.cantidad_productos = cantidad_productos

    def esperar_atencion(self):
        self.estado = "Esperando atencion"

    def recibir_atencion(self):
        self.estado = "Siendo atendido"
        # Lógica para recibir atención del panadero

def get_rand():
    rnd = round(random.uniform(0, 1), 4)
    if rnd == 1:
        rnd = 0.9999
    return rnd

