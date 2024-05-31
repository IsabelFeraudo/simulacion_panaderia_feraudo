#retorna el proximo evento
def get_min_reloj(llegada_cliente, lista_fin_atencion, encendido_horno, fin_coccion, lista_fin_espera):
    lista = [llegada_cliente,encendido_horno, fin_coccion] + lista_fin_atencion+ lista_fin_espera
    val = [0, None]
    for i in lista:
        if val[0] == 0:
            val[0] = i.valor_reloj
            val[1] = i
        else:
            if i.valor_reloj < val[0] and i.valor_reloj != 0:
                val[0] = i.valor_reloj
                val[1] = i
    return val

#Busca el panadero libre para aignarle un cliente posteriormente
def panadero_libre(lista_panaderos):
    for i in range(len(lista_panaderos)):
        if lista_panaderos[i].estado == "Libre":
            return i
    return False

#Devuelve la cola mas corta
def mandado_a_cola(lista):
    indice = -1
    for i in range(len(lista)):
        if indice == -1:
            indice = i
        if len(lista[i]) < len(lista[indice]):
            indice = i
    return indice