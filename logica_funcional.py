"""
Archivo: logica_funcional.py
Propósito: Contener el núcleo de la lógica de procesamiento de datos.
Todo aquí se basa en el flujo: datos → función → función → resultado.
"""
from functools import reduce

def iterador_tareas(tareas):
    """
    Generador que implementa evaluación perezosa.
    """
    for tarea in tareas:
        yield tarea

def calcular_presupuesto(tareas):
    """
    Función pura que encadena el pipeline funcional (Filter -> Map -> Reduce).
    Recibe los datos originales y retorna un diccionario con los resultados.
    """
    # 1. FILTER: Selecciona elementos mediante un predicado.
    # El predicado (lambda) devuelve True si la categoría no es "Administrativo".
    tareas_facturables = list(filter(lambda t: t[1] != "Administrativo", iterador_tareas(tareas)))

    # 2. MAP: Aplica una transformación a cada elemento.
    # Multiplica la posición 2 (Horas) por la posición 3 (Tarifa).
    costos = list(map(lambda t: t[2] * t[3], tareas_facturables))

    # 3. REDUCE: Acumula y combina muchos valores en uno solo.
    # Suma todos los elementos de la lista de costos.
    if costos:
        total = reduce(lambda a, b: a + b, costos)
    else:
        total = 0

    # 4. Comprensiones de listas: Estilo idiomático en Python.
    # Extraemos solo el nombre de las tareas (posición 0) para mostrar en la interfaz.
    nombres_facturables = [t[0] for t in tareas_facturables]

    # Retorna un nuevo conjunto de datos sin haber modificado la tupla original.
    return {
        "nombres": nombres_facturables,
        "costos_parciales": costos,
        "total": total
    }