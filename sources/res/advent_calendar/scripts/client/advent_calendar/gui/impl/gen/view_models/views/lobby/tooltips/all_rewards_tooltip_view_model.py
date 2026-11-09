# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/tooltips/all_rewards_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/tooltips/all_rewards_tooltip_view_model.py
from frameworks.wulf import Array, ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.bonus_item_view_model import BonusItemViewModel

class AllRewardsTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AllRewardsTooltipViewModel, self).__init__(properties=properties, commands=commands)

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def _initialize(self):
        super(AllRewardsTooltipViewModel, self)._initialize()
        self._addArrayProperty('rewards', Array())
