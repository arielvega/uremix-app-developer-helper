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
Created on 08/09/2012

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''

import Tkinter

from uadh.gui import baserepository



class Application(baserepository.Application):
    def __init__(self):
        pass

    def run(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()



class Widget(baserepository.Widget):

    def __init__(self):
        pass

    def get_position(self):
        raise NotImplementedError()

    def set_position(self, x, y):
        raise NotImplementedError()

    def get_size(self):
        raise NotImplementedError()

    def set_size(self, width, height):
        raise NotImplementedError()

    def get_prefered_size(self):
        raise NotImplementedError()

    def set_prefered_size(self, width, height):
        raise NotImplementedError()

    def get_rect(self):
        raise NotImplementedError()

    def set_rect(self, rect):
        raise NotImplementedError()

    def set_visible(self, visible):
        raise NotImplementedError()

    def is_visible(self):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()

    def destroy(self):
        raise NotImplementedError()



class TrayIcon(Widget):

    def show_message(self, message, icon, milisec=5000):
        pass

    def set_icon(self, icon):
        pass

    def get_icon(self):
        pass

    def set_menu(self, menu):
        pass

    def get_menu(self):
        pass



class Window(Widget):

    def __init__(self, title = ''):
        Widget.__init__(self)

    def get_container(self):
        raise NotImplementedError()

    def set_title(self, title):
        raise NotImplementedError()

    def get_title(self):
        raise NotImplementedError()

    def set_app(self, app):
        raise NotImplementedError()



class Child(Widget):

    def __init__(self):
        Widget.__init__(self)

    def set_parent(self, parent):
        raise NotImplementedError()

    def get_parent(self):
        raise NotImplementedError()

    def get_topparent(self):
        raise NotImplementedError()



class Parent(Child):

    def __init__(self):
        Child.__init__(self)

    def add_child(self, child):
        raise NotImplementedError()

    def remove_child(self, child):
        raise NotImplementedError()

    def get_child(self, pos):
        raise NotImplementedError()

    def get_child_count(self):
        raise NotImplementedError()



class Container(Parent):

    def __init__(self):
        Parent.__init__(self)

    def set_layout(self, layout):
        raise NotImplementedError()


class Section(Container):
    
    def get_name(self):
        raise NotImplementedError()

    def set_name(self, name):
        raise NotImplementedError()



class ScrolledContainer(Container):
    pass



class TabContainer(Container):
    pass



class ButtonTabContainer(Container):
    pass



class Control(Child):

    def __init__(self):
        Child.__init__(self)

    def set_active(self, active):
        raise NotImplementedError()

    def is_active(self, active):
        raise NotImplementedError()

    def set_accel_key(self, accel):
        raise NotImplementedError()

    def get_text(self):
        raise NotImplementedError()

    def set_text(self, text):
        raise NotImplementedError()



class Image(Child):
    pass



class Icon(Control):
    pass



class MenuItem(Control):
    pass



class Label(Control):
    pass



class ToolTip(Control):
    pass



class AbstractButton(Control):
    pass



class Button(AbstractButton):
    pass



class AbstractPushButton(AbstractButton):
    def set_selected(self, value):
        raise NotImplementedError()

    def is_selected(self):
        raise NotImplementedError()



class PushButton(AbstractButton):
    pass



class CheckButton(PushButton):
    pass



class RadioButton(PushButton):
    pass



class TextEdit(Control):
    pass



class TextArea(TextEdit):
    pass



class PasswordField(TextEdit):
    pass



class ComboBox(Control):
    pass



class ListBox(Control):
    pass


if __name__=='__main__':
    
    w = Window()
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
        #ta.set_active(element.is_selected())
        pass
    
    b = Button('Norte')
    b.set_position(100, 10)
    w.get_container().add_child(b, BorderLayout.TOP)
    
    radio = RadioButton('Sur')
    radio.set_position(100, 50)
    w.get_container().add_child(radio, BorderLayout.DOWN)
    
    b = CheckButton('Este')
    b.set_position(100, 100)
    b.set_selected(True)
    b.connect('button_selected', proc)
    w.get_container().add_child(b, BorderLayout.RIGHT)
    
    b = PasswordField('Oeste')
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
    tc = ButtonTabContainer()
    #tc = TabContainer()
    tc.set_visible(True)
    tc.set_size(600, 300)
    tc.set_position(100, 450)
    
    b = Button('boton1')
    b.set_position(100, 50)
    s = Section('uno')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    b = Button('boton2')
    b.set_position(100, 50)
    s = Section('dos')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    b = Button('boton3')
    b.set_position(100, 50)
    s = Section('tres')
    s.set_layout(BorderLayout())
    s.add_child(b, BorderLayout.CENTER)
    tc.add_child(s)
    
    w.get_container().add_child(tc, BorderLayout.CENTER)
    
    
    
    app = Application()
    app.set_main_window(w)
    app.run()