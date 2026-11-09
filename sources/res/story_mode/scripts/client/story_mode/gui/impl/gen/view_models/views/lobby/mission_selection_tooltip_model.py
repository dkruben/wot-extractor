# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_selection_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_selection_tooltip_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MissionSelectionTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(MissionSelectionTooltipModel, self).__init__(properties=properties, commands=commands)

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)

    def getVehicleIcon(self):
        return self._getResource(1)

    def setVehicleIcon(self, value):
        self._setResource(1, value)

    def getVehicleDescription(self):
        return self._getString(2)

    def setVehicleDescription(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(MissionSelectionTooltipModel, self)._initialize()
        self._addStringProperty('vehicleName', '')
        self._addResourceProperty('vehicleIcon', R.invalid())
        self._addStringProperty('vehicleDescription', '')
