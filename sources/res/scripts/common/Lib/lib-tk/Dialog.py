# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib-tk/Dialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib-tk/Dialog.py
from Tkinter import *
from Tkinter import _cnfmerge
if TkVersion <= 3.6:
    DIALOG_ICON = 'warning'
else:
    DIALOG_ICON = 'questhead'

class Dialog(Widget):

    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(self.tk.call('tk_dialog', self._w, cnf['title'], cnf['text'], cnf['bitmap'], cnf['default'], *cnf['strings']))
        try:
            Widget.destroy(self)
        except TclError:
            pass

    def destroy(self):
        pass


def _test():
    d = Dialog(None, {'title': 'File Modified', 'text': 'File "Python.h" has been modified since the last time it was saved. Do you want to save it before exiting the application.', 
       'bitmap': DIALOG_ICON, 
       'default': 0, 
       'strings': ('Save File', 'Discard Changes', 'Return to Editor')})
    print d.num
    return


if __name__ == '__main__':
    t = Button(None, {'text': 'Test', 'command': _test, 
       Pack: {}})
    q = Button(None, {'text': 'Quit', 'command': (t.quit), 
       Pack: {}})
    t.mainloop()
