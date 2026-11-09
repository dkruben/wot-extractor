# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BrowserViewStackExPaddingMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BrowserViewStackExPaddingMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BrowserViewStackExPaddingMeta(BaseDAAPIComponent):

    def setViewSize(self, width, height):
        self._printOverrideError('setViewSize')

    def as_setAllowWaitingS(self, value, startImmediately):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllowWaiting(value, startImmediately)

    def as_setWaitingMessageS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaitingMessage(value)

    def as_createBrowserViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_createBrowserView()
