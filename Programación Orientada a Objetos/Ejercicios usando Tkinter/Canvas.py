import tkinter as tk

def dibujar(event):
    canvas.create_line(event.x, event.y, event.x + 1, event.y + 1)

ventana = tk.Tk()
ventana.title("Ejercicio 5")



canvas = tk.Canvas(ventana, width=400, height=300, bg="white")
canvas.pack()


canvas.bind("<B1-Motion>", dibujar)

ventana.mainloop()
