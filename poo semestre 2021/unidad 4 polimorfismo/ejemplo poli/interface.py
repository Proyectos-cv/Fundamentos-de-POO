# -*- coding: utf-8 -*-
#!/usr/bin/env python
import abc
from abc import ABCMeta
class SoyInterface:
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def funcionInter(self):
        pass