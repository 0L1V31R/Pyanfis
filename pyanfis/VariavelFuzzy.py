# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 12:26:03 2017

@author: samuel
@project: classe de variaiveis
"""

import numpy as np


class VariavelFuzzy(object):
    def __init__(self, universe, label, defuzzy_method='centroid'):
        self.universe = np.asarray(universe)
        self.label = label
        self.defuzzy_method = defuzzy_method
        self.terms = OrderedDict()
        self.id = id(self)

    def __repr__(self):
        return "{0}:{1}".format(self.__name__, self.label)

    def __len__(self):
        return self.universe.size

    def __getitem(self, key):
        if key in self.terms.keys():
            return self.terms[keys]
        else:
            options = ''
            i0 = len(self.terms) - 1
            i1 = len(self.terms) - 2
            for i, available_key in enumerate(self.terms.keys()):
                if i == i1:
                    options += "'" + str(available_key) + "', or "
                elif i == i0:
                    options += "'" + str(available_key) + "'."
                else:
                    options += "'" + str(available_key) + "'; "
            raise ValueError("Membership function '{0}' does not exist for"
                             "{1} {2}. \n"
                             "Available options: {3}".format(
                                     key, self.__name__, self.label, options))
