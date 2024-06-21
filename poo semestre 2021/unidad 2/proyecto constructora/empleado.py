from Tkinter import*
#from Datos import DatosComunes
#from Interface import Funciones
from excepciones import EspacioBlanco, Negativos, ECorreo, ETelefono
class Trabajador():
#class Trabajador(DatosComunes, Funciones):
    def __init__(self):
        self.ventana = Toplevel()
        self.ventana.geometry("1200x1500")
        self.ventana.config(bg="orange")
        self.ventana.config(cursor="cross")
        self.ventana.config(relief="sunken")
        self.ventana.title("EMPLEADOS")
        etiquta = Label(self.ventana, font=("Arial", 16), fg='blue', text="MATERIALES EL PROYECTO DE ESTRELLITA",bg="orange").place(x=400, y=25)
        etiqueta = Label(self.ventana, font=("Arial", 12), fg='cyan', text="con calidad dura mas", bg="orange").place(x=500, y=50)
        etiqueta = Label(self.ventana, font=("Arial", 10), fg='black', text="EMPLEADOS",bg="orange").place(x=550, y=75)
        self.nombre = StringVar()
        etiquta = Label(self.ventana, text="Nombre del trabajador", bg="orange").grid(row=1, column=2)
        texto = Entry(self.ventana, textvariable=self.nombre).grid(row=1, column=3, padx=5, pady=60)
        self.telefono = StringVar()
        etiqueta = Label(self.ventana, text="Telefono del trabajador", bg="orange").grid(row=2, column=2)
        texto = Entry(self.ventana, textvariable=self.telefono).grid(row=2, column=3, padx=5, pady=65)
        self.correo = StringVar()
        etiqueta = Label(self.ventana, text="Correo del trabajador", bg="orange").grid(row=3, column=2)
        texto = Entry(self.ventana, textvariable=self.correo).grid(row=3, column=3, padx=5, pady=70)
        self.rango = StringVar()
        etiqueta = Label(self.ventana, text="Rango del trabajador", bg="orange").grid(row=4, column=2)
        texto = Entry(self.ventana, textvariable=self.rango).grid(row=4, column=3, padx=5, pady=75)
        self.id = StringVar()
        etiquta = Label(self.ventana, text=" ID del empleado ", bg="orange").grid(row=4, column=2)
        texto = Entry(self.ventana, textvariable=self.id).grid(row=4, column=3, padx=5, pady=75)
        bot = Button(self.ventana, text="Agregar", bg='cyan', command=self.guardar).place(x=100, y=600)
        bot = Button(self.ventana, text="Baja", bg='cyan',command=self.baja).place(x=200, y=600)
        bot = Button(self.ventana, text="Actualizar", bg='cyan', command=self.ActualizacionTrabajador).place(x=300, y=600)
        bot = Button(self.ventana, text="Generar ID", bg='cyan',command=self.generarID).place(x=400, y=600)
        bot = Button(self.ventana, text="Password", bg='cyan',command=self.password).place(x=500, y=600)
        bot = Button(self.ventana, text="Volver", bg='cyan',command=self.volverMenu).place(x=350, y=650)
    def guardar(self):
        try:
            self.nomTrabajador = self.nombre.get()
            if self.nomTrabajador=="":
                raise EspacioBlanco
            self.correoTrabajador = self.correo.get()
            if self.correoTrabajador=="":
                raise EspacioBlanco
            arroba = False
            longcor = len(self.correoTrabajador)
            s = 0
            while s < longcor:
                m = self.correoTrabajador[s]
                if m == '@':
                    arroba = True
                s = s + 1
            if arroba == False:
                raise ECorreo
            self.telTrabajador = self.telefono.get()
            if self.telTrabajador=="":
                raise EspacioBlanco
            long = len(self.telTrabajador)
            if long != 10:
                raise ETelefono
            self.rangoTrabajador = self.rango.get()
            if self.rangoTrabajador=="":
                raise EspacioBlanco
            self.idTrabajador = self.id.get()
            if self.idTrabajador=="":
                raise EspacioBlanco
            Lista_Trabajadores = open("Lista de Trabajadores.txt", 'a')
            Lista_Trabajadores.write("   ")
            Lista_Trabajadores.write(self.nomTrabajador)
            Lista_Trabajadores.write("    ")
            Lista_Trabajadores.write(self.correoTrabajador)
            Lista_Trabajadores.write("           ")
            Lista_Trabajadores.write(self.telTrabajador)
            Lista_Trabajadores.write("            ")
            Lista_Trabajadores.write(self.rangoTrabajador)
            Lista_Trabajadores.write("         ")
            Lista_Trabajadores.write(self.idTrabajador)
            Lista_Trabajadores.write("\n")
            Lista_Trabajadores.close()
            self.agregar()
        except EspacioBlanco as e:
            pass
        except ECorreo as e:
            pass
        except ETelefono as e:
            pass
    def eliminar(self):
        print "si elimino"
        self.venGua.destroy()
    def ActualizacionTrabajador(self):
        pass
    def generarID(self):
        pass
    def password(self):
        pass
    def volverMenu(self):
        self.ventana.destroy()
    def baja(self):
        self.venGua = Tk()
        self.venGua.iconbitmap("Icono.ico")
        self.venGua.geometry("300x100")
        self.venGua.config(bg="orange")
        self.venGua.title("Remover")
        anuncioQuitar = Label(self.venGua, text="Removido con exito", fg="navy", bg="orange", font=("Arial", 15))
        anuncioQuitar.place(x=30, y=0)
        btnInicio = Button(self.venGua, text="Cancelar", bg='cyan', command=self.cerrar)
        btnInicio.place(x=50, y=50)
        btnInicio = Button(self.venGua, text="OK", bg='cyan', command=self.eliminar)
        btnInicio.place(x=150, y=50)
        self.venGua.mainloop()
#e=Trabajador()
#e.guardar()