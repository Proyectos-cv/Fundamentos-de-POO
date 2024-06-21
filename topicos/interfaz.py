from Tkinter import *

import ttk
from ttk import *
import tkMessageBox

#from Tkinter.ttk import Progressbar
#from Tkinter import messagebox
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)

chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=1, row=1)

rad1 = Radiobutton(window,text='First', value=1)
rad2 = Radiobutton(window,text='Second', value=2)
rad3 = Radiobutton(window,text='Third', value=3)
rad1.grid(column=1, row=2)
rad2.grid(column=2, row=2)
rad3.grid(column=3, row=2)


def clicked():
    tkMessageBox.showinfo('Message title', 'Message content')
btn = Button(window,text='Click here', command=clicked)
btn.grid(column=3,row=1)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=1,row=3)

lbl = Label(window, text="Hello")
lbl.grid(column=2, row=4)
txt = Entry(window,width=10)
txt.grid(column=2, row=5)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=6)


style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='red')
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value'] = 70
bar.grid(column=1, row=7)

window.mainloop()