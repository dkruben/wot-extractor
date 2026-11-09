# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/tooltips/leaderboard_reward_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/tooltips/leaderboard_reward_tooltip_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'
    SIMPLIFIED = 'simplified'


class LeaderboardRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LeaderboardRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return State(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getSeasonEndTimestamp(self):
        return self._getNumber(1)

    def setSeasonEndTimestamp(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(LeaderboardRewardTooltipModel, self)._initialize()
        self._addStringProperty('state')
        self._addNumberProperty('seasonEndTimestamp', 0)
