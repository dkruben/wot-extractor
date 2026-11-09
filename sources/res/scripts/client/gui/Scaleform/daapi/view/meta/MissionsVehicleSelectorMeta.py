# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/MissionsVehicleSelectorMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsVehicleSelectorMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsVehicleSelectorMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_showSelectedVehicleS(self, vehData):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectedVehicle(vehData)

    def as_hideSelectedVehicleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSelectedVehicle()

    def as_closeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_close()
