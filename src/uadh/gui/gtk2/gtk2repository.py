'''
Created on 09/05/2012

@author: ariel
'''

import pygtk
pygtk.require('2.0')
import gtk
from uadh.gui import repository, Rect, Point, Size
from uadh.gui.layouts import BorderLayout, GridLayout
import sys



class Application(repository.Application):

    def __init__(self):
        repository.Application.__init__(self)

    def run(self):
        gtk.gdk.threads_init()
        gtk.gdk.threads_enter()
        if self._main_window <> None:
            self._main_window.set_visible(True)
            self._main_window._widget.connect('destroy', self.__on_destroy)
            gtk.main()
        gtk.gdk.threads_leave()

    def stop(self):
        for w in self._windows:
            w.destroy()
        gtk.main_quit()

    def __on_destroy(self, *args):
        self.stop()


class Widget(repository.Widget):
    
    def __init__(self):
        repository.Widget.__init__(self)
        self._rect = Rect(1,1,0,0)
        self._prefered_size = Size()
        #self.set_visible(True)

    def _set_widget(self, w):
        self._widget = w
        if self._widget <> None:
            self._widget.connect('destroy', self.__on_destroy)
            self._widget.connect('expose-event', self.__on_draw)
            self._widget.connect('hide', self.__on_hide)
            self._widget.connect('show', self.__on_show)
            self._widget.connect('size-allocate', self.__on_resize)
            self.emit('created')

    def __on_destroy(self, w, *args):
        self.emit('destroy')

    def __on_draw(self, *args):
        self.emit('draw')

    def __on_hide(self,*args):
        self.emit('hide')

    def __on_show(self,*args):
        self.emit('show')

    def __on_resize(self,*args):
        self.emit('size_changed')
        self.emit('position_changed')

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
        r = self._widget.get_allocation()
        if (r.width>0 and r.height >0):
            self._rect = Rect(r.width, r.height, r.x, r.y)

    def __move(self):
        self._widget.size_allocate(gtk.gdk.Rectangle(self._rect.x, self._rect.y, self._rect.width, self._rect.height))
        self._widget.set_size_request(self._rect.width, self._rect.height)
        self.draw()

    def set_visible(self, visible):
        self._visible = visible
        if visible:
            self._widget.show()
        else:
            self._widget.hide()
        self.draw()

    def is_visible(self):
        return self._visible

    def draw(self):
        self._widget.queue_draw()

    def destroy(self):
        self._widget.destroy()



class Window(Widget):

    def __init__(self, title = ''):
        Widget.__init__(self)
        self._set_widget(gtk.Window())
        self.__container = Container()
        self.connect('size_changed', self.__on_size_changed)
        self._widget.add(self.__container._widget)
        self.__app = None
        self.set_title(title)

    def __on_size_changed(self, *args):
        self.__container.draw()

    def get_container(self):
        return self.__container

    def set_title(self, title):
        self.__title = title
        self._widget.set_title(title)

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
            self._widget.show_all()
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
            self._parent._widget.add(self._widget)
            self._parent._widget.show_all()
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

    def set_visible(self, visible):
        self._visible = visible
        if visible:
            self._widget.show_all()
        else:
            self._widget.hide_all()
        self.draw()


class Container(Parent):

    def __init__(self):
        Parent.__init__(self)
        self._layout = None
        self._set_widget(gtk.Layout())
        self.set_visible(True)

    def remove_child(self, child):
        if child in self._children:
            self._widget.remove(child._widget)
            Parent.remove_child(self, child)

    def add_child(self, child, position = 0):
        if self._layout <> None:
            self._layout.add_layout_widget(child, position)
        Parent.add_child(self, child)

    def set_layout(self, layout):
        self._layout = layout

    def draw(self):
        #Parent.draw(self)
        if self._layout <> None:
            self._layout.do_layout(self)
        else:
            Parent.draw(self)



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
        Container.__init__(self)
        self._set_widget(gtk.Notebook())

    def add_child(self, child, position = 0):
        if child not in self._children:
            self._children.append(child)
            label = gtk.Label(child.get_name())
            self._widget.append_page(child._widget, label)
            self.emit('child_added')



class ButtonTabContainer(Container):
    def __init__(self):
        Container.__init__(self)
        self.set_layout(BorderLayout())
        self.__buttoncontainer = Container()
        self.__buttoncontainer.set_layout(GridLayout(1,0))
        self.__buttoncontainer.set_prefered_size(500, 25)
        self.__buttoncontainer.set_visible(True)
        self.set_visible(True)
        self._items = {}
        Container.add_child(self, self.__buttoncontainer, BorderLayout.TOP)

    def add_child(self, child, position = 0):
        self._items[child.get_name()] = child
        b = PushButton(child.get_name())
        cb = self.__buttoncontainer.get_child(0)
        if cb <> None:
            b._widget.set_group(cb._widget)
        else:
            b.set_selected(True)
        b.set_visible(True)
        child.button = b
        self.__buttoncontainer.add_child(child.button)
        child.button.connect('button_selected', self._on_button_selected)
        
    def _on_button_selected(self, source):
        item = self._items[source.get_text()]
        ch = self.get_child(1)
        if ch <> None:
            ch.set_visible(False)
            self.remove_child(ch)
        Container.add_child(self, item, BorderLayout.CENTER)
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
        self._widget.set_sensitive(active)
        self.emit('active_changed')

    def is_active(self):
        return self._active

    def set_accel_key(self, accel):
        raise NotImplementedError()

    def set_text(self, text):
        raise NotImplementedError()

    def get_text(self):
        return self._caption



class MenuItem(Control):
    pass



class Label(Control):
    def __init__(self, text):
        Control.__init__(self)
        self._set_widget(gtk.Label())
        self.set_text(text)
        self.set_prefered_size(75, 25)

    def set_text(self, text):
        self._caption = text
        self._widget.set_text(text)
        self.emit('text_changed')



class ToolTip(Control):
    def __init__(self, text):
        Control.__init__(self)
        self._set_widget(gtk.Tooltip())
        self.set_text(text)

    def set_size(self, width, height):
        pass

    def set_position(self, x, y):
        pass

    def set_rect(self, rect):
        pass

    def set_parent(self, parent):
        pass

    def set_text(self, text):
        self._caption = text
        self._widget.set_text(text)
        self.emit('text_changed')

    def _load_rect(self):
        pass



class AbstractButton(Control):
    def __init__(self, text):
        Control.__init__(self)

    def set_text(self, text):
        self._caption = text
        self._widget.set_label(text)
        self.emit('text_changed')

    def _set_widget(self, w):
        Control._set_widget(self, w)
        self._widget.connect('clicked', self.__on_clicked)

    def __on_clicked(self, *args):
        self.emit('clicked')



class Button(AbstractButton):
    def __init__(self, text = ''):
        AbstractButton.__init__(self, text)
        self._set_widget(gtk.Button())
        self.set_text(text)
        self.set_prefered_size(75, 25)
        self.set_visible(True)



class AbstractPushButton(AbstractButton):
    def __init__(self, text):
        AbstractButton.__init__(self, text)

    def _set_widget(self, w):
        AbstractButton._set_widget(self, w)
        self._widget.connect('pressed', self.__on_selected)

    def __on_selected(self, *args):
        self.emit('button_selected')

    def set_selected(self, value):
        self._selected = value
        self._widget.set_active(value)
        #self._widget.toggled()
        #self.emit('button_selected')

    def is_selected(self):
        self._selected = self._widget.get_active()
        return self._selected


class PushButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        #self._set_widget(gtk.ToggleButton())
        self._set_widget(gtk.RadioButton())
        self._widget.set_mode(False)
        self.set_text(text)
        self.set_prefered_size(75, 25)
        self.set_selected(False)
        self.set_visible(True)

    def set_selected(self, value):
        self._selected = value
        self._widget.set_active(value)
        self.emit('button_selected')

    def is_selected(self):
        self._selected = self._widget.get_active()
        return self._selected



class CheckButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(gtk.CheckButton())
        self.set_text(text)
        self.set_prefered_size(75, 25)
        self.set_selected(False)
        self.set_visible(True)



class RadioButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._set_widget(gtk.RadioButton())
        self.set_text(text)
        self.set_prefered_size(75, 25)
        self.set_selected(False)
        self.set_visible(True)



class TextEdit(Control):
    def __init__(self, text=''):
        Control.__init__(self)
        self._set_widget(gtk.Entry())
        try:
            self.set_text(text)
        except:
            pass
        self.set_prefered_size(100, 20)
        self.set_visible(True)

    def set_text(self, text):
        self._widget.set_text(text)

    def get_text(self):
        return self._widget.get_text()



class TextArea(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._set_widget(gtk.TextView())
        self.set_text(text)
        self.set_prefered_size(200, 100)
        self.set_visible(True)

    def set_text(self, text):
        self._widget.get_buffer().set_text(text)

    def get_text(self):
        buffer = self._widget.get_buffer() 
        return buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter())



class PasswordField(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._widget.set_visibility(False)
        self.set_visible(True)



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