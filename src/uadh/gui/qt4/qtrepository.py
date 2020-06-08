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
Created on 28/03/2012

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

    def __get_window_from_handler(self, hwnd):
        for w in self._windows:
            if w._widget == hwnd:
                return w

    def __get_container_from_handler(self, hwnd):
        for w in self._windows:
            if w.get_container()._widget == hwnd:
                return w.get_container()
            else:
                return w.get_container()._get_child_from_handler(hwnd)
        return None

    def run(self):
        if self._main_window <> None:
            self._main_window._main()
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
        self._widget = None
        self._queue = []
        self._prefered_size = Size()
        self.set_visible(True)

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

    def _process_queue(self):
        if self._widget <> None:
            queue = self._queue
            self._queue = []
            for (f,args) in queue:
                f(*args)

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
        if self._widget == None:
            return
        self._rect = Rect(self._widget.width(), self._widget.height(), self._widget.x(), self._widget.y())
        self.emit('size_changed')

    def __move(self):
        if self._widget == None:
            #self._queue.append((self.__move, ()))
            self._qappend(self.__move)
            return
        self._widget.move(self._rect.x, self._rect.y)
        self._widget.resize(self._rect.width, self._rect.height)
        #self.emit('position_changed')
        self.draw()

    def set_visible(self, visible):
        self._visible = visible
        if self._widget == None:
            #self._queue.append((self.set_visible, (visible,)))
            self._qappend(self.set_visible, visible)
            return
        if visible:
            self._widget.show()
            #self.emit('show')
        else:
            self._widget.hide()
            #self.emit('hide')
        self.draw()

    def is_visible(self):
        return self._visible

    def draw(self):
        if self._widget == None:
            #self._queue.append((self.draw, ()))
            self._qappend(self.draw)
            return
        self._widget.update()
        self.emit('draw')

    def destroy(self):
        if self._widget == None:
            self._queue.append((self.destroy, ()))
            return
        self.emit('destroy')
        self._widget.destroy()

    def _qappend(self, f, *args):
        e = (f,args)
        if len(self._queue)==0 or self._queue[-1] != e:
            self._queue.append(e)



class Window(Widget):

    def __init__(self, title = ''):
        Widget.__init__(self)
        self.__container = Container()
        self.connect('size_changed', self.__on_size_changed)
        self.__app = None
        self.set_title(title)

    def __create(self):
        # Create Window
        self._set_widget(QtGui.QMainWindow())
        self.emit('created')

    #def _load_rect(self):
    #    if self._widget == None:
    #        return
    #    r = windef.RECT()
    #    winuser.GetClientRect(self._widget, pointer(r))
    #    self._rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)

    def _main(self):
        self.__create()
        self._process_queue()
        #r = windef.RECT()
        #winuser.GetClientRect(self._widget, pointer(r))
        #rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)
        #self.__container._load_rect = self._load_rect
        self.__container.set_parent(self)
        #self.__container.set_rect(rect)
        #self.__container._process_queue()
        self._widget.setCentralWidget(self.__container._widget)
        self.connect('position_changed', self.__container._on_position_changed)
        self.connect('draw', self.__container._on_draw)
        self._widget.update()
        #self.emit('draw')

    def __on_size_changed(self, *args):
        self.__container.draw()

    def get_container(self):
        return self.__container

    def set_title(self, title):
        self.__title = title
        if self._widget == None:
            self._queue.append((self.set_title, (title,)))
            return
        self._widget.setWindowTitle(title)

    def get_title(self):
        return self.__title

    def set_app(self, app):
        self.__app = app

    def destroy(self):
        self.__container.destroy()
        #self.emit('destroy')
        Widget.destroy(self)

    def set_visible(self, visible):
        Widget.set_visible(self, visible)
        try:
            self.__container.set_visible(visible)
        except:
            pass



class Child(Widget):

    def __init__(self):
        Widget.__init__(self)
        self._parent = None
        self._createops = []

    def set_parent(self, parent):
        if parent == None: # deleting parent
            #if self._parent <> None:
            #    self._parent.disconnect('size_changed', self.listener)
            self._parent = None
        else:
            Child.set_parent(self, None)
            self._parent = parent
            if self._parent._widget == None or self._widget == None:
                if self._parent._widget != None:
                    self._process_queue()
                else:
                    self._createops.append((self.set_parent, (parent,)))
            else:
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

    def _process_queue(self):
        createops = self._createops
        self._createops = []
        for (f,args) in createops:
            f(*args)
        Widget._process_queue(self)

    def _set_widget(self, w):
        if self._parent == None:
            self._createops.append((self._set_widget, (w,)))
            return
        Widget._set_widget(self, w)
            


class Parent(Child):

    def __init__(self):
        Child.__init__(self)
        self._children = []
        self.connect('created', self.__on_created)

    def __on_created(self, source):
        self._process_queue()

    def _process_queue(self):
        Child._process_queue(self)
        for child in self._children:
            child._process_queue()

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

    def set_visible(self, visible):
        self._visible = visible
        if self._widget == None:
            self._queue.append((self.set_visible, (visible,)))
            return
        for child in self._children:
            child.set_visible(visible)
        Child.set_visible(self, visible)



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
        Parent.draw(self)
        if self._layout <> None:
            self._layout.do_layout(self)

    def _on_draw(self, source):
        if (self._parent <> None) and (self._parent._widget <> None):
            self.draw()
        else:
            self._queue.append((self._on_draw, (source,)))

    def _on_size_changed(self, source):
        if (self._parent <> None) and (self._parent._widget <> None):
            self.draw()
        else:
            self._queue.append((self._on_size_changed, (source,)))

    def _on_position_changed(self, source):
        if (self._parent <> None) and (self._parent._widget <> None):
            self.draw()
        else:
            self._queue.append((self._on_position_changed, (source,)))



class Section(Container):
    
    def __init__(self, name):
        Container.__init__(self)
        self._caption = name

    def set_name(self, name):
        self._caption = name
        self.emit('text_changed')

    def get_name(self):
        return self._caption



class ScrolledContainer(Container):
    def __init__(self):
        Container.__init__(self)



class TabContainer(Container):
    def __init__(self):
        Parent.__init__(self)
        self._layout = None
        self._set_widget(QtGui.QTabWidget())
        self._items = {}
        self.__selectable = True

    #def _set_widget(self, w):
    #    Container._set_widget(self, w)

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
            if self._widget == None:
                self._createops.append((self.add_child, (child, position)))
                return
            child.set_parent(self)
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
        if self._widget == None:
            self._queue.append((self.add_child, (child,)))
            return
        self._process_queue()
        b = PushButton(child.get_name())
        b.set_visible(True)
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
        Container.add_child(self, item, BorderLayout.CENTER)
        #self.add_child(item, BorderLayout.CENTER)
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
        if self._widget == None:
            self._queue.append((self.set_active, (active,)))
            return
        self._widget.setEnabled(active)
        self.emit('active_changed')

    def is_active(self):
        return self._active

    def set_accel_key(self, accel):
        raise NotImplementedError()

    def set_text(self, text):
        self._caption = text
        if self._widget == None:
            self._queue.append((self.set_text, (text,)))
            return
        self._widget.setText(text)
        self.emit('text_changed')

    def get_text(self):
        if self._widget != None:
            self._caption = self._widget.text()
        return self._caption

    def __repr__(self):
        return str(self.get_text())



class MenuItem(Control):
    pass



class Label(Control):
    def __init__(self, text):
        Control.__init__(self)
        self.set_text(text)
        self._set_widget(QtGui.QLabel())
        self.set_prefered_size(75, 25)



class ToolTip(Control):
    pass



class AbstractButton(Control):
    def __init__(self, text):
        Control.__init__(self)



class Button(AbstractButton):
    def __init__(self, text = ''):
        AbstractButton.__init__(self, text)
        self._set_widget(QtGui.QPushButton())
        self.set_text(text)
        self.set_prefered_size(75, 25)



class AbstractPushButton(AbstractButton):
    def __init__(self, text):
        AbstractButton.__init__(self, text)
        self._selected = False

    def _set_widget(self, w):
        AbstractButton._set_widget(self, w)
        if self._widget == None:
            self._queue.append((self._set_widget, (w,)))
            return
        QtCore.QObject.connect(self._widget, QtCore.SIGNAL('toggled(bool)'), self.__on_selected)

    def __on_selected(self, bool):
        print 'selected '+repr(self)
        self.emit('button_selected')

    def set_selected(self, value):
        self._selected = value
        if self._widget == None:
            self._queue.append((self.set_selected, (value,)))
            return
        self._widget.setChecked(value)
        self.emit('button_selected')

    def is_selected(self):
        if self._widget != None:
            self._selected = self._widget.isChecked()
        return self._selected



class PushButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QPushButton())
        self._init()
        self.set_text(text)
        self.set_prefered_size(75, 25)

    def _init(self):
        if self._widget == None:
            self._createops.append((self._init,()))
            return
        self._widget.setCheckable(True)
        self._widget.setAutoExclusive(True)

    def is_selected(self):
        if self._widget != None:
            self._selected = self._widget.isDown()
        return self._selected

    def draw(self):
        self.emit('draw')



class CheckButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QCheckBox())
        self.set_text(text)
        self.set_prefered_size(75, 25)



class RadioButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(QtGui.QRadioButton())
        self._init()
        self.set_text(text)
        self.set_prefered_size(75, 25)

    def _init(self):
        if self._widget == None:
            self._createops.append((self._init,()))
            return
        self._widget.setAutoExclusive(True)

class TextEdit(Control):
    def __init__(self, text=''):
        Control.__init__(self)
        self._set_widget(QtGui.QLineEdit())
        self.set_text(text)
        self.set_prefered_size(100, 20)



class TextArea(TextEdit):
    def __init__(self, text=''):
        Control.__init__(self)
        self._set_widget(QtGui.QTextEdit())
        self.set_text(text)
        self.set_prefered_size(200, 100)

    def set_text(self, text):
        self._caption = text
        if self._widget == None:
            self._queue.append((self.set_text, (text,)))
            return
        self._widget.setPlainText(text)
        self.emit('text_changed')

    def get_text(self):
        if self._widget != None:
            self._caption = self._widget.toPlainText()
        return self._caption



class PasswordField(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._format()

    def _format(self):
        if self._widget == None:
            self._createops.append((self._format, ()))
            return
        self._widget.setEchoMode(QtGui.QLineEdit.Password)



class ComboBox(Control):
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
    
    ta = TextArea('este es un texto largo')
    ta.connect('text_changed', proc2)
    
    #ta.set_size(500, 300)
    ta.set_position(100, 250)
    w.get_container().add_child(ta, BorderLayout.CENTER)
    print ta.get_text()
    
    def proc(element):
        ta.set_active(element.is_selected())
    
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
    
    b = TextEdit('Oeste')
    b.set_position(100, 150)
    w.get_container().add_child(b, BorderLayout.LEFT)
    '''
    b = RadioButton('Centro')
    b.set_position(100, 200)
    w.get_container().add_child(b, BorderLayout.CENTER)
    
    b = PasswordField('')
    b.set_position(100, 500)
    w.get_container().add_child(b)
    
    
    tc = ButtonTabContainer()
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
    
    w.get_container().add_child(tc)
    '''
    
    
    app = Application()
    app.set_main_window(w)
    app.run()