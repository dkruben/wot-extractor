# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehicleInfoMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleInfoMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleInfoMeta(AbstractWindowView):

    def getVehicleInfo(self):
        self._printOverrideError('getVehicleInfo')

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def addToCompare(self):
        self._printOverrideError('addToCompare')

    def changeNation(self):
        self._printOverrideError('changeNation')

    def as_setVehicleInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleInfo(data)

    def as_setCompareButtonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setCompareButtonData(data)

    def as_setChangeNationButtonDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setChangeNationButtonData(data)
