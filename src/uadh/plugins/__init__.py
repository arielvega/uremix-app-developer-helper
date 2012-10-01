#
#
# Copyright 2011,2012 Luis Ariel Vega Soliz, Uremix (http://www.uremix.org) and contributors.
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

@author: Luis Ariel Vega Soliz
'''

import os, imp, sys, new

__all__ = ['Plugin']

class Plugin:
    def __init__(self, data):
        self._data = data

    def run(self):
        raise NotImplementedError()

    def get_id(self):
        raise NotImplementedError()

class PluginAdmin:
    def __init__(self):
        self.__list = {}

    def admin_plugin(self, plugin):
        self.__list[plugin.get_id()] = plugin
        plugin.run()

    def get_plugin(self, id):
        return self.__list[id]

    def load_plugins(self, data, path = ''):
        # analizamos la carpeta modules
        modules = self.analize(path + 'modules')
        # cargamos los modulos encontrados
        for name in modules:
            try:
                impmod = __import__('modules.'+name, globals(), locals(), [])
                plugin = getattr(impmod, name)
                obj = plugin.Main(data)
                self.admin_plugin(obj) 
            except Exception, ex:
                print ex
        pass

    def analize(self, orig='.'):
        res = []
        for parent, subfolders, files in os.walk(orig):
            subfolders.sort()
            for folder in subfolders:
                try:
                    if folder.count('.py') == 0:
                        res.append(folder)
                except Exception, ex:
                    print ex
            for i in files:
                try:
                    if len(i)>3 and i[-3] == '.':
                        ext = i[-2:]
                        if ext.lower() == 'py':
                            name = i[:-3]
                            if name <> '__init__':
                                res.append(name)
                except Exception, ex:
                    print ex
            break
        return res

admin = PluginAdmin()
