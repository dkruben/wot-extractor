# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/PveSecondaryObjectivesMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PveSecondaryObjectivesMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class PveSecondaryObjectivesMeta(BaseDAAPIComponent):

    def as_addObjectS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_addObject(data)

    def as_removeObjectS(self, id, state):
        if self._isDAAPIInited():
            return self.flashObject.as_removeObject(id, state)

    def as_setProgressBarValueS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressBarValue(id, value)

    def as_updateTimeS(self, id, value, isWarning):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTime(id, value, isWarning)

    def as_setAlarmS(self, id, isAlarm):
        if self._isDAAPIInited():
            return self.flashObject.as_setAlarm(id, isAlarm)

    def as_setTitleS(self, id, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(id, title)

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
