import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Hola, mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz Gráfica")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a mi aplicación")
etiqueta.pack(pady=10)  # Añadir un espacio entre la etiqueta y otros widgets

# Crear un botón
boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack(pady=10)  # Añadir un espacio entre el botón y otros widgets

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
