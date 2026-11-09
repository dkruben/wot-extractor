# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/SystemMessageDialog.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/SystemMessageDialog.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.SystemMessageDialogMeta import SystemMessageDialogMeta

class SystemMessageDialog(SystemMessageDialogMeta):

    def __init__(self, meta, handler, **kwargs):
        super(SystemMessageDialog, self).__init__()
        self.__meta = meta
        self.__handler = handler

    def _populate(self):
        super(SystemMessageDialog, self)._populate()
        self.as_setInitDataS({'title': (self.__meta.getTitle()), 
           'closeBtnTitle': (self.__meta.getCancelLabel()), 
           'settings': (self.__meta.getSettings())})
        self.as_setMessageDataS(self.__meta.getMessageObject())

    def onWindowClose(self):
        self.destroy()

    def _dispose(self):
        if self.__handler:
            self.__handler(True)
        self.__meta.cleanUp()
        self.__meta = None
        self.__handler = None
        super(SystemMessageDialog, self)._dispose()
        return
