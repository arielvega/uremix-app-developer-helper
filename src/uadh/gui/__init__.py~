#__all__ = ['Frame', 'Section']

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
        raise
        try:
            from uadh.gui.qt4 import qt4repository as repository
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
    #from uadh.gui.gtk2 import gtk2repository as repository
else:
    raise Exception("Sorry: no implementation for your platform ('%s') available" % os.name)





