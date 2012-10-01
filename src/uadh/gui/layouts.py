'''
Created on 29/03/2012

@author: xXx
'''
from uadh.gui.base import Rect

class Layout:
    def __init__(self):
        pass

    def add_layout_widget(self, widget, position):
        raise NotImplementedError()

    def do_layout(self, container):
        raise NotImplementedError()

class BorderLayout(Layout):
    TOP    = 0
    DOWN   = 1
    LEFT   = 2
    RIGHT  = 3
    CENTER = 4

    def __init__(self):
        self.top = self.down = self.left = self.right = self.center = None

    def __get_widget(self, position):
        if position == self.CENTER:
            return self.center
        elif position == self.DOWN:
            return self.down
        elif position == self.LEFT:
            return self.left
        elif position == self.RIGHT:
            return self.right
        else:
            return self.top

    def add_layout_widget(self, widget, position):
        if position == self.CENTER:
            self.center = widget
        elif position == self.DOWN:
            self.down = widget
        elif position == self.LEFT:
            self.left = widget
        elif position == self.RIGHT:
            self.right = widget
        else:
            self.top = widget

    def do_layout(self, container):
        container_rect = container.get_rect()

        toppos = 0
        bottompos = container_rect.height
        leftpos = 0
        rightpos = container_rect.width
        
        if self.top <> None:
            size = self.top.get_prefered_size()
            rect = Rect(rightpos, size.height, leftpos, toppos)
            self.top.set_rect(rect)
            toppos = toppos + size.height
        if self.down <> None:
            size = self.down.get_prefered_size()
            rect = Rect(rightpos, size.height, leftpos, bottompos - size.height)
            self.down.set_rect(rect)
            bottompos = bottompos - rect.height
        if self.left <> None:
            size = self.left.get_prefered_size()
            rect = Rect(size.width, bottompos - toppos, leftpos, toppos)
            self.left.set_rect(rect)
            leftpos = leftpos + size.width
        if self.right <> None:
            size = self.right.get_prefered_size()
            rect = Rect(size.width, bottompos - toppos, rightpos - size.width, toppos)
            self.right.set_rect(rect)
            rightpos = rightpos - size.width
        if self.center <> None:
            #size = self.center.get_prefered_size()
            rect = Rect(rightpos - leftpos, bottompos - toppos, leftpos, toppos)
            self.center.set_rect(rect)



class GridLayout(Layout):
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols

    def do_layout(self, container):
        cont = container.get_child_count()
        if cont == 0:
            return
        if self.__cols > 0:
            rows = (cont + self.__cols - 1) / self.__cols
            cols = self.__cols
        else:
            cols = (cont + self.__rows -1) / self.__rows
            rows = self.__rows
        container_rect = container.get_rect()
        toppos = 0#container_rect.y
        leftpos = 0#container_rect.x
        wwidth =  container_rect.width / cols
        wheight = container_rect.height / rows
        i = 0
        while i<cont :
            widget = container.get_child(i)
            widget.set_position(leftpos, toppos)
            widget.set_size(wwidth, wheight)
            i = i + 1
            if (i % cols) == 0:
                leftpos = 0#container_rect.x
                toppos = toppos + wheight
            else:
                leftpos = leftpos + wwidth

    def add_layout_widget(self, widget, position):
        pass



class BoxLayout(Layout):
    def __init__(self):
        pass

    def do_layout(self, container):
        pass

    def add_layout_widget(self, widget, position):
        pass
