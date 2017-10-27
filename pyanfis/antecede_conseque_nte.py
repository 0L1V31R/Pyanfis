# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:35:30 2017

@author: samuel
@project: Antecedent e consequent classes
"""

import numpy as np
import networkx as nx


class Antecedente(VariavelFuzzy):
    
    def __init__(self, universe, label):
        """""" + Antecedente.__doc__
        super(Antecedente, self).__init__(universe, label)
        self.__name__ = 'Antecedente'
        