# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ProgressTimersPanelMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProgressTimersPanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ProgressTimersPanelMeta(BaseDAAPIComponent):

    def as_setLocalizedDataS(self, type, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setLocalizedData(type, data)

    def as_showS(self, timerTypeID, state, id):
        if self._isDAAPIInited():
            return self.flashObject.as_show(timerTypeID, state, id)

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()

    def as_setStateS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state)

    def as_setTimeStringS(self, cooldownTime):
        if self._isDAAPIInited():
            return self.flashObject.as_setTimeString(cooldownTime)

    def as_setProgressValueS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressValue(progress)
