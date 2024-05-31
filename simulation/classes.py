from abc import ABC, abstractmethod
import random
from numpy import log

PROB_PRODUCTOS = [
    (1, 0, 0.32),
    (2, 0.33, 0.65),
    (3, 0.66, 0.9999),
]

def get_rand():
    rnd = round(random.uniform(0, 1), 4)
    if rnd == 1:
        rnd = 0.9999
    return rnd

#actúa como una clase base abstracta (ABC) 
class Evento(ABC):
    def __init__(self, id, rand=0, valor=0, valor_reloj=0, valor_formula=0, *args, **kwargs):
        self.id = id
        self.rand = rand
        self.valor = valor
        self.valor_reloj = valor_reloj
        self.valor_formula = valor_formula

# Devuelve una representación del evento en forma de diccionario.
    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def calc_valor_reloj(self, reloj):
        pass

    def reset(self):
        self.rand = 0
        self.valor = 0
        self.valor_reloj = 0
   
class LlegadaCliente(Evento):
    def __init__(self, estado="Libre", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.estado = estado

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Cliente Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = -3*log(1-self.rand)
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(LlegadaCliente, self).reset()
        self.id_grupo = 0

class Cliente:
    def __init__(self, id, estado, hora_llegada=0):
        self.id = id
        self.estado = estado
        self.hora_llegada = hora_llegada


    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            d[f"G {self.id} - {llave}"] = valor
        return d
