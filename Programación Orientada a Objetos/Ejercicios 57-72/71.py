#En una aduana hay una máquina que sortea las personas cuyo equipaje serán revisados.
#La persona selecciona la cantidad de bultos (hacer dicha selección mediante un Spinbox)

#Luego se presiona el botón sortear y aparece al lado de este botón una Label de color rojo o verde (En caso de ser rojo se revisa su equipaje, en caso de ser verde, no se revisa)
#Para el sorteo generar un valor aleatorio entre 1 y 3. Si se genera un 1 se revisa, si se genera un 2 o 3 no se revisa, mostrar un mensaje de error si el Spinbox tiene un cero.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import random

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="Seleccione la cantidad de bultos:")
        self.label1.grid(column=0, row=0, padx=10, pady=10)
        self.spinbox1=ttk.Spinbox(self.ventana1, from_=0, to=100, width=10, state='readonly')        
        self.spinbox1.set(0)        
        self.spinbox1.grid(column=1, row=0, padx=10, pady=10)
        self.boton1=ttk.Button(self.ventana1, text="Sortear", command=self.sortear)
        self.boton1.grid(column=0, row=1, padx=10, pady=10)
        self.label2=ttk.Label(self.ventana1, text="", width=20)
        self.label2.grid(column=1, row=1, padx=10, pady=10)
        self.ventana1.mainloop()

    def sortear(self):
        if int(self.spinbox1.get())==0:
            mb.showerror("Cuidado","Debe seleccionar un valor distinto a cero en bultos")
        else:
            valor=random.randint(1,3)
            if valor==1:
                self.label2.configure(text="Se deben revisar")
                self.label2.configure(background="red")
            else:
                self.label2.configure(text="No se revisan")
                self.label2.configure(background="green")

aplicacion1=Aplicacion() 