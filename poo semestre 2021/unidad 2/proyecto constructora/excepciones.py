from Tkinter import *
class UsuaIncorrecto(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        #self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("205x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="Credenciales Invalidas", fg="navy", bg="orange",
                             font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=75, y=(50))
    def close_window(self):
        self.winequi.destroy()
class EspacioBlancoLogin(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        #self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("290x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="Debes ingresar tus credenciales", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=125, y=(50))
    def close_window(self):
        self.winequi.destroy()
class EspacioBlanco(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("320x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="No puedes dejar casillas en blanco", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=125, y=(50))
    def close_window(self):
        self.winequi.destroy()
class Negativos(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("340x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="No puedes ingresar numero negativos", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=125, y=(50))
    def close_window(self):
        self.winequi.destroy()
class ClienteF(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("290x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="Cliente frecuente es 's' o 'n'", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=125, y=(50))
    def close_window(self):
        self.winequi.destroy()
class ETelefono(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        #self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("385x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="El numero telefonico debe tener 10 digitos", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=180, y=(50))
    def close_window(self):
        self.winequi.destroy()
class ECorreo(Exception):
    def __init__(self):
        self.winequi = Toplevel()
        self.winequi.iconbitmap("Icono.ico")
        self.winequi.geometry("290x100")
        self.winequi.config(bg="orange")
        anuncioCorre = Label(self.winequi, text="Formato de correo invalido", fg="navy", bg="orange",
                                 font=("Arial", 15))
        anuncioCorre.place(x=2, y=0)
        btnInicio = Button(self.winequi, text="Okay", bg='cyan', command=self.close_window)
        btnInicio.place(x=125, y=(50))
    def close_window(self):
        self.winequi.destroy()