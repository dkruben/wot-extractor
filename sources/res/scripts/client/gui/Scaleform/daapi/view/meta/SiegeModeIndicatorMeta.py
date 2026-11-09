# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/SiegeModeIndicatorMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SiegeModeIndicatorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SiegeModeIndicatorMeta(BaseDAAPIComponent):

    def as_switchSiegeStateS(self, totalTime, leftTime, siegeState, moduleState, isSmooth):
        if self._isDAAPIInited():
            return self.flashObject.as_switchSiegeState(totalTime, leftTime, siegeState, moduleState, isSmooth)

    def as_setAutoSiegeModeStateS(self, siegeState, moduleState):
        if self._isDAAPIInited():
            return self.flashObject.as_setAutoSiegeModeState(siegeState, moduleState)

    def as_switchSiegeStateSnapshotS(self, totalTime, leftTime, siegeState, moduleState, isSmooth):
        if self._isDAAPIInited():
            return self.flashObject.as_switchSiegeStateSnapshot(totalTime, leftTime, siegeState, moduleState, isSmooth)

    def as_updateDeviceStateS(self, deviceName, deviceState):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDeviceState(deviceName, deviceState)

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)

    def as_setSiegeModeTypeS(self, type):
        if self._isDAAPIInited():
            return self.flashObject.as_setSiegeModeType(type)
