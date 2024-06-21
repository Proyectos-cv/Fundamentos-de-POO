#coding=utf-8
from Tkinter import*
import sys
class trabajador():
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.geometry("1200x1500")
        self.ventana.config(bg="orange")
        self.ventana.config(cursor="cross")
        self.ventana.config(relief="sunken")
        self.ventana.title("EMPLEADOS")

        etiqueta = Label(self.ventana, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",
                        bg="orange").place(x=400, y=25)
        etiqueta = Label(self.ventana, font=("Arial", 12), fg='cyan', text="con calidad dura mas", bg="orange").place(
            x=500, y=50)
        etiqueta = Label(self.ventana, font=("Arial", 10), fg='black', text="EMPLEADOS",
                    bg="orange").place(x=550, y=75)
        nombre = StringVar()
        etiquta = Label(self.ventana, text="nombre del trabajador", bg="orange").grid(row=1, column=2)

        texto = Entry(self.ventana, textvariable=nombre).grid(row=1, column=3, padx=5, pady=60)
        telefono = StringVar()
        etiqueta = Label(self.ventana, text="telefono del trabajador", bg="orange").grid(row=2, column=2)
        texto = Entry(self.ventana, textvariable=telefono).grid(row=2, column=3, padx=5, pady=65)
        correo = StringVar()
        etiqueta = Label(self.ventana, text="correo del trabajador", bg="orange").grid(row=3, column=2)
        texto = Entry(self.ventana, textvariable=correo).grid(row=3, column=3, padx=5, pady=70)
        rango = StringVar()
        etiqueta = Label(self.ventana, text="rango del trabajador", bg="orange").grid(row=4, column=2)
        texto = Entry(self.ventana, textvariable=rango).grid(row=4, column=3, padx=5, pady=75)
        id = StringVar()
        etiquta = Label(self.ventana, text=" id del empleado ", bg="orange").grid(row=4, column=2)
        texto = Entry(self.ventana, textvariable=id).grid(row=4, column=3, padx=5, pady=75)

        bot = Button(self.ventana, text="agregar", bg='cyan', command=self.agregarTrabajador).place(x=100, y=600)
        bot = Button(self.ventana, text="baja", bg='cyan',command=self.bajaTrabajador).place(x=200, y=600)
        bot = Button(self.ventana, text="actualizar", bg='cyan', command=self.actualizacionTrabajador).place(x=300, y=600)
        bot = Button(self.ventana, text="generar", bg='cyan',command=self.generarID).place(x=400, y=600)
        bot = Button(self.ventana, text="contraseña", bg='cyan', command=self.password).place(x=500, y=600)
        bot = Button(self.ventana, text="Salir", bg='cyan', command=self.volverMenu).place(x=350, y=650)

    def agregarTrabajador(self):
        pass
    def bajaTrabajador(self):
        pass
    def actualizacionTrabajador(self):
        pass
    def generarID(self):
        pass
    def password(self):
        pass
    def volverMenu(self):
        self.ventana.destroy()