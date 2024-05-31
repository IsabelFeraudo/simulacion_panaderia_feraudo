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
    def __init__(self, estado="Esperando Atencion", id_cliente=0,valor_formula=3,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.estado = estado
        self.id_cliente = id_cliente

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Cliente Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = -self.valor_formula*log(1-self.rand)
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(LlegadaCliente, self).reset()
        self.id_grupo = 0

class Cliente:
    def __init__(self, id, estado, hora_llegada=0,abandona=False):
        self.id = id
        self.estado = estado
        self.hora_llegada = hora_llegada
        self.abandona= abandona


    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            d[f"G {self.id} - {llave}"] = valor
        return d
    
    def calc_cant_productos(self):
        self.rnd_cant_personas = get_rand()
        for i in PROB_PRODUCTOS:
            if i[1] <= self.rnd_cant_productos <= i[2]:
                self.cant_productos = i[0]
                
    #calcular abandono

#COMO HACERLO PARA DOS CAJAS?
class FinAtencion(Evento):
    def __init__(self, estado="Libre", id_cliente=0,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.estado = estado
        self.id_cliente = id_cliente

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Cliente Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = 0.5+(self.rand)*(1.5-0.5)
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(FinAtencion, self).reset()
        self.id_cliente = 0
        
class FinEspera(Evento):
    def __init__(self, id_cliente=0,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id_cliente = id_cliente

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Cliente Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = 5
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(FinEspera, self).reset()
        self.id_cliente = 0
        
class FinCoccion(Evento):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      

    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Cliente Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        self.valor = 0 #programar ec dif
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(FinCoccion ,self).reset()
        self.id_cliente = 0
        
class ProximoEncendido(Evento):
    def __init__(self, estado="Apagado",*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.estado = estado
    
    def to_dict(self):
        d = {}
        for llave, valor in self.__dict__.items():
            if llave == "id" or llave == "valor_formula":
                continue
            d[f"Horno Est {self.id} - {llave}"] = valor
        return d

    def calc_valor_reloj(self, reloj):
        self.rand = get_rand()
        #calcular valor de proximo encendido. vada 45 min o cuando no haya stock
        self.valor = 0
        self.valor_reloj = reloj + self.valor

    def reset(self):
        super(FinAtencion, self).reset()
        self.id_cliente = 0
        
#clase panadero 1 y 2?