from Tkinter import *
from paquetes.paquetesuma.logica import suma
from paquetes.paquetesuma.archivo import guarda

class ventana:
    def inter(self):
        self.a=0
        self.b=0
        self.v6 = Tk()
        self.v6.geometry("700x300")
        self.v6.config(bg="gray")
        self.v6.config(relief="sunken")
        self.v6.title("Unidad 6")
        Label(self.v6, font=("ROCKWELL", 18), fg='black', text="dame x: ", bg='gray').place(x=10,
                                                                                                      y=0)
        Label(self.v6, font=("ROCKWELL", 18), fg='black', text="dame y: ", bg='gray').place(x=10,
                                                                                                      y=50)
        Label(self.v6, font=("ROCKWELL", 18), fg='black', text="suma: ", bg='gray').place(x=10,
                                                                                                      y=100)
        self.dat = IntVar()
        v1 = Entry(self.v6, textvariable=self.dat).place(x=150, y=5)
        self.dat1 = IntVar()
        v2= Entry(self.v6, textvariable=self.dat1).place(x=150, y=55)
        self.dat2 = IntVar()
        self.v3=Entry(self.v6, textvariable=self.dat2).place(x=150, y=105)
        Button(self.v6, font=("INK FREE", 18), fg='black', text="suma", bg='gray',
               command=self.logic, relief=FLAT).place(x=400, y=10)
        Button(self.v6, font=("INK FREE", 18), fg='black', text="mostrar", bg='gray',
               command=self.muestra, relief=FLAT).place(x=400, y=100)
        #barra=Scrollbar(self.v6,comamnd=listbox.yview)
        #barra.place(relx=0.3,rely=0.3)

        #print self.a,self.b
        self.v6 = mainloop()
    def muestra(self):
        str=guarda.muestra()
        #print str
        listbox = Listbox(self.v6)
        listbox.insert(0,str)
        listbox.place(x=150,y=130)
    def logic(self):
        a= self.dat.get()
        b= self.dat1.get()
        p= a+b
        self.dat2.set(str(p))
        c=suma.sumar(a,b)
        guarda.guard(c)


#v=ventana()
#v.muestra()