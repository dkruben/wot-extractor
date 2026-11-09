# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoWindow.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/FreeXPInfoWindow.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.FreeXPInfoWindowMeta import FreeXPInfoWindowMeta
__author__ = 'd_savitski'

class FreeXPInfoWindow(FreeXPInfoWindowMeta):

    def __init__(self, ctx=None):
        super(FreeXPInfoWindow, self).__init__()
        self.meta = ctx.get('meta')
        self.handler = ctx.get('handler')

    def _populate(self):
        super(FreeXPInfoWindow, self)._populate()
        self.as_setTitleS(self.meta.getTitle())
        self.as_setSubmitLabelS(self.meta.getSubmitLbl())
        self.as_setTextS(self.meta.getTextInfo())

    def onWindowClose(self):
        self.handler(True)
        self.destroy()

    def onSubmitButton(self):
        self.onWindowClose()

    def onCancelButton(self):
        self.onWindowClose()

    def _dispose(self):
        super(FreeXPInfoWindow, self)._dispose()
        self.handler = None
        return
