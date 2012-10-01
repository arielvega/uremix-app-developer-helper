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
Created on 08/09/2012

@author: Luis Ariel Vega Soliz
'''

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Size:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

class Rect(Point, Size):
    def __init__(self, width = 0, height = 0, x = 0, y = 0):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)


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