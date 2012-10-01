'''
Created on 28/03/2012

@author: xXx
'''

from uadh.gui import baserepository
from uadh.gui.base import Rect, Point, Size

from uadh.gui.winapi.lib import winuser, windef, winbase, commctrl, wingdi
from ctypes import byref, WinError, pointer, c_char_p, c_void_p, wintypes
from uadh.gui.winapi.lib.winuser import CreateWindow
from uadh.gui.layouts import BorderLayout, GridLayout
import sys
import ctypes
from ctypes.wintypes import LPSTR, LPWSTR, HANDLE
from uadh.gui.winapi.lib.windef import RECT


class Application(baserepository.Application):

    def __init__(self):
        baserepository.Application.__init__(self)
        self.__registerwcls()

    def __registerwcls(self):
        # Define Window Class
        self.wndclass = winuser.WNDCLASS()
        self.wndclass.style = winuser.CS_HREDRAW | winuser.CS_VREDRAW
        self.wndclass.lpfnWndProc = winuser.WNDPROC(self.__WindowProc)
        self.wndclass.cbClsExtra = self.wndclass.cbWndExtra = 0
        self.wndclass.hInstance = winbase.GetModuleHandle(windef.NULL)
        self.wndclass.hIcon = winuser.LoadIconA(windef.NULL, winuser.IDI_APPLICATION)
        self.wndclass.hCursor = winuser.LoadCursorA(windef.NULL, winuser.IDC_ARROW)
        self.wndclass.hbrBackground = winuser.COLOR_WINDOW #wingdi.GetStockObject(wingdi.WHITE_BRUSH)
        self.wndclass.lpszMenuName = None
        self.wndclass.lpszClassName = "MAINWINDOW"
        # Register Window Class
        if not winuser.RegisterClass(byref(self.wndclass)):
            raise WinError()
        # Define Container Class
        self.contclass = winuser.WNDCLASS()
        self.contclass.style = winuser.CS_HREDRAW | winuser.CS_VREDRAW
        self.contclass.lpfnWndProc = winuser.WNDPROC(self.__ContainerProc)
        self.contclass.cbClsExtra = self.contclass.cbWndExtra = 0
        self.contclass.hInstance = winbase.GetModuleHandle(windef.NULL)
        self.contclass.hIcon = winuser.LoadIconA(windef.NULL, winuser.IDI_APPLICATION)
        self.contclass.hCursor = winuser.LoadCursorA(windef.NULL, winuser.IDC_ARROW)
        self.contclass.hbrBackground = winuser.COLOR_WINDOW #wingdi.GetStockObject(wingdi.WHITE_BRUSH)
        self.contclass.lpszMenuName = None
        self.contclass.lpszClassName = "CONTAINER"
        # Register Container Class
        if not winuser.RegisterClass(byref(self.contclass)):
            raise WinError()
        ccex = commctrl.INITCOMMONCONTROLSEX()
        res = commctrl.InitCommonControlsEx(byref(ccex))
        

    def __WindowProc(self, hwnd, message, wParam, lParam):
        if message == winuser.WM_PAINT:
            w = self.__get_window_from_handler(hwnd)
            if w <> None:
                w.emit('draw')
            return 0
        elif message == winuser.WM_SIZE:
            w = self.__get_window_from_handler(hwnd)
            if w <> None:
                w.emit('size_changed')
            return 0
        elif message == winuser.WM_SIZING:
            #print 'sizing'
            w = self.__get_window_from_handler(hwnd)
            if w <> None:
                w.emit('size_changed')
            return 0
        elif message == winuser.WM_WINDOWPOSCHANGED:
            w = self.__get_window_from_handler(hwnd)
            if w <> None:
                w.emit('position_changed')
            return 0
        elif message == winuser.WM_DESTROY:
            #self.stop()
            winuser.PostQuitMessage(0)
            return 0
        return winuser.DefWindowProcA(hwnd, message, wParam, lParam)

    def __ContainerProc(self, hwnd, message, wParam, lParam):
        #print message
        if message == winuser.WM_PAINT:
            return 0
        elif message == winuser.WM_DRAWITEM:
            return 0
        elif message == winuser.WM_COMMAND:
            submessage = windef.HIWORD(wParam)
            if submessage == winuser.BN_CLICKED:
                container = self.__get_container_from_handler(hwnd)
                if container <> None:
                    button = container._get_child_from_handler(lParam)
                    if button <> None:
                        button.emit('clicked')
            elif submessage == winuser.EN_CHANGE:
                container = self.__get_container_from_handler(hwnd)
                if container <> None:
                    textedit = container._get_child_from_handler(lParam)
                    if textedit <> None:
                        textedit.emit('text_changed')
            return 0
        elif message == winuser.WM_DESTROY:
            #winuser.PostQuitMessage(0)
            return 0
        return winuser.DefWindowProcA(hwnd, message, wParam, lParam)

    def __get_window_from_handler(self, hwnd):
        for w in self._windows:
            if w._hwnd == hwnd:
                return w

    def __get_container_from_handler(self, hwnd):
        for w in self._windows:
            if w.get_container()._hwnd == hwnd:
                return w.get_container()
            else:
                return w.get_container()._get_child_from_handler(hwnd)
        return None

    def run(self):
        if self._main_window <> None:
            sys.exit(self._main_window._main())

    def stop(self):
        for w in self._windows:
            w.destroy()


class Widget(baserepository.Widget):
    
    def __init__(self):
        baserepository.Widget.__init__(self)
        self._rect = Rect()
        self._hwnd = None
        self._queue = []
        self._prefered_size = Size()
        self.set_visible(True)

    def _process_queue(self):
        if self._hwnd <> None:
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
        self._rect.width = width
        self._rect.height = height
        self.__move()

    def get_prefered_size(self):
        return Size(self._prefered_size.width, self._prefered_size.height)

    def set_prefered_size(self, width, height):
        self._prefered_size.width = width
        self._prefered_size.height = height
        if (self._rect.height < height) or (self._rect.width < width):
            self.set_size(width, height)

    def get_rect(self):
        self._load_rect()
        return Rect(self._rect.width, self._rect.height, self._rect.x, self._rect.y)

    def set_rect(self, rect):
        self._rect.x = rect.x
        self._rect.y = rect.y
        self._rect.width = rect.width
        self._rect.height = rect.height
        self.__move()

    def _load_rect(self):
        if self._hwnd == None:
            return
        r = windef.RECT()
        winuser.GetClientRect(self._hwnd, pointer(r))
        self._rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)
        self.emit('size_changed')

    def __move(self):
        if self._hwnd == None:
            self._queue.append((self.__move, ()))
            return
        winuser.MoveWindow(self._hwnd, self._rect.x, self._rect.y, self._rect.width, self._rect.height, windef.TRUE)
        self.emit('position_changed')
        self.draw()

    def set_visible(self, visible):
        self._visible = visible
        if self._hwnd == None:
            self._queue.append((self.set_visible, (visible,)))
            return
        if visible:
            winuser.ShowWindow(self._hwnd, winuser.SW_SHOWNORMAL)
            self.emit('show')
        else:
            winuser.ShowWindow(self._hwnd, winuser.SW_HIDE)
            self.emit('hide')
        self.draw()

    def is_visible(self):
        return self._visible

    def draw(self):
        if self._hwnd == None:
            self._queue.append((self.draw, ()))
            return
        winuser.UpdateWindow(self._hwnd)
        self.emit('draw')

    def destroy(self):
        if self._hwnd == None:
            self._queue.append((self.destroy, ()))
            return
        winuser.SendMessage(self._hwnd, winuser.WM_DESTROY, 0, 0)
        self.emit('destroy')



class Window(Widget):

    def __init__(self, title = ''):
        Widget.__init__(self)
        self.__container = Container()
        self.__app = None
        self.__title = title

    def __create(self):
        # Create Window
        self._hwnd = CreateWindow(  'MAINWINDOW',
                          self.__title,
                          winuser.WS_OVERLAPPEDWINDOW | winuser.WS_CLIPCHILDREN,
                          winuser.CW_USEDEFAULT,
                          winuser.CW_USEDEFAULT,
                          winuser.CW_USEDEFAULT,
                          winuser.CW_USEDEFAULT,
                          windef.NULL,
                          windef.NULL,
                          self.__app.wndclass.hInstance,
                          windef.NULL)
        newfont = wingdi.CreateFont(12,0,0,0,wingdi.FW_NORMAL,False, False, False,wingdi.DEFAULT_CHARSET, wingdi.OUT_DEFAULT_PRECIS, wingdi.CLIP_DEFAULT_PRECIS,wingdi.DEFAULT_QUALITY, wingdi.DEFAULT_PITCH | wingdi.FF_DONTCARE, 'Arial')
        wingdi.GetStockObject(wingdi.DEFAULT_GUI_FONT)
        winuser.SendMessage(self._hwnd, winuser.WM_SETFONT, newfont, winuser.MAKELPARAM(windef.TRUE, 0))
        self.emit('created')
        #winuser.AnimateWindow(hwnd, 50000, winuser.AW_BLEND | winuser.AW_HOR_POSITIVE | winuser.AW_CENTER)

    def _load_rect(self):
        if self._hwnd == None:
            return
        r = windef.RECT()
        winuser.GetClientRect(self._hwnd, pointer(r))
        self._rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)

    def _main(self):
        self.__create()
        self._process_queue()
        r = windef.RECT()
        winuser.GetClientRect(self._hwnd, pointer(r))
        rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)
        self.__container._load_rect = self._load_rect
        self.__container.set_parent(self)
        self.__container.set_rect(rect)
        self.__container._process_queue()
        self.connect('position_changed', self.__container._on_position_changed)
        self.connect('draw', self.__container._on_draw)
        winuser.UpdateWindow(self._hwnd)
        # Pump Messages
        msg = winuser.MSG()
        pMsg = pointer(msg)
        while winuser.GetMessage( pMsg, windef.NULL, 0, 0) != 0:
            winuser.TranslateMessage(pMsg)
            winuser.DispatchMessageA(pMsg)
            #time.sleep(0.01)
        #return msg.wParam
        return 0

    def get_container(self):
        return self.__container

    def set_title(self, title):
        self.__title = title
        if self._hwnd == None:
            self._queue.append((self.set_title, (title,)))
            return
        winuser.SetWindowText(self._hwnd , title)

    def get_title(self):
        return self.__title

    def set_app(self, app):
        self.__app = app

    def destroy(self):
        self.__container.destroy()
        self.emit('destroy')


class Child(Widget):

    def __init__(self):
        Widget.__init__(self)
        self._parent = None
        self._caption = ''
        self._wclass = ''
        self._style = 0
        self._createops = []

    def set_parent(self, parent):
        if parent == None: # deleting parent
            #if self._parent <> None:
            #    self._parent.disconnect('size_changed', self.listener)
            self._parent = None
        else:
            Child.set_parent(self, None)
            self._parent = parent
            if self._parent._hwnd == None:
                self._createops.append((self.set_parent, (parent,)))
            elif self._hwnd == None:
                self._hinst = winuser.GetWindowLong(self._parent._hwnd, winuser.GWL_HINSTANCE)
                rect = self.get_rect()
                self._hwnd = CreateWindow(  self._wclass,
                          self._caption,
                          winuser.WS_VISIBLE | winuser.WS_CHILD | self._style,
                          # Size and position values are given explicitly, because the CW_USEDEFAULT constant gives zero values for buttons. 
                          rect.x,         # starting x position 
                          rect.y,         # starting y position 
                          rect.width,        # button width 
                          rect.height,        # button height 
                          self._parent._hwnd,#hwnd,       # parent window 
                          windef.NULL,#NULL,       # No menu 
                          self._hinst, 
                          windef.NULL);      #// pointer not needed
                #self._parent.connect('size_changed', self._on_size_changed)
                newfont = wingdi.CreateFont(-11,0,0,0,wingdi.FW_NORMAL,False, False, False,wingdi.DEFAULT_CHARSET, wingdi.OUT_DEFAULT_PRECIS, wingdi.CLIP_DEFAULT_PRECIS,wingdi.DEFAULT_QUALITY, wingdi.DEFAULT_PITCH | wingdi.FF_DONTCARE, 'Tahoma')
                winuser.SendMessage(self._hwnd, winuser.WM_SETFONT, newfont, winuser.MAKELPARAM(windef.TRUE, 0))
                self.emit('created')
                self.emit('parent_changed')
            else:
                winuser.SetParent(self._hwnd, self._parent._hwnd)
                #self._parent.connect('size_changed', self._on_size_changed)
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

    def _load_rect(self):
        if self._hwnd == None:
            return
        pr = windef.RECT()
        winuser.GetWindowRect(self._parent._hwnd, pointer(pr))
        r = windef.RECT()
        winuser.GetWindowRect(self._hwnd, pointer(r))
        self._rect = Rect(r.right - r.left, r.bottom - r.top, r.left - pr.left, r.top - pr.top)

    def _process_queue(self):
        createops = self._createops
        self._createops = []
        for (f,args) in createops:
            f(*args)
        Widget._process_queue(self)


class Parent(Child):

    def __init__(self):
        Child.__init__(self)
        self._children = []
        self.connect('created', self.__on_created)

    def __on_created(self, source):
        self._process_queue()

    def add_child(self, child):
        if child not in self._children:
            self._children.append(child)
            child.set_parent(self)
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

    def _process_queue(self):
        Child._process_queue(self)
        for child in self._children:
            child._process_queue()

    def _get_child_from_handler(self, hwnd):
        for child in self._children:
            if Container in child.__class__.__bases__:
                childres = child._get_child_from_handler(hwnd)
                if childres <> None:
                    return childres
            elif child._hwnd == hwnd:
                return child
        return None

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
        self._caption = ''
        self._wclass = 'CONTAINER'
        self._style = winuser.WS_CLIPCHILDREN
        self._layout = None

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
        if (self._parent <> None) and (self._parent._hwnd <> None):
            r = windef.RECT()
            winuser.GetClientRect(self._parent._hwnd, pointer(r))
            rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)
            self.set_rect(rect)
            self.draw()
        else:
            self._queue.append((self._on_draw, (source,)))

    def _on_size_changed(self, source):
        if (self._parent <> None) and (self._parent._hwnd <> None):
            r = windef.RECT()
            winuser.GetClientRect(self._parent._hwnd, pointer(r))
            rect = Rect(r.right - r.left, r.bottom - r.top, r.left, r.top)
            self.set_rect(rect)
            self.draw()
        else:
            self._queue.append((self._on_size_changed, (source,)))

    def _on_position_changed(self, source):
        if (self._parent <> None) and (self._parent._hwnd <> None):
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
        self._style = self._style | winuser.WS_HSCROLL | winuser.WS_VSCROLL



class TabContainer(Container):
    def __init__(self):
        Container.__init__(self)
        self._caption = ''
        self._wclass = commctrl.WC_TABCONTROL
        self._style = winuser.WS_CLIPCHILDREN | winuser.WS_CLIPSIBLINGS | winuser.WS_VISIBLE# | commctrl.TCS_OWNERDRAWFIXED
        self._items = {}

    def add_child(self, child, position=0):
        self._items[position] = child
        if self._hwnd == None:
            self._queue.append((self.insert_section, (position, child)))
            return
        tie = commctrl.TC_ITEM()
        tie.mask = commctrl.TCIF_TEXT;
        tie.pszText = LPWSTR(child)
        tie.cchTextMax = len(tie.pszText.value)
        commctrl.TabCtrl_InsertItem(self._hwnd, position, byref(tie))

    def _on_draw(self, source):
        for (i,text) in self._items.items():
            rect = RECT()
            commctrl.TabCtrl_GetItemRect(self._hwnd, i, pointer(rect))
            ps = winuser.PAINTSTRUCT()
            hdc = winuser.BeginPaint(self._hwnd, byref(ps))
            #winuser.GetClientRect(self._hwnd, byref(rect))
            newfont = wingdi.CreateFont(25,0,0,0,wingdi.FW_NORMAL,False, False, False,wingdi.DEFAULT_CHARSET, wingdi.OUT_DEFAULT_PRECIS, wingdi.CLIP_DEFAULT_PRECIS,wingdi.DEFAULT_QUALITY, wingdi.DEFAULT_PITCH | wingdi.FF_DONTCARE, 'Arial')
            oldfont = wingdi.SelectObject(hdc, newfont)
            winuser.DrawTextA(hdc,
                      text ,
                      -1,
                      byref(rect), 
                      winuser.DT_SINGLELINE|winuser.DT_CENTER|winuser.DT_VCENTER|winuser.DT_NOCLIP)
            oldfont = wingdi.SelectObject(hdc, oldfont)
            winuser.EndPaint(self._hwnd, byref(ps))



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

    def add_child(self, child, position=0):
        self._items[child.get_name()] = child
        if self._hwnd == None:
            self._queue.append((self.add_child, (child,)))
            return
        self._process_queue()
        b = PushButton(child.get_name())
        b.set_visible(True)
        child.button = b
        self.__buttoncontainer.add_child(child.button)
        child.button.connect('clicked', self._on_clicked)
        
    def _on_clicked(self, source):
        #item = self._items[source.get_text()].get_element()
        item = self._items[source.get_text()]
        ch = self.get_child(1)
        if ch <> None:
            ch.set_visible(False)
            self.remove_child(ch)
        #self.add_child(item, BorderLayout.CENTER)
        Container.add_child(self, item, BorderLayout.CENTER)
        item.set_visible(True)
        item.draw()
        self.draw()



class Control(Child):

    def __init__(self):
        Child.__init__(self)
        self._hwnd = None
        self._caption = ''
        self.set_active(True)

    def set_active(self, active):
        self._active = active
        if self._hwnd == None:
            self._queue.append((self.set_active, (active,)))
            return
        winuser.EnableWindow(self._hwnd, self._active)
        self.emit('active_changed')

    def is_active(self):
        return self._active

    def set_accel_key(self, accel):
        raise NotImplementedError()

    def set_text(self, text):
        self._caption = text
        if self._hwnd == None:
            self._queue.append((self.set_text, (text,)))
            return
        winuser.SetWindowText(self._hwnd , self._caption)

    def get_text(self):
        return self._caption



class MenuItem(Control):
    pass



class Label(Control):
    def __init__(self, text):
        Control.__init__(self)
        self.set_text(text)
        self._wclass = 'BUTTON'
        self.set_prefered_size(75, 25)
        self._style = winuser.BS_PUSHBUTTON



class ToolTip(Control):
    def __init__(self, text):
        Control.__init__(self)
        self.set_text(text)
        self._wclass = commctrl.TOOLTIPS_CLASS
        self._style = commctrl.TTS_ALWAYSTIP | winuser.WS_POPUP | commctrl.TTS_NOPREFIX
        Control.set_position(self, winuser.CW_USEDEFAULT, winuser.CW_USEDEFAULT)
        Control.set_size(self, winuser.CW_USEDEFAULT, winuser.CW_USEDEFAULT)

    def set_size(self, width, height):
        pass

    def set_position(self, x, y):
        pass

    def set_rect(self, rect):
        pass

    def set_parent(self, parent):
        if parent == None: # deleting parent
            self._parent = None
        else:
            self.set_parent(None)
            self._parent = parent
            if self._parent._hwnd == None:
                self._createops.append((self.set_parent, (parent,)))
            elif self._hwnd == None:
                self._hinst = winuser.GetWindowLong(self._parent._hwnd, winuser.GWL_HINSTANCE)
                self._hwnd = winuser.CreateWindowEx(
                          winuser.WS_EX_TOPMOST,
                          self._wclass,
                          '',
                          self._style,
                          # Size and position values are given explicitly, because the CW_USEDEFAULT constant gives zero values for buttons. 
                          0,        # starting x position 
                          0,        # starting y position 
                          0,        # button width 
                          0,        # button height 
                          self._parent._hwnd,      # parent window 
                          windef.NULL,      # No menu 
                          windef.NULL, 
                          windef.NULL);     # pointer not needed
                
                winuser.SetWindowPos(self._hwnd, winuser.HWND_TOPMOST, 0,0,0,0, winuser.SWP_NOMOVE | winuser.SWP_NOSIZE | winuser.SWP_NOACTIVATE)
                
                ti = commctrl.TOOLINFO()
                ti.cbSize = 44
                ti.uFlags = commctrl.TTF_SUBCLASS
                ti.hwnd = self._parent._hwnd 
                ti.hinst = windef.NULL
                ti.uId = 0; 
                ti.lpszText = self._caption; 
                prect = self._parent.get_rect()
                ti.rect = wintypes.RECT()
                ti.rect.left = prect.x
                ti.rect.top = prect.y
                ti.rect.right = prect.x + prect.width
                ti.rect.bottom = prect.y + prect.height
                winuser.SendMessage(self._hwnd, commctrl.TTM_ADDTOOL, 0, byref(ti))
                #winuser.SendMessage(self._hwnd, commctrl.TTM_ACTIVATE, windef.TRUE, 0)

                #newfont = wingdi.CreateFont(-11,0,0,0,wingdi.FW_NORMAL,False, False, False,wingdi.DEFAULT_CHARSET, wingdi.OUT_DEFAULT_PRECIS, wingdi.CLIP_DEFAULT_PRECIS,wingdi.DEFAULT_QUALITY, wingdi.DEFAULT_PITCH | wingdi.FF_DONTCARE, 'Tahoma')
                #winuser.SendMessage(self._hwnd, winuser.WM_SETFONT, newfont, winuser.MAKELPARAM(windef.TRUE, 0))
                self.emit('created')
            else:
                self._parent.draw()

    def set_text(self, text):
        self._caption = text
        if (self._parent <> None) and (self._parent._hwnd <> None):
            ti = commctrl.TOOLINFO()
            ti.cbSize = 44
            ti.hwnd = self._parent._hwnd 
            ti.hinst = self._hinst
            ti.uId = 0; 
            ti.lpszText = self._caption; 
            prect = self._parent.get_rect()
            ti.rect = wintypes.RECT()
            ti.rect.left = prect.x
            ti.rect.top = prect.y
            ti.rect.right = prect.x + prect.width
            ti.rect.bottom = prect.y + prect.height
            winuser.SendMessage(self._hwnd, commctrl.TTM_ADDTOOL, 0, byref(ti))
            winuser.SendMessage(self._hwnd, commctrl.TTM_ACTIVATE, windef.TRUE, 0)
        else:
            self._queue.append((self.set_text, (text,)))
            return

    def _load_rect(self):
        pass



class AbstractButton(Control):
    def __init__(self, text):
        Control.__init__(self)
        self.set_text(text)
        self._wclass = 'BUTTON'
        self.set_prefered_size(75, 25)
        self._style = winuser.BS_PUSHBUTTON



class Button(AbstractButton):
    def __init__(self, text = ''):
        AbstractButton.__init__(self, text)



class AbstractPushButton(AbstractButton):
    def __init__(self, text):
        AbstractButton.__init__(self, text)
        self.set_selected(False)

    def set_selected(self, value):
        self._selected = value
        if self._hwnd == None:
            self._queue.append((self.set_selected, (value,)))
            return
        if value:
            fCheck = winuser.BST_CHECKED
        else:
            fCheck = winuser.BST_UNCHECKED
        winuser.SendMessage(self._hwnd, winuser.BM_SETCHECK, fCheck, 0)
        self.emit('button_selected')

    def is_selected(self):
        return self._selected



class PushButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._style = winuser.BS_FLAT



class CheckButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._style = winuser.BS_AUTOCHECKBOX
        self.connect('clicked', self.__process_clicked)

    def __process_clicked(self, source):
        self.set_selected(not self.is_selected())



class RadioButton(AbstractPushButton):
    def __init__(self, text):
        AbstractPushButton.__init__(self, text)
        self._style = winuser.BS_AUTORADIOBUTTON



class TextEdit(Control):
    def __init__(self, text=''):
        Control.__init__(self)
        self.set_text(text)
        self._wclass = 'EDIT'
        self._style = winuser.WS_BORDER | winuser.ES_AUTOHSCROLL
        self.set_prefered_size(100, 20)

    def get_text(self):
        textbuff = c_char_p('')
        if self._hwnd <> None:
            winuser.GetWindowText(self._hwnd , textbuff, winuser.GetWindowTextLength(self._hwnd) + 1)
        self._caption = textbuff.value
        return self._caption



class TextArea(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._wclass = 'EDIT'
        self._style = winuser.WS_BORDER | winuser.ES_MULTILINE | winuser.WS_HSCROLL | winuser.WS_VSCROLL
        self.set_prefered_size(200, 100)



class PasswordField(TextEdit):
    def __init__(self, text=''):
        TextEdit.__init__(self, text)
        self._wclass = 'EDIT'
        self._style = winuser.WS_BORDER | winuser.ES_PASSWORD | winuser.ES_AUTOHSCROLL



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