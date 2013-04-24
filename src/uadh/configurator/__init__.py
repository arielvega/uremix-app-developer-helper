#
#
# Copyright 2011,2013 Luis Ariel Vega Soliz, Uremix (http://www.uremix.org) and contributors.
#
#
# This file is part of UADH (Uremix App Developer Helper).
#
#    UADH is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    UADH is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with UADH.  If not, see <http://www.gnu.org/licenses/>.
#
#

'''
Created on 10/10/2011

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

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