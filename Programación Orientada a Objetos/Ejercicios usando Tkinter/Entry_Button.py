import tkinter as tk

def mostrar_texto():
    resultado.config(text=entrada.get())

ventana = tk.Tk()
ventana.title("Ejercicio 2")
ventana.geometry("400x400")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar", command=mostrar_texto)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
