import tkinter as tk

def agregar():
    lista.insert(tk.END, entrada.get())
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Ejercicio 4")
ventana.geometry("400x400")

lista = tk.Listbox(ventana)
lista.pack()


entrada = tk.Entry(ventana)
entrada.pack()


boton = tk.Button(ventana, text="Agregar", command=agregar)
boton.pack()

ventana.mainloop()
