#se crea el archivo
file=open("miarchivo.txt","w")
#nos da el nombre
print "nombre del archivo: ",file.name
#nos dice si esta cerrado
print "cerrado o no: ",, file.closed
#nos dice en que modo esta el archivo
print"modo de apertura: ",file.mode
#se cierra el archivo
file.close()
#volvemos a preguntar si esta cerrado
print"cerrado o no: ",file.closed