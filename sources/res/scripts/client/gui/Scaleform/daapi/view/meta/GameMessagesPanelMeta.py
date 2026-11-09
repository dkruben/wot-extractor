# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/GameMessagesPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/GameMessagesPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class GameMessagesPanelMeta(BaseDAAPIComponent):

    def onMessageStarted(self, type, modificator, id):
        self._printOverrideError('onMessageStarted')

    def onMessagePhaseStarted(self, type, modificator, id):
        self._printOverrideError('onMessagePhaseStarted')

    def onMessageEnded(self, type, id):
        self._printOverrideError('onMessageEnded')

    def onMessageHiding(self, type, id):
        self._printOverrideError('onMessageHiding')

    def as_addMessageS(self, messageVO):
        if self._isDAAPIInited():
            return self.flashObject.as_addMessage(messageVO)

    def as_clearMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clearMessages()
