import json

def agregar_a_lista(lista: list,nombre:str,puntaje:int):
    '''
    controla y cambia la variable utilizada como indice de las listas paralelas.

    parametros:
    nombre (str): variable que contiene el nombre del jugador.
    puntaje (int): variables que contiene la puntuacion del jugador.
    lista (list): lista donde se guardan todos los jugadores y sus puntajes.

    Retorna:
    lista (list)
    '''
    persona = {}
    persona["nombre"] = nombre
    persona["puntaje"] = puntaje
    lista.append(persona)

    return lista

def leer_json(path: str):
    """
    Lee un archivo JSON y retorna su contenido.

    Parámetros:
    path (str): Ruta del archivo JSON.

    Retorna:
    retorno (list|bool): Lista con los datos del archivo JSON si se lee correctamente, de lo contrario False.
    """
    try:
        with open(path, 'r') as archivo:
            data = json.load(archivo)
            retorno = data
    except:
        print("ERROR, NO SE PUDO ABRIR EL ARCHIVO.")
        retorno = False

    return retorno

def guardar_json(lista: list, path: str):
    """
    Guarda una lista en un archivo JSON.

    Parámetros:
    lista (list): Lista de diccionarios que se guardarán en el archivo.
    path (str): Ruta del archivo JSON.

    Retorna:
    None
    """
    try:
        with open(path, 'w+') as archivo:
            json.dump(lista, archivo, ensure_ascii=False, indent=4)
        print(f"Lista guardada exitosamente en '{path}'.")
    except:
        print(f"Ocurrió un error al guardar el archivo JSON")

def ordenar_por_clave(lista_diccionarios:list, clave = "puntaje"):
    """
    Ordena una lista de diccionarios por una clave específica.

    Parámetros:
    lista_diccionarios (list): Lista de diccionarios que contiene los servicios.
    clave (str): Clave por la cual se ordenará la lista.

    Retorna:
    lista_ordenada (list): Lista de diccionarios ordenada por la clave especificada.
    """
    lista_ordenada = sorted(lista_diccionarios, key = lambda diccionario: diccionario[clave], reverse = True)
    return lista_ordenada

def cambiar_pregunta(contador_indices: int, lista: list):
    '''
    controla y cambia la variable utilizada como indice de las listas paralelas.

    parametros:
    contador_indices (int): variables utilizada como indice de listas.
    lista (list): lista utilizada para controlar que la variable "contador_indice" 
                  no supere el len de las listas.
    Retorna:
    contador_indices (int)
    '''
    if contador_indices < (len(lista)-1):
        contador_indices += 1
    else:
        contador_indices = 0

    return contador_indices
