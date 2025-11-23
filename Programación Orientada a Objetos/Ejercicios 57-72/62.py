#Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="Ingrese nombre")
        self.label1.grid(column=0, row=0)
        self.nombre=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=40, textvariable=self.nombre)
        self.entry1.grid(column=0, row=1)
        self.label2=tk.Label(self.ventana1,text="Seleccione país")
        self.label2.grid(column=0, row=2)
        self.listbox1=tk.Listbox(self.ventana1)
        self.listbox1.grid(column=0,row=3)
        self.listbox1.insert(0,"Argentina")
        self.listbox1.insert(1,"Chile")
        self.listbox1.insert(2,"Bolivia")
        self.listbox1.insert(3,"Paraguay")
        self.listbox1.insert(4,"Brasil")
        self.listbox1.insert(5,"Uruguay")
        self.boton1=tk.Button(self.ventana1, text="Recuperar", command=self.mostrardatos)
        self.boton1.grid(column=0, row=4)        
        self.ventana1.mainloop()

    def mostrardatos(self):
         if len(self.listbox1.curselection())!=0:
            self.ventana1.title("Nombre:"+self.nombre.get()+" Pais:"+self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1=Aplicacion()