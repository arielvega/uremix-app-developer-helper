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
Created on 09/05/2012

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''

from PyQt4 import QtGui, QtCore
from uadh.gui import baserepository
from uadh.gui.base import Rect, Point, Size
from uadh.gui.layouts import BorderLayout, GridLayout

import sys

qt4repositoryapp = QtGui.QApplication([])

class Application(baserepository.Application):

    def __init__(self):
        baserepository.Application.__init__(self)
        self.__app = qt4repositoryapp

    def run(self):
        self._main_window.set_visible(True)
        sys.exit(self.__app.exec_())

    def stop(self):
        for w in self._windows:
            w.destroy()
        pass



class Widget(baserepository.Widget):
    
    def __init__(self):
        baserepository.Widget.__init__(self)
        self._rect = Rect()
        self._prefered_size = Size()
        self.__pressed = False

    def _set_widget(self, w):
        self._widget = w
        if self._widget <> None:
            self._widget.resizeEvent = lambda args: self.__on_resize(args)
            self._widget.moveEvent = lambda args: self.__on_move(args)
            #self._widget.paintEvent = lambda *args: self.__on_draw(args)
            self._widget.showEvent = lambda args: self.__on_show(args)
            self._widget.hideEvent = lambda args: self.__on_hide(args)
            self._widget.mousePressEvent = lambda args: self.__on_mouse_pressed(args)
            self._widget.mouseReleaseEvent = lambda args: self.__on_mouse_released(args)
            self.emit('created')

    def __on_destroy(self, w, args):
        self.emit('destroy')

    def __on_draw(self, args):
        self.emit('draw')

    def __on_hide(self,args):
        type(self._widget).hideEvent(self._widget, args)
        self.emit('hide')

    def __on_show(self,args):
        type(self._widget).showEvent(self._widget, args)
        self.emit('show')

    def __on_resize(self,args):
        type(self._widget).resizeEvent(self._widget, args)
        self.emit('size_changed')
        self.draw()

    def __on_move(self,args):
        type(self._widget).moveEvent(self._widget, args)
        self.emit('position_changed')

    def __on_mouse_pressed(self,args):
        type(self._widget).mousePressEvent(self._widget, args)
        self.__pressed = True
        self.emit('mouse_pressed')

    def __on_mouse_released(self,args):
        type(self._widget).mouseReleaseEvent(self._widget, args)
        self.emit('mouse_released')
        if self.__pressed:
            self.emit('clicked')
        self.__pressed = False

    def get_position(self):
        self._load_rect()
        return Point(self._rect.x, self._rect.y)

    def set_position(self, x, y):
        self._rect.x = x
        self._rect.y = y
        self.__move()

    def get_size(self):
        self._load_rect()
        return Size(self._rect.width, self._rect.height)

    def set_size(self, width, height):
        if width > 0 and height > 0:
            self._rect.width = width
            self._rect.height = height
            self.__move()

    def get_prefered_size(self):
        return Size(self._prefered_size.width, self._prefered_size.height)

    def set_prefered_size(self, width, height):
        if width > 0 and height > 0:
            self._prefered_size.width = width
            self._prefered_size.height = height
            if (self._rect.height < height) or (self._rect.width < width):
                self.set_size(width, height)

    def get_rect(self):
        self._load_rect()
        return Rect(self._rect.width, self._rect.height, self._rect.x, self._rect.y)

    def set_rect(self, rect):
        if rect.width > 0 and rect.height > 0:
            self._rect.x = rect.x
            self._rect.y = rect.y
            self._rect.width = rect.width
            self._rect.height = rect.height
            self.__move()

    def _load_rect(self):
        self._rect = Rect(self._widget.width(), self._widget.height(), self._widget.x(), self._widget.y())

    def __move(self):
        self._widget.move(self._rect.x, self._rect.y)
        self._widget.resize(self._rect.width, self._rect.height)
        self.draw()
    
#    def set_visible(self, visible):
#        pass
    '''
        self._visible = visible
        if visible:
            self._widget.show()
        else:
            self._widget.hide()
        self.draw()
    '''
    def is_visible(self):
        return self._visible

    def draw(self):
        self._widget.update()
        self.__on_draw(None)

    def destroy(self):
        self.__on_destroy(None)
        self._widget.destroy()



class Window(Widget):

    def __init__(self, title = ''):
        Widget.__init__(self)
        self._set_widget(QtGui.QMainWindow())
        self.__container = Container()
        self.connect('size_changed', self.__on_size_changed)
        self._widget.setCentralWidget(self.__container._widget)
        self.__app = None
        self.set_title(title)

    def __on_size_changed(self, *args):
        self.__container.draw()

    def get_container(self):
        return self.__container

    def set_title(self, title):
        self.__title = title
        self._widget.setWindowTitle(title)

    def get_title(self):
        return self.__title

    def set_app(self, app):
        self.__app = app

    def destroy(self):
        self.__container.destroy()
        Widget.destroy(self)

    def set_visible(self, visible):
        self._visible = visible
        if visible:
            self._widget.show()
        else:
            self._widget.hide()
        self.draw()



class Child(Widget):

    def __init__(self):
        Widget.__init__(self)
        self._parent = None

    def set_parent(self, parent):
        if parent == None: # deleting parent
            self._parent = None
        else:
            Child.set_parent(self, None)
            self._parent = parent
            self._parent.connect('size_changed', lambda *args: self.draw())
            self._widget.setParent(self._parent._widget)
            self.emit('parent_changed')
            self._parent.draw()

    def get_parent(self):
        return self._parent

    def get_topparent(self):
        if self._parent <> None:
            grandpa = self._parent.get_parent()
            if grandpa == None:
                return self._parent
            else:
                return grandpa.get_topparent()
        else:
            return self



class Parent(Child):

    def __init__(self):
        Child.__init__(self)
        self._children = []

    def add_child(self, child):
        if child not in self._children:
            child.set_parent(self)
            self._children.append(child)
            self.emit('child_added')

    def remove_child(self, child):
        if child in self._children:
            child.set_parent(None)
            pos = self._children.index(child)
            del(self._children[pos])
            self.emit('child_removed')

    def get_child(self, pos):
        try:
            return self._children[pos]
        except:
            return None

    def get_child_count(self):
        return len(self._children)

    def draw(self):
        Child.draw(self)
        for child in self._children:
            child.draw()

    def destroy(self):
        for child in self._children:
            child.destroy()
        Child.destroy(self)



class Container(Parent):

    def __init__(self):
        Parent.__init__(self)
        self._layout = None
        self._set_widget(QtGui.QWidget())

    def add_child(self, child, position = 0):
        if self._layout <> None:
            self._layout.add_layout_widget(child, position)
        Parent.add_child(self, child)

    def set_layout(self, layout):
        self._layout = layout

    def draw(self):
        if self._layout <> None:
            self._layout.do_layout(self)
        Parent.draw(self)

    def set_visible(self, visible):
        pass


class Section(Container):
    
    def __init__(self, name):
        Container.__init__(self)
        self._caption = name

    def set_name(self, name):
        self._caption = name
        self.emit('text_changed')

    def get_name(self):
        return self._caption

    def set_visible(self, visible):
        self._visible = visible
        if visible:
            self._widget.show()
        else:
            self._widget.hide()
        self.draw()



class ScrolledContainer(Container):
    def __init__(self):
        Container.__init__(self)



class TabContainer(Container):
    def __init__(self):
        Container.__init__(self)
        self._set_widget(QtGui.QTabWidget())
        self._items = {}
        self.__selectable = True

    def _set_widget(self, w):
        Container._set_widget(self, w)

    def draw(self):
        Child.draw(self)
        try:
            child = self._items[str(self._widget.tabText(self._widget.currentIndex()))]
            child.draw()
        except:
            pass

    def add_child(self, child, position = 0):
        if child not in self._children:
            self._items[child.get_name()] = child
            self._children.append(child)
            self._widget.addTab(child._widget, child.get_name())
            self.emit('child_added')
            QtCore.QObject.connect(self._widget, QtCore.SIGNAL('currentChanged(int)'), self.__on_selected)

    def __on_selected(self, pagenum):
        if self.__selectable:
            self.emit('page_changed')
            print 'PAGE '+str(pagenum)



class ButtonTabContainer(Container):
    def __init__(self):
        Container.__init__(self)
        self.set_layout(BorderLayout())
        self.__buttoncontainer = Container()
        self.__buttoncontainer.set_layout(GridLayout(1,0))
        self.__buttoncontainer.set_prefered_size(500, 25)
        #self.__buttoncontainer.set_visible(True)
        #self.set_visible(True)
        self._items = {}
        Container.add_child(self, self.__buttoncontainer, BorderLayout.TOP)

    def add_child(self, child, position = 0):
        self._items[child.get_name()] = child
        b = PushButton(child.get_name())
        #b.set_visible(True)
        child.button = b
        self.__buttoncontainer.add_child(child.button)
        child.button.connect('clicked', self._on_button_selected)
        showbutton = self.__buttoncontainer.get_child(0)
        showbutton.set_selected(True)
        self._on_button_selected(showbutton)
        
    def _on_button_selected(self, source):
        item = self._items[source.get_text()]
        ch = self.get_child(1)
        if ch <> None:
            ch.set_visible(False)
            self.remove_child(ch)
            '''
            for btn in self.__buttoncontainer._children:
                if btn.get_text() == ch.get_name():
                    #btn.set_selected(False)
                    pass
            '''
        Container.add_child(self, item, BorderLayout.CENTER)
        #source.set_selected(True)
        item.set_visible(True)
        item.draw()
        self.draw()
        self.emit('page_changed')



class Control(Child):

    def __init__(self):
        Child.__init__(self)
        self._caption = ''
        #self.set_active(True)

    def set_active(self, active):
        self._active = active
        self._widget.setEnabled(active)
        self.emit('active_changed')

    def is_active(self):
        return self._active

    def set_accel_key(self, accel):
        raise NotImplementedError()

    def set_text(self, text):
        raise NotImplementedError()

    def get_text(self):
        return self._caption

    def __repr__(self):
        return str(self.get_text())


class MenuItem(Control):
    pass



class Label(Control):
    def __init__(self, text):
        Control.__init__(self)
        self._set_widget(QtGui.QLabel())
        self.set_text(text)
        self.set_prefered_size(75, 25)

    def set_text(self, text):
        self._caption = text
        self._widget.setText(text)
        self.emit('text_changed')



class ToolTip(Control):
    pass



class AbstractButton(Control):
    def __init__(self, text):
        Control.__init__(self)

    def set_text(self, text):
        self._caption = text
        self._widget.setText(text)
        self.emit('text_changed')



class Button(AbstractButton):
    def __init__(self, text = ''):
        AbstractButton.__init__(self, text)
        self._set_widget(QtGui.QPushButton())
        self.set_text(text)
        self.set_prefered_size(75, 25)



class AbstractPushButton(AbstractButton):
    def __init__(self, text):
        AbstractButton.__init__(self, text)

    def _set_widget(self, w):
        AbstractButton._set_widget(self, w)
        QtCore.QObject.connect(self._widget, QtCore.SIGNAL('toggled(bool)'), self.__on_selected)

    def __on_selected(self, bool):
        print 'selected '+repr(self)
        self.emit('button_selected')

    def set_selected(self, value):
        self._selected = value
        self._widget.setChecked(value)
        self.emit('button_selected')

    def is_selected(self):
        self._selected = self._widget.isChecked()
        return self._selected


class PushButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QPushButton())
        self._widget.setCheckable(True)
        self._widget.setAutoExclusive(True)
        self.set_text(text)
        self.set_prefered_size(75, 25)
        #self.set_selected(False)

    def set_selected(self, value):
        self._selected = value
        #self._widget.setDown(value)
        #self._widget.setFlat(value)
        self._widget.setChecked(value)
        self.emit('button_selected')

    def is_selected(self):
        self._selected = self._widget.isDown()
        return self._selected

    def draw(self):
        #print 'draw '+self.get_text()
        self.emit('draw')


class CheckButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QCheckBox())
        self.set_text(text)
        self.set_prefered_size(75, 25)
        #self.set_selected(False)



class RadioButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QRadioButton())
        self._widget.setAutoExclusive(True)
        self.set_text(text)
        self.set_prefered_size(75, 25)
        #self.set_selected(False)



class TextEdit(Control):
    def __init__(self, text=''):
        Control.__init__(self)
        self._set_widget(QtGui.QLineEdit())
        try:
            self.set_text(text)
        except:
            pass
        self.set_prefered_size(100, 20)

    def set_text(self, text):
        self._widget.setText(text)

    def get_text(self):
        return self._widget.text()



class TextArea(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._set_widget(QtGui.QTextEdit())
        try:
            self.set_text(text)
        except:
            pass
        self.set_prefered_size(200, 100)

    def set_text(self, text):
        self._widget.setPlainText(text)

    def get_text(self):
        return self._widget.toPlainText()



class PasswordField(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._widget.setEchoMode(QtGui.QLineEdit.Password)



class ComboBox(Control):
    pass


if __name__=='__main__':
    app = Application()
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
        #print element
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
    b.connect('clicked', proc)
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
    
    app.set_main_window(w)
    app.run()