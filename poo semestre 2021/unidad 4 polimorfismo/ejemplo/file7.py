# -*- coding: utf-8 -*-
#!/usr/bin/env python
from file5 import Animalito
class Tierra(Animalito):
    def __init__(self):
        print chr(27) + "[0;32m" +"Animales Terrestres"
        self.datos()
        self.mostrar()
    def habitat(self):
        print "Este animal vive en la tierra."
        print "Tiene pulmones que le permiten respirar."
    def desplazamiento(self):
        print "Este animal se mueve mediante patas."
        print "O bien se arrastra, como animal rastrero. (OJO: No es Paquita la del Barrio)"