# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/RadialMenuMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RadialMenuMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RadialMenuMeta(BaseDAAPIComponent):

    def onSelect(self):
        self._printOverrideError('onSelect')

    def onAction(self, action):
        self._printOverrideError('onAction')

    def onHideCompleted(self):
        self._printOverrideError('onHideCompleted')

    def onRefresh(self):
        self._printOverrideError('onRefresh')

    def as_buildDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_buildData(data)

    def as_showS(self, cursorX, cursorY, radialState, staticShortcutsDiff, replyStateDiff, offset):
        if self._isDAAPIInited():
            return self.flashObject.as_show(cursorX, cursorY, radialState, staticShortcutsDiff, replyStateDiff, offset)

    def as_hideS(self, allowAction):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(allowAction)
