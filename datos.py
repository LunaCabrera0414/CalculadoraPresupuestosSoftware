"""
Archivo: datos.py
Propósito: Almacenar el estado inicial o los datos de entrada del programa.
En el paradigma funcional, estos datos no deben ser modificados durante 
la ejecución (inmutabilidad), solo leídos para generar nuevos resultados.
"""

# Utilizamos una Tupla general que contiene otras Tuplas adentro.
# Las tuplas son inmutables en Python, lo que evita cambios de estado accidentales.
TAREAS_PROYECTO = (
    # Estructura: (Nombre de la tarea, Categoría, Horas estimadas, Tarifa por hora en $)
    ("Diseño de Base de Datos", "Desarrollo", 15, 400),
    ("Reunión de requerimientos", "Administrativo", 3, 0),
    ("Desarrollo de API REST", "Desarrollo", 25, 450),
    ("Configuración de Servidor Linux", "Infraestructura", 10, 500),
    ("Pruebas unitarias", "Calidad", 8, 350),
    ("Gestión de correos y minutas", "Administrativo", 5, 0),
    ("Despliegue en producción", "Infraestructura", 4, 600)
)