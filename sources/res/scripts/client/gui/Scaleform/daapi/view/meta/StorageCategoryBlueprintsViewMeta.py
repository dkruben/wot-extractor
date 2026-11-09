# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryBlueprintsViewMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StorageCategoryBlueprintsViewMeta.py
from gui.Scaleform.daapi.view.lobby.storage.vehicle_view import VehicleView

class StorageCategoryBlueprintsViewMeta(VehicleView):

    def navigateToBlueprintScreen(self, itemId):
        self._printOverrideError('navigateToBlueprintScreen')

    def selectConvertible(self, value):
        self._printOverrideError('selectConvertible')

    def as_updateIntelligenceDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateIntelligenceData(data)

    def as_updateNationalFragmentsS(self, fragments):
        if self._isDAAPIInited():
            return self.flashObject.as_updateNationalFragments(fragments)

    def as_updateCanConvertS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCanConvert(value)
