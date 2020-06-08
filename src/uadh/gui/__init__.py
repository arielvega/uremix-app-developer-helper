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
Created on 26/03/2012

@author: Luis Ariel Vega Soliz (ariel.vega@uremix.org)
@contact: Uremix Team (http://uremix.org)

'''


import os

#load an implementation depending on os
if os.name == 'nt': #sys.platform == 'win32':
    try:
        from uadh.gui.tkinter import tkinterrepository as repository
    except:
        try:
            from uadh.gui.winapi import winapirepository as repository
        except:
            raise Exception("Sorry: no implementation for your platform ('%s') available" % os.name)
elif os.name == 'posix':
    try:
        from uadh.gui.gtk2 import gtk2repository as repository
    except Exception, ex:
        #raise
        try:
            from uadh.gui.qt4 import qtrepository as repository
        except:
            try:
                from uadh.gui.wxwidgets import wxwidgetsrepository as repository
            except:
                try:
                    from uadh.gui.tkinter import tkinterrepository as repository
                except:
                    raise Exception("Sorry: no implementation for your platform ('%s') available" % os.name)
elif os.name == 'java':
    from uadh.gui.swing import swingrepository as repository
else:
    raise Exception("Sorry: no implementation for your platform ('%s') available" % os.name)





