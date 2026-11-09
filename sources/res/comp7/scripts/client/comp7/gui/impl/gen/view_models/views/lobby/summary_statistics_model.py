# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/summary_statistics_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/summary_statistics_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class SummaryStatisticsType(Enum):
    BATTLES = 'battles'
    DAMAGE = 'damage'
    MAXPRESTIGEPOINTS = 'maxPrestigePoints'
    MAXFRAGS = 'maxFrags'
    WINSERIES = 'winSeries'


class SummaryStatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SummaryStatisticsModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return SummaryStatisticsType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getMain(self):
        return self._getNumber(1)

    def setMain(self, value):
        self._setNumber(1, value)

    def getAdditional(self):
        return self._getReal(2)

    def setAdditional(self, value):
        self._setReal(2, value)

    def _initialize(self):
        super(SummaryStatisticsModel, self)._initialize()
        self._addStringProperty('type')
        self._addNumberProperty('main', 0)
        self._addRealProperty('additional', 0.0)
