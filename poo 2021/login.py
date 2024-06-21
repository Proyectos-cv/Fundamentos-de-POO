#coding=utf-8
from interface import Principal
from Tkinter import *
from falla import UsuaIncorrecto
from falla import EspacioBlancoLogin
class LoginPunto:
    def __init__(self):
        self.venUser=Tk()
        #self.venUser=Toplevel()
        self.venUser.geometry("600x450")
        self.venUser.config(bg="orange")
        self.venUser.config(cursor="cross")
        self.venUser.config(relief="sunken")
        self.venUser.title("INICIO DE SESION")
        etiquta = Label(self.venUser, text="", bg="orange")
        etiquta.grid(row=1, column=1)
        etiqueta = Label(self.venUser, text="", bg="orange")
        etiquta.grid(row=2, column=1)
        etiquta= Label(self.venUser,text="Usuario",bg="orange")
        etiquta.grid(row=5,column=1)
        usuario= StringVar()
        texto1 = Entry(self.venUser, textvariable=usuario)
        texto1.grid(row=5, column=2)
        etiqueta = Label(self.venUser, text= "contraseña", bg="orange")
        etiqueta.grid(row=100, column=1)
        password = StringVar()
        imagen1 = PhotoImage(file="C:\users\carlo\Downloads\imagen7.png")  # imagen1.gif, productos.gif
        widget = Label(self.venUser, image=imagen1)
        widget.place(x=90, y=150)
        texto2 = Entry(self.venUser,show="*", textvariable=password)
        texto2.grid(row=100, column=2)
        Boton1 = Button(self.venUser, text= "iniciar sesion", bg='cyan', command = self.ingresar)  # bg='cyan' agregando botones con color
        Boton1.grid(row=8, column=8)
        self.venUser.mainloop()
    def ingresar(self):
        self.p = Principal()
        self.p.ventana()
    def pafuera(self):
        sys.exit(1)

    #def close_window(self):
        #self.winequi.destroy()

    #def inicio(self):
        #Label(self.venUser, text="Registration Sucess", fg="green", font=("calibri", 11))
        #self.venUser.withdraw()
        #self.winCorre.withdraw()
        #menu = Principal()

    #def validacion(self):
        #try:
            #verifica_user = self.usuario.get()
            #verifica_pass = self.password.get()
            #if verifica_user == 'Admin' and verifica_pass == '12345':
                #self.winCorre = Toplevel()
                #self.winCorre.iconbitmap("Icono.ico")
                #self.winCorre.geometry("200x100")
                #self.winCorre.config(bg="orange")
                #anuncioCorre = Label(self.winCorre, text="Exito al iniciar", fg="navy", bg="orange",
                                         #font=("Arial", 15))
                #anuncioCorre.place(x=30, y=0)
                #btnInicio = Button(self.winCorre, text="Comenzar", bg='cyan', command=self.inicio)
                #btnInicio.place(x=50, y=(50))
            #elif verifica_user == "" or verifica_pass == "":
                #raise EspacioBlancoLogin
            #elif verifica_user != 'Admin' or verifica_pass != '12345':
                #raise UsuaIncorrecto
        #except UsuaIncorrecto as e:
            #pass
        #except EspacioBlancoLogin as e:
            #pass
c=LoginPunto()











#eti = Label(self.ventan, font=("Arial", 16), fg='black', text="INVENTARIO",
                       #bg="orange")
        #eti.place(x=400, y=25)
        #consulta=StringVar()
        #lblEti = Label(self.ventan, text="consulta", bg="orange")
        #lblEti.grid(row=1, column=2)
        #txtCaja = Entry(self.ventan, textvariable=consulta)
        #txtCaja.grid(row=1, column=3, padx=5 , pady=60)
        #actualizacion = StringVar()
        #lblEti = Label(self.ventan, text="actualizacion", bg="orange")
        #lblEti.grid(row=2, column=2)
        #txtCaja = Entry(self.ventan, textvariable=actualizacion)
        #txtCaja.grid(row=2, column=3,padx=5 , pady=65)
        #faltantes = StringVar()
        #lblEti = Label(self.ventan, text="faltantes", bg="orange")
        #lblEti.grid(row=3, column=2)
        #txtCaja = Entry(self.ventan, textvariable=faltantes)
        #txtCaja.grid(row=3, column=3,padx=5 , pady=70)
        #volvermenu = StringVar()
        #lblEti = Label(self.ventan, text="volver menu", bg="orange")
        #lblEti.grid(row=4, column=2)
        #txtCaja = Entry(self.ventan, textvariable=volvermenu)
        #txtCaja.grid(row=4, column=3,padx=5 , pady=75)



