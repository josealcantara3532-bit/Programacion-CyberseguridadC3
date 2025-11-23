#Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario.
#Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.radio1=tk.Radiobutton(self.ventana1,text="Rojo", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1,text="Verde", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.radio2=tk.Radiobutton(self.ventana1,text="Azul", variable=self.seleccion, value=3)
        self.radio2.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text="Cambiar color", command=self.activar)
        self.boton1.grid(column=0, row=3)
        self.ventana1.mainloop()        

    def activar(self):
        if self.seleccion.get()==1:
            self.ventana1.configure(bg="red")
        if self.seleccion.get()==2:
            self.ventana1.configure(bg="green")
        if self.seleccion.get()==3:
            self.ventana1.configure(bg="blue")

aplicacion1=Aplicacion()