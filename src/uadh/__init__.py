class VoidObject:
    pass

class UObject:
    
    def __init__(self):
        self._listeners = {}
        pass

    def add_event(self, event):
        if not (event in self._listeners.keys()):
            self._listeners[event] = []

    def remove_event(self, event):
        if (event in self._listeners.keys()):
            del(self._listeners[event])

    def emit(self, event, obj=None):
        if obj == None:
            obj = self
        if event in self._listeners.keys():
            for listener in self._listeners[event]:
                listener(self)

    def get_events(self):
        return self._listeners.keys()

    def connect(self, event, listener):
        if event in self._listeners.keys():
            self._listeners[event].append(listener)

    def disconnect(self, event, listener):
        if event in self._listeners.keys():
            index = 0
            for listenerfunc in self._listeners[event]:
                if repr(listener) == repr(listenerfunc):
                    del(self._listeners[event][index])
                index = index + 1

    def __eq__(self, other):
        return repr(self) == repr(other)