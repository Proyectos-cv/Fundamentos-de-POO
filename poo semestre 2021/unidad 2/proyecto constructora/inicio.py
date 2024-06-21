# -*- coding: utf-8 -*-
#!/usr/bin/env python
from Tkinter import *
import sys
from principal import Principal
from excepciones import UsuaIncorrecto
from excepciones import EspacioBlancoLogin
#from MenuPrincipal import Principal
class LoginPunto:
    def __init__(self):
        self.venUser=Tk()
        self.venUser.geometry("700x300")
        self.venUser.config(bg="orange")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        #self.venUser.iconbitmap("Icono.ico")
        self.venUser.title("INICIO DE SESION")
        #imagen=PhotoImage(file="Login.gif")
        #fondo=Label(self.venUser,image=imagen)
        #fondo.place(x=380, y=20)
        lblEti = Label(self.venUser, text="El proyecto de Estrellita",fg="navy", bg="orange",font=("Arial",15))
        lblEti.place(x=100, y=(0))
        lblEti= Label(self.venUser,text="Usuario",bg="orange")
        lblEti.place(x=0,y=(100))
        self.usuario= StringVar()
        self.cajaUser = Entry(self.venUser, textvariable=self.usuario)
        self.cajaUser.place(x=70,y=(100))
        lblEti = Label(self.venUser, text="Contraseña", bg="orange")
        lblEti.place(x=0,y=(150))
        self.password = StringVar()
        self.cajaPass = Entry(self.venUser,show="*", textvariable=self.password)
        self.cajaPass.place(x=70,y=(150))
        btnInicio = Button(self.venUser, text="Iniciar Sesión", bg='cyan',command=self.validacion)  # agregando botones con color
        btnInicio.place(x=200,y=(122))
        btnSalir = Button(self.venUser, text="Salir", bg='grey', command=self.pafuera)
        btnSalir.place(x=200, y=250)
        self.venUser.mainloop()
    def pafuera(self):
        sys.exit(1)
    def close_window(self):
        self.winequi.destroy()
    def inicio(self):
        Label(self.venUser, text="Registration Sucess", fg="green", font=("calibri", 11))
        self.p= Principal()
        self.p.ventana()
        self.venUser.withdraw()
        self.winCorre.withdraw()
        #menu = Principal()
        #self.p= principal()
        #self.p.Principal()
    def validacion(self):
        try:
            verifica_user=self.usuario.get()
            verifica_pass=self.password.get()
            if verifica_user=='Admin' and verifica_pass=='12345':
                self.winCorre = Toplevel()
                #self.winCorre.iconbitmap("Icono.ico")
                self.winCorre.geometry("200x100")
                self.winCorre.config(bg="orange")
                anuncioCorre=Label(self.winCorre,text="Exito al iniciar", fg="navy", bg="orange",
                               font=("Arial", 15))
                anuncioCorre.place(x=30, y=0)
                btnInicio = Button(self.winCorre, text="Comenzar", bg='cyan', command=self.inicio)
                btnInicio.place(x=50, y=(50))
            elif verifica_user=="" or verifica_pass=="":
                raise EspacioBlancoLogin
            elif verifica_user!='Admin' or verifica_pass!='12345':
                raise UsuaIncorrecto
        except UsuaIncorrecto as e:
            pass
        except EspacioBlancoLogin as e:
            pass

pantalla=LoginPunto()