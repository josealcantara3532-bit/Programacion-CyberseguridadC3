#Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese primer valor:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="Ingrese segundo valor:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Sumar", command=self.sumar)
        self.boton1.grid(column=1, row=2)
        self.label3=tk.Label(self.ventana1,text="resultado")
        self.label3.grid(column=1, row=3)
        self.ventana1.mainloop()

    def sumar(self):
        suma=int(self.dato1.get()) + int(self.dato2.get())
        self.label3.configure(text=suma)

aplicacion1=Aplicacion() 

#Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
#Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese nombre de usuario:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=30, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2=tk.Label(text="Ingrese clave:")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana1, text="Ingresar", command=self.ingresar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def ingresar(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana1.title("Correcto")
        else:
            self.ventana1.title("Incorrecto")

aplicacion1=Aplicacion()