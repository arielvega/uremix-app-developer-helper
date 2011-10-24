__all__ = ['Frame', 'Section']

class Frame:
    def __init__(self):
        self.__windows = {}
        self.set_window('main', self)

    def add_section(self, section):
        raise NotImplementedError()

    def get_section(self, name):
        raise NotImplementedError()

    def get_menubar(self):
        return self.__menubar

    def set_menubar(self, menubar):
        self.__menubar = menubar

    def get_toolbar(self):
        return self.__toolbar

    def set_toolbar(self, toolbar):
        self.__toolbar = toolbar

    def get_window(self, name):
        return self.__windows[name]

    def set_window(self, name, window):
        self.__windows[name] = window

    def set_visible(self, visible):
        raise NotImplementedError()

    def set_size(self, width, height):
        raise NotImplementedError()

    def set_status_message(self, message):
        raise NotImplementedError()

class Section:
    def __init__(self, name, content):
        self.__name = name
        self.__content = content

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

class GuiFactory:
    def Section(self, name, content):
        raise NotImplementedError()

    def Frame(self, title):
        raise NotImplementedError()

    def Window(self, title):
        raise NotImplementedError()

    def Wizard(self, title):
        raise NotImplementedError()

    def Button(self, content):
        raise NotImplementedError()

    def Label(self, content):
        raise NotImplementedError()

    def Menu(self, content):
        raise NotImplementedError()

    def MenuItem(self, content):
        raise NotImplementedError()

    def Toolbar(self, content):
        raise NotImplementedError()