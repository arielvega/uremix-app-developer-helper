import os, imp, sys, new

__all__ = ['Plugin']

class Plugin:
    '''
    The "view" is a gui.Frame
    '''
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

    def load_plugins(self, data):
        # analizamos la carpeta modules
        modules = self.analize('modules')
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