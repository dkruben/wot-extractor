# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/tooltips/points_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/tooltips/points_tooltip_view_model.py
from frameworks.wulf import ViewModel

class PointsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(PointsTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getEndDate(self):
        return self._getNumber(0)

    def setEndDate(self, value):
        self._setNumber(0, value)

    def getEffective(self):
        return self._getNumber(1)

    def setEffective(self, value):
        self._setNumber(1, value)

    def getObelisk(self):
        return self._getNumber(2)

    def setObelisk(self, value):
        self._setNumber(2, value)

    def getMissionDaily(self):
        return self._getNumber(3)

    def setMissionDaily(self, value):
        self._setNumber(3, value)

    def getVehicleDaily(self):
        return self._getNumber(4)

    def setVehicleDaily(self, value):
        self._setNumber(4, value)

    def getBundleKey(self):
        return self._getString(5)

    def setBundleKey(self, value):
        self._setString(5, value)

    def getIsPostBattle(self):
        return self._getBool(6)

    def setIsPostBattle(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(PointsTooltipViewModel, self)._initialize()
        self._addNumberProperty('endDate', 0)
        self._addNumberProperty('effective', 0)
        self._addNumberProperty('obelisk', 0)
        self._addNumberProperty('missionDaily', 0)
        self._addNumberProperty('vehicleDaily', 0)
        self._addStringProperty('bundleKey', '')
        self._addBoolProperty('isPostBattle', False)
