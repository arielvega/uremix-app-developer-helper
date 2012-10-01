'''
Created on 26/03/2012

@author: xXx
'''

import uadh



class Application(uadh.UObject):
    def __init__(self):
        self._windows = []
        self._main_window = None

    def add_window(self, window):
        if window not in self._windows:
            self._windows.append(window)
            window.set_app(self)

    def set_main_window(self, window):
        self.add_window(window)
        self._main_window = window

    def run(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()



class Widget(uadh.UObject):

    def __init__(self):
        uadh.UObject.__init__(self)
        self.__init(self.__class__)

    def __init(self, cls):
        typename = cls.__name__
        if len(cls.__bases__) > 0:
            self.__init(cls.__bases__[0])
        if typename == 'Widget':
            self.add_event('mouse_entered')
            self.add_event('clicked')
            self.add_event('mouse_pressed')
            self.add_event('mouse_released')
            self.add_event('mouse_draged')
            self.add_event('mouse_exited')
            self.add_event('show')
            self.add_event('hide')
            self.add_event('position_changed')
            self.add_event('size_changed')
            self.add_event('created')
            self.add_event('destroy')
            self.add_event('state_changed')
            self.add_event('draw')
        elif typename == 'Window':
            self.add_event('closed')
            self.add_event('minimized')
            self.add_event('maximized')
            self.add_event('restored')
        elif typename == 'Child':
            self.add_event('parent_changed')
        elif typename == 'Parent':
            #self.__init('Child')
            self.add_event('child_added')
            self.add_event('child_removed')
        elif typename == 'Container':
            #self.__init('Parent')
            self.add_event('layout_added')
            self.add_event('layout_removed')
            self.add_event('layout_changed')
            pass
        elif typename == 'TabContainer':
            self.add_event('page_changed')
        elif typename == 'Control':
            #self.__init('Child')
            self.add_event('active_changed')
            self.add_event('text_changed')
        elif typename == 'AbstractButton':
            pass
            #self.__init('Control')
        elif typename == 'Button':
            #self.__init('AbstractButton')
            pass
        elif typename == 'AbstractPushButton':
            self.add_event('button_selected')
            #self.__init('AbstractButton')
            pass
        elif typename == 'PushButton':
            #self.__init('AbstractButton')
            pass
        elif typename == 'CheckButton':
            #self.__init('AbstractButton')
            pass
        elif typename == 'RadioButton':
            #self.__init('AbstractButton')
            pass
        elif typename == 'TextEdit':
            self.add_event('text_changed')
            #self.__init('Control')
            pass
        elif typename == 'TextArea':
            #self.__init('TextField')
            pass
        elif typename == 'ComboBox':
            #self.__init('Control')
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


