# -*- coding: utf-8 -*-
#!/usr/bin/env python
import abc
from abc import ABCMeta

class SoyAbstracta:
    __metaclass__ = ABCMeta
    def normalAbs(self):
        print "Soy norma el abstracta"
    @abc.abstractmethod
    def funcionAbs(self):
        pass