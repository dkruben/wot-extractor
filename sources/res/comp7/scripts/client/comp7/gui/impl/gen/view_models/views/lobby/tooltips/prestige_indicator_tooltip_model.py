# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/prestige_indicator_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/prestige_indicator_tooltip_model.py
from comp7.gui.impl.gen.view_models.views.lobby.enums import StatisticsMode
from frameworks.wulf import ViewModel

class PrestigeIndicatorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PrestigeIndicatorTooltipModel, self).__init__(properties=properties, commands=commands)

    def getStatisticsMode(self):
        return StatisticsMode(self._getNumber(0))

    def setStatisticsMode(self, value):
        self._setNumber(0, value.value)

    def getAveragePrestige(self):
        return self._getReal(1)

    def setAveragePrestige(self, value):
        self._setReal(1, value)

    def getRecordPrestige(self):
        return self._getReal(2)

    def setRecordPrestige(self, value):
        self._setReal(2, value)

    def getRecordPrestigeVehicleName(self):
        return self._getString(3)

    def setRecordPrestigeVehicleName(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(PrestigeIndicatorTooltipModel, self)._initialize()
        self._addNumberProperty('statisticsMode')
        self._addRealProperty('averagePrestige', 0.0)
        self._addRealProperty('recordPrestige', 0.0)
        self._addStringProperty('recordPrestigeVehicleName', '')
