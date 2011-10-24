'''
Created on 04/09/2011

@author: ariel
'''
from uadh import gui
import pygtk
pygtk.require20()

import gtk, gobject


__all__ = ['GtkWindow', 'GtkWizard']

class GtkFrame(gui.Frame, gtk.Window):
    def __init__(self, title):
        gtk.Window.__init__(self)
        self.set_title(title)
        self._table = gtk.Table(rows = 3, columns = 1)
        self.add(self._table)
        self._statusbar = gtk.Statusbar()
        self._statuscontext = self._statusbar.get_context_id('Main')
        self._table.attach(self._statusbar, 0, 1, 2, 3, yoptions=False)
        self.connect('destroy', lambda q: gtk.main_quit())
        self.set_size_request(600,480)

    def add_section(self, section):
        pass

    def get_section(self, name):
        pass

    def set_menubar(self, menubar):
        if self.self.get_menubar() <> None:
            self._table.remove(self.get_menubar())
        gui.Frame.set_menubar(self, menubar)
        self._table.attach(self.get_menubar(), 0, 1, 0, 1, xpadding = 10, ypadding = 10, xoptions=False, yoptions=False)

    def set_toolbar(self, toolbar):
        gui.Frame.set_toolbar(self, toolbar)

    def set_visible(self, visible):
        if visible:
            self.show()
        else:
            self.hide()

    def set_size(self, width, height):
        self.set_size_request(width, height)

    def set_status_message(self, message):
        self._statusbar.pop(self._statuscontext)
        self._statusbar.push(self._statuscontext, message)

class GtkWindow(GtkFrame):
    def __init__(self, title = ''):
        GtkFrame.__init__(self, title)
        self.__notebook = gtk.Notebook()
        self.__notebook.set_border_width(5)
        self._table.attach(self.__notebook, 0, 1, 1, 2, xpadding = 10, ypadding = 10)

    def add_section(self, section):
        label = gtk.Label(section.get_name())
        self.__notebook.append_page(section.get_content(), label)

class GtkWizard(GtkFrame):
    pass



class ListView(gtk.TreeView):
    __gsignals__ = {'modified':(gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,(gobject.TYPE_INT,)) ,'row-selected': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (gobject.TYPE_PYOBJECT,))}

    items={}
    def __init__(self, title, viewer, alist = [], storeType = gobject.TYPE_PYOBJECT):
        gtk.TreeView.__init__(self)
        self.liststore = gtk.ListStore(storeType)
        self.set_model(self.liststore)
        self.tvcolumn = gtk.TreeViewColumn(title)
        self.append_column(self.tvcolumn)
        self.cell = gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn.set_attributes(self.cell, text=0)
        self.set_search_column(0)
        self.tvcolumn.set_sort_column_id(0)
        self.set_reorderable(True)
        self.connect('row-activated',self.__row_selected)
        self.add_all(alist)
        self.tvcolumn.set_cell_data_func(self.cell, viewer.show)

    def __len__(self):
        return 0

    def __row_selected(self,treeview, path, view_column):
        (model,iter)=treeview.get_selection().get_selected()
        self.emit('row-selected',model.get_value(iter,0))

    def clear(self):
        self.liststore.clear()
        self.queue_draw()
        self.emit('modified',len(self))

    def add(self, elem):
        self.liststore.append([elem])
        self.queue_draw()
        self.emit('modified',len(self))

    def add_all(self, alist):
        for elem in alist:
            self.liststore.append([elem])
        self.queue_draw()
        self.emit('modified',len(self))



class ComboBoxObject(gtk.ComboBox):
    def __init__(self, viewer):
        model = gtk.ListStore(gobject.TYPE_PYOBJECT)
        gtk.ComboBox.__init__(self, model)
        render = gtk.CellRendererText()
        self.pack_start(render, True)
        self.set_cell_data_func(render, viewer.show)



class Viewer:
    def __init__(self):
        pass

    def show(self, treeviewcolumn, render, model, iter):
        pyobj = model.get_value(iter, 0)
        render.set_property('text', self.get_text(pyobj))
        return

    def get_text(self, pyobj):
        raise NotImplementedError()

class ObjectViewer(Viewer):
    def __init__(self):
        Viewer.__init__(self)

    def get_text(self, pyobj):
        return str(pyobj)

class SecuenceViewer(Viewer):
    def __init__(self, pos = 0):
        Viewer.__init__(self)
        self.__pos = pos

    def get_text(self, sec):
        if (sec <> None):
            return str(sec[self.__pos])
        return ''

if __name__ == '__main__':
    f = GtkWindow('MMM')
    s = gui.Section('1',gtk.Frame(''))
    f.add_section(s)
    s = gui.Section('2',gtk.Frame(''))
    f.add_section(s)
    s = gui.Section('3',gtk.Frame(''))
    f.add_section(s)
    s = gui.Section('4',gtk.Frame(''))
    f.add_section(s)
    s = gui.Section('5',gtk.Frame(''))
    f.add_section(s)
    scroll = gtk.ScrolledWindow()
    scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    scroll.add(ListView('Listita', range(30)))
    s = gui.Section('6',scroll)
    f.add_section(s)
    f.show_all()
    gtk.main()