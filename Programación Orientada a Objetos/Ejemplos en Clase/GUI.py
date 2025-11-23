import tkinter as tk
from tkinter import messagebox

def saludar():
    
        messagebox.showinfo("Saludo ","¡Hola Mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera GUI")
ventana.geometry("400x400")

# Crear un botón y asignarle la función saludar
boton=tk.Button(ventana, text="Haz clic aquí", command=saludar )
boton.pack(pady=100)

# Iniciar el bucle principal de la GUI
ventana.mainloop()
    
