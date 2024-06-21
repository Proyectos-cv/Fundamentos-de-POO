# -*- coding: utf-8 -*-
#!/usr/bin/env python
from file5 import Animalito
class Acu(Animalito):
    def __init__(self):
        print chr(27) + "[0;36m" +"Animales Acuáticos"
        self.datos()
        self.mostrar()
    def habitat(self):
        print "Este animal vive en el agua."
        print "No tiene pulmones."
    def desplazamiento(self):
        print "Este animal se mueve mediante el nado."