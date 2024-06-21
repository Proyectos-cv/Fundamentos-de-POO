texto = Text(winInv)
texto.place(x=100, y=100)
scroll = tk.Scrollbar(winInv, command=texto.yview)
texto.configure(yscrollcommand=scroll.set)
texto.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
texto.tag_configure('big', font=('Verdana', 20, 'bold'))
texto.tag_configure('color',
                    foreground='#476042',
                    font=('Tempus Sans ITC', 12, 'bold'))
#Sacando datos de archivos
espacio="\t\t\t"
for linea in open("products.txt", "r"):
    linea = linea.strip()  # El strip elimina espacios
    clave, nomprod, precio = linea.split()
    texto.insert('insert', "\t")
    texto.insert('insert', clave, 'color')
    texto.insert('insert', espacio)
    texto.insert('insert', nomprod, 'color')
    texto.insert('insert', espacio)
    texto.insert('insert', "\t")
    texto.insert('insert', precio, 'color')
    texto.insert('insert', "\n")
texto.configure(state='disabled')
winInv.mainloop()