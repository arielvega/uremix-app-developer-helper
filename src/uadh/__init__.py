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
Created on 1/10/2011

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''

import threading
import time


class VoidObject:
    pass

class UObject:
    
    def __init__(self):
        self._listeners = {}
        pass

    def add_event(self, event):
        if not (event in self._listeners.keys()):
            self._listeners[event] = []

    def remove_event(self, event):
        if (event in self._listeners.keys()):
            del(self._listeners[event])

    def emit(self, event, obj=None):
        if obj == None:
            obj = self
        if event in self._listeners.keys():
            for listener in self._listeners[event]:
                listener(self)

    def get_events(self):
        return self._listeners.keys()

    def connect(self, event, listener):
        if event in self._listeners.keys():
            self._listeners[event].append(listener)

    def disconnect(self, event, listener):
        if event in self._listeners.keys():
            index = 0
            for listenerfunc in self._listeners[event]:
                if repr(listener) == repr(listenerfunc):
                    del(self._listeners[event][index])
                index = index + 1

    def __eq__(self, other):
        return repr(self) == repr(other)

TCOUNTER = 0

class CommonThread(threading.Thread,UObject):
    
    def __init__(self):
        UObject.__init__(self)
        threading.Thread.__init__(self)
        global TCOUNTER
        TCOUNTER = TCOUNTER + 1
        self.setName(TCOUNTER)
        #print 'creado: '+self.getName()
    
    def execute(self):
        raise NotImplementedError('CommonThread.execute() not implemented yet!')
    
    def run(self):
        while True:
            self.execute()
            time.sleep(0.1)
            #print 'ejecutando:'+self.getName()
            if not self.__started:
                #print 'matando:'+self.getName()
                break

    def start(self):
        try:
            self.__started = True
            threading.Thread.start(self)
        except Exception, ex:
            print ex
            pass

    def stop(self):
        self.__started = False

if __name__ == '__main__':
    from uadh import gui
    from gui import repository
    from gui.layouts import *
    app = repository.Application()
    w = repository.Window()
    w.set_size(500, 400)
    w.set_title('HOLA MAMA :D')
    #w.set_visible(True)
    
    w.get_container().set_layout(BorderLayout())
    #w.get_container().set_layout(GridLayout(5,4))
    
    def proc2(element):
        print element.get_parent()
    '''
    ta = TextArea('este es un texto largo')
    ta.connect('text_changed', proc2)
    
    #ta.set_size(500, 300)
    ta.set_position(100, 250)
    w.get_container().add_child(ta, BorderLayout.CENTER)
    print ta.get_text()
    '''
    def proc(element):
        #print element
        #ta.set_active(element.is_selected())
        pass
    
    b = repository.Button('Norte')
    b.set_position(100, 10)
    w.get_container().add_child(b, BorderLayout.TOP)
    
    radio = repository.RadioButton('Sur')
    radio.set_position(100, 50)
    w.get_container().add_child(radio, BorderLayout.DOWN)
    
    b = repository.CheckButton('Este')
    b.set_position(100, 100)
    b.set_selected(True)
    b.connect('button_selected', proc)
    w.get_container().add_child(b, BorderLayout.RIGHT)
    
    b = repository.PasswordField('Oeste')
    b.set_position(100, 150)
    w.get_container().add_child(b, BorderLayout.LEFT)
    '''
    b = RadioButton('Centro')
    b.set_position(100, 200)
    w.get_container().add_child(b, BorderLayout.CENTER)
    
    b = PasswordField('')
    b.set_position(100, 500)
    w.get_container().add_child(b)
    
    '''
    tc = repository.ButtonTabContainer()
    #tc = TabContainer()
    tc.set_visible(True)
    tc.set_size(600, 300)
    tc.set_position(100, 450)
    
    b = repository.Button('boton1')
    b.set_position(100, 50)
    s = repository.Section('uno')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    b = repository.Button('boton2')
    b.set_position(100, 50)
    b.connect('clicked', proc)
    s = repository.Section('dos')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    b = repository.Button('boton3')
    b.set_position(100, 50)
    s = repository.Section('tres')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    w.get_container().add_child(tc, BorderLayout.CENTER)
    
    app.set_main_window(w)
    app.run()