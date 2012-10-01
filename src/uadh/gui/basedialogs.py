'''
Created on 24/09/2012

@author: Luis Ariel Vega Soliz
'''

import uadh

class Dialog(uadh.UObject):
    def __init__(self):
        pass

    def get_value(self):
        raise NotImplementedError()