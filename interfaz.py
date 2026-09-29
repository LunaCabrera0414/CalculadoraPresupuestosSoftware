import tkinter as tk
from tkinter import messagebox

def crear_ventana(comando_agregar, comando_procesar):
    ventana = tk.Tk()
    ventana.title("Cotizador de Proyectos Funcional")
    ventana.geometry("450x550")
    ventana.config(padx=20, pady=20)

    tk.Label(ventana, text="Ingreso de Datos", font=("Arial", 12, "bold")).pack(pady=5)

    # Entradas de texto (Inputs)
    tk.Label(ventana, text="Nombre de la Tarea:").pack()
    entry_nombre = tk.Entry(ventana, width=40)
    entry_nombre.pack()

    tk.Label(ventana, text="Categoría (ej. Desarrollo, Administrativo):").pack()
    entry_categoria = tk.Entry(ventana, width=40)
    entry_categoria.pack()

    tk.Label(ventana, text="Horas estimadas:").pack()
    entry_horas = tk.Entry(ventana, width=40)
    entry_horas.pack()

    tk.Label(ventana, text="Tarifa por hora ($):").pack()
    entry_tarifa = tk.Entry(ventana, width=40)
    entry_tarifa.pack()

    etiqueta_contador = tk.Label(ventana, text="Tareas agregadas: 0", fg="blue")
    etiqueta_contador.pack(pady=10)

    # Función interna para capturar los datos ingresados
    def capturar_datos():
        try:
            nombre = entry_nombre.get()
            categoria = entry_categoria.get()
            horas = float(entry_horas.get())
            tarifa = float(entry_tarifa.get())
            
            # Pasamos los datos a la función coordinadora
            comando_agregar(nombre, categoria, horas, tarifa, etiqueta_contador)
            
            # Limpiamos los campos
            entry_nombre.delete(0, tk.END)
            entry_categoria.delete(0, tk.END)
            entry_horas.delete(0, tk.END)
            entry_tarifa.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Las horas y la tarifa deben ser números")

    tk.Button(ventana, text="Agregar Tarea a la Lista", command=capturar_datos).pack(pady=5)

    tk.Label(ventana, text="Procesamiento", font=("Arial", 12, "bold")).pack(pady=15)
    
    etiqueta_resultados = tk.Label(ventana, text="Esperando ejecución...", justify="center", font=("Courier", 10))
    
    # Botón que dispara el pipeline funcional
    tk.Button(ventana, text="Calcular con Filter -> Map -> Reduce", 
              command=lambda: comando_procesar(etiqueta_resultados), 
              bg="#0052cc", fg="white").pack(pady=5)
              
    etiqueta_resultados.pack(pady=10)

    return ventana