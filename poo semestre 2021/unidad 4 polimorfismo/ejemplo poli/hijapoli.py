# -*- coding: utf-8 -*-
#!/usr/bin/env python
from normal import SoyNormal
from abstracta import SoyAbstracta
from interface import SoyInterface

class Hija(SoyNormal, SoyAbstracta, SoyInterface):
    def llamadas(self):
        self.funcionNormal()
        self.normalAbs()
    def funcionAbs(self):
        print "Soy una función que le estoy poniendo código"
        print "Pues mi apá la hizo abstracta"
    def funcionInter(self):
        print "Yo soy una función abstracta en el papá"
        print "Pero yo como hija le estoy poniendo código"
h=Hija()
h.llamadas()
h.funcionAbs()
h.funcionInter()