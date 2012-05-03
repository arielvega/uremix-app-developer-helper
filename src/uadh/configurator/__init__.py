'''
Created on 10/10/2011

@author: ariel
'''

import configobj

class Configurator:

    def __init__(self, basepath):
        self._basepath = basepath

    def get_configuration(self, path):
        raise NotImplementedError()

    def set_configuration(self, path, value):
        raise NotImplementedError()

class ConfConfigurator(Configurator):
    def __init__(self, basepath):
        Configurator.__init__(self, basepath)

    def get_configuration(self, path):
        try:
            filename = path[:path.find('.conf')+5]
            section = path[path.find('.conf')+6:]
            config = configobj.ConfigObj(self._basepath + filename)
            if len(section)>0:
                return config[section]
            else:
                return config
        except:
            return None

'''
to implement:
'''
class XMLConfigurator(Configurator):
    pass