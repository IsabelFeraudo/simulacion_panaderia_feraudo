from .classes2 import *

class Cliente:
    def __init__(self, id_cliente, estado):
        self.id_cliente = id_cliente
        self.estado = estado
        # Otros atributos necesarios para el cliente

class Panadero:
    def __init__(self, id_panadero, estado):
        self.id_panadero = id_panadero
        self.estado = estado
        # Otros atributos necesarios para el panadero

class Horno:
    def __init__(self, estado):
        self.estado = estado
        # Otros atributos necesarios para el horno

# Definir otras clases necesarias para el sistema de la panadería

def llegada_cliente():
    # Lógica para el evento de llegada de un cliente

def fin_atencion_panadero(panadero):
    # Lógica para el evento de finalización de la atención por parte de un panadero

def proximo_encendido_horno():
    # Lógica para determinar cuándo encender el horno

def fin_calentado():
    # Lógica para el evento de finalización del calentado del horno

def fin_coccion():
    # Lógica para el evento de finalización de la cocción en el horno

# Otros métodos y funciones necesarios para la simulación

def simulacion_panaderia(desde, cantidad_mostrar, total, media_llegada_cliente):
    # Lógica principal de la simulación
    # Usar las clases y funciones definidas anteriormente para simular el funcionamiento de la panadería

    # Retornar resultados de la simulación

# Lógica para la interfaz de usuario y la ejecución de la simulación

