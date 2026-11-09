# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_reward_item_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_reward_item_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class ProgressionState(Enum):
    REWARD_RECEIVED = 'rewardReceived'
    REWARD_IN_PROGRESS = 'rewardInProgress'
    REWARD_LOCKED = 'rewardLocked'


class RewardType(Enum):
    STYLE_2D = 'style2D'
    CREW_MEMBER = 'crewMember'
    BIG_LOOTBOX = 'lootBox'


class ProgressionRewardItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ProgressionRewardItemViewModel, self).__init__(properties=properties, commands=commands)

    def getRequiredOpenedDoorsAmount(self):
        return self._getNumber(0)

    def setRequiredOpenedDoorsAmount(self, value):
        self._setNumber(0, value)

    def getActualOpenedDoorsAmount(self):
        return self._getNumber(1)

    def setActualOpenedDoorsAmount(self, value):
        self._setNumber(1, value)

    def getState(self):
        return ProgressionState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def getTooltipContentId(self):
        return self._getNumber(4)

    def setTooltipContentId(self, value):
        self._setNumber(4, value)

    def getRewardType(self):
        return RewardType(self._getString(5))

    def setRewardType(self, value):
        self._setString(5, value.value)

    def _initialize(self):
        super(ProgressionRewardItemViewModel, self)._initialize()
        self._addNumberProperty('requiredOpenedDoorsAmount', 0)
        self._addNumberProperty('actualOpenedDoorsAmount', 0)
        self._addStringProperty('state')
        self._addStringProperty('tooltipId', '')
        self._addNumberProperty('tooltipContentId', 0)
        self._addStringProperty('rewardType')
