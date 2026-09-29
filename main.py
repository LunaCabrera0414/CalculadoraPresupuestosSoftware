from logica_funcional import calcular_presupuesto
from interfaz import crear_ventana

# Esta lista temporal actúa como recolector de los datos del usuario en la interfaz.
# (Pertenece a la capa imperativa, no a la lógica funcional)
recolector_tareas = []

def coordinador_agregar(nombre, categoria, horas, tarifa, etiqueta_contador):
    """Agrega temporalmente la tarea ingresada por el usuario."""
    recolector_tareas.append((nombre, categoria, horas, tarifa))
    etiqueta_contador.config(text=f"Tareas agregadas: {len(recolector_tareas)}")

def coordinador_procesar(etiqueta_destino):
    """Convierte los datos a formato inmutable y los pasa al pipeline."""
    # 1. Disciplina funcional: Convertimos la lista dinámica en una TUPLA inmutable
    # antes de enviarla a la lógica, asegurando que no se pueda modificar.
    datos_inmutables = tuple(recolector_tareas)
    
    # 2. Los datos originales entran a la función pura
    resultados = calcular_presupuesto(datos_inmutables)
    
    # 3. Formateamos y enviamos a la pantalla (efecto secundario)
    texto = (
        f"--- Tareas Facturables (Filter) ---\n"
        f"{', '.join(resultados['nombres']) if resultados['nombres'] else 'Ninguna'}\n\n"
        f"--- Presupuesto Total (Reduce) ---\n"
        f"${resultados['total']:,.2f}"
    )
    etiqueta_destino.config(text=texto)

def iniciar_aplicacion():
    # Pasamos ambas funciones como "funciones de orden superior" a la interfaz
    ventana_principal = crear_ventana(coordinador_agregar, coordinador_procesar)
    ventana_principal.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()