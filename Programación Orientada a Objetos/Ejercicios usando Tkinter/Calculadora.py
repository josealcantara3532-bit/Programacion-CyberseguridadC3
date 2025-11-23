import tkinter as tk

def sumar():
    n1 = float(num1.get())
    n2 = float(num2.get())
    resultado.config(text=f"Resultado: {n1 + n2}")

ventana = tk.Tk()
ventana.title("Ejercicio 3")
ventana.geometry("400x400")

tk.Label(ventana, text="Número 1:").pack()
num1 = tk.Entry(ventana)
num1.pack()



tk.Label(ventana, text="Número 2:").pack()
num2 = tk.Entry(ventana)
num2.pack()

boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack()

resultado = tk.Label(ventana, text="Resultado: ")
resultado.pack()

ventana.mainloop()
