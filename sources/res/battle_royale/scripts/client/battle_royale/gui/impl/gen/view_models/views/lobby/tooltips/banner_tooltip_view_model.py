# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/banner_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/banner_tooltip_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel

class PerformanceRisk(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class BannerTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BannerTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def eventInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    def getTime(self):
        return self._getNumber(1)

    def setTime(self, value):
        self._setNumber(1, value)

    def getModeState(self):
        return self._getString(2)

    def setModeState(self, value):
        self._setString(2, value)

    def getPerformanceRisk(self):
        return PerformanceRisk(self._getString(3))

    def setPerformanceRisk(self, value):
        self._setString(3, value.value)

    def _initialize(self):
        super(BannerTooltipViewModel, self)._initialize()
        self._addViewModelProperty('eventInfo', BattleRoyaleEventModel())
        self._addNumberProperty('time', 0)
        self._addStringProperty('modeState', '')
        self._addStringProperty('performanceRisk', PerformanceRisk.HIGH.value)
