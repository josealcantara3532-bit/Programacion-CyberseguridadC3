import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejercicio 1")
ventana.geometry("400x400") 

mensaje = tk.Label(ventana, text="¡Bienvenido a Tkinter!")
mensaje.pack()

ventana.mainloop()
