import abc
from abc import ABCMeta
class mater:
    __metaclass__ = ABCMeta
    def pres(self):
        print "MATERIAS"

    @abc.abstractmethod
    def isc(self):
        pass

    @abc.abstractmethod
    def iem(self):
        pass

    @abc.abstractmethod
    def promisc(self):
        pass

    @abc.abstractmethod
    def promiem(self):
        pass