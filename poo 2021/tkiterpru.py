import Tkinter
from Tkinter import *
from Tkinter import *
class Caliz:
    def __init__(self):
        self.winCaliz = Tk()
        self.winCaliz.geometry("800x300")
        self.winCaliz.title('INICIO DE SESION')
        #frame = Frame(self.winCaliz)
        labelUsuario = Label(self.winCaliz, text="Usuario", bg="white")
        labelUsuario.place(x=50, y=20)  # con esto indicas la posicion donde quieres la etiqueta
        self.txtUsua = Entry(self.winCaliz, font="Arial")  # con esto agregas una caja de texto
        self.txtUsua.place(x=150, y=20)
        btnPrueba = Button(self.winCaliz, text="Probar Boton", bg='grey', command=self.probando)
        btnPrueba.place(x=250, y=130)
        self.winCaliz.mainloop()
    def probando(self):
        print "Soy un boton"
c=Caliz()

class LoginPunto:
    def __init__(self):
        self.venUser=Tk()
        self.venUser.geometry("800x300")
        self.venUser.title("INICIO DE SESION")
        frame = Frame(self.venUser)
        frame.config(bg="blue")
        frame.config(width=1000,height=600)
        frame.config(cursor="")
        self.venUser.mainloop()
        boton1=self.venUser.button(row=2, column=0, sticky="nsew")
        #boton1= Tkinter.BUTTON(self.venUser, text="iniciar sesion", width=10, height=5)
k=LoginPunto()


# -*- coding: utf-8 -*-
#!/usr/bin/env python

from Tkinter import *

class LoginPunto:
    def __init__(self):
        self.venUser=Tk()
        self.venUser.geometry("500x300")
        self.venUser.config(bg="orange")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("INICIO DE SESION")
        #imagen=PhotoImage(file="login.png")
        #fondo=Label(self.venUser,image=imagen).place(x=0,y=0)
        #fondo.grid(row=1,column=3)
        lblEti = Label(self.venUser, text="", bg="orange")
        lblEti.grid(row=1, column=1)
        lblEti = Label(self.venUser, text="", bg="orange")
        lblEti.grid(row=2, column=1)
        lblEti= Label(self.venUser,text="Usuario",bg="orange")
        lblEti.grid(row=5,column=1)
        usuario= StringVar()
        txtCaja = Entry(self.venUser, textvariable=usuario)
        txtCaja.grid(row=5, column=2)
        lblEti = Label(self.venUser, text= "Contraseña", bg="orange")
        lblEti.grid(row=100, column=1)
        password = StringVar()
        txtCaja = Entry(self.venUser,show="*", textvariable=password)
        txtCaja.grid(row=100, column=2)
        btnBoton1 = Button(self.venUser, text="Iniciar Sesión", bg='cyan')  # agregando botones con color
        btnBoton1.grid(row=8, column=8)
        self.venUser.mainloop()

c=LoginPunto()

