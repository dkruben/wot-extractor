# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleCompareViewMeta.py
from gui.Scaleform.daapi.view.meta.VehicleCompareCommonViewMeta import VehicleCompareCommonViewMeta

class VehicleCompareViewMeta(VehicleCompareCommonViewMeta):

    def onGoToPreviewClick(self, index):
        self._printOverrideError('onGoToPreviewClick')

    def onGoToHangarClick(self, vehicleID):
        self._printOverrideError('onGoToHangarClick')

    def onSelectModulesClick(self, vehicleID, index):
        self._printOverrideError('onSelectModulesClick')

    def onParamDeltaRequested(self, index, paramID):
        self._printOverrideError('onParamDeltaRequested')

    def onCrewLevelChanged(self, index, crewLevelID):
        self._printOverrideError('onCrewLevelChanged')

    def onRemoveVehicle(self, index):
        self._printOverrideError('onRemoveVehicle')

    def onRevertVehicle(self, index):
        self._printOverrideError('onRevertVehicle')

    def onRemoveAllVehicles(self):
        self._printOverrideError('onRemoveAllVehicles')

    def as_setParamsDeltaS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setParamsDelta(data)

    def as_setVehicleParamsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleParamsData(data)

    def as_getVehiclesDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getVehiclesDP()

    def as_setVehiclesCountTextS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesCountText(text)
