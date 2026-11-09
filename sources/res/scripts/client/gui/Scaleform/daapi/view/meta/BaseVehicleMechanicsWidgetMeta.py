# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/BaseVehicleMechanicsWidgetMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BaseVehicleMechanicsWidgetMeta.py
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.components_common import VehicleMechanicDAAPIComponent

class BaseVehicleMechanicsWidgetMeta(VehicleMechanicDAAPIComponent):

    def as_setStateS(self, state, isInstantly=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(state, isInstantly)

    def as_setHotKeysS(self, keyCodes):
        if self._isDAAPIInited():
            return self.flashObject.as_setHotKeys(keyCodes)

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)

    def as_setCrosshairTypeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrosshairType(value)

    def as_setTimeS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setTime(time)
