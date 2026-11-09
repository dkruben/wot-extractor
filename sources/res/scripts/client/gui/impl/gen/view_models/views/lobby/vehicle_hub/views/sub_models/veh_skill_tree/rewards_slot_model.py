# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/rewards_slot_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/rewards_slot_model.py
from enum import Enum
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class RewardStatus(Enum):
    AVAILABLE = 'available'
    BLOCKED = 'blocked'
    PROGRESS = 'progress'
    ACHIEVED = 'achieved'


class RewardsSlotModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(RewardsSlotModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(9)

    def setLevel(self, value):
        self._setNumber(9, value)

    def getTitle(self):
        return self._getString(10)

    def setTitle(self, value):
        self._setString(10, value)

    def getSubtitle(self):
        return self._getString(11)

    def setSubtitle(self, value):
        self._setString(11, value)

    def getHasPreview(self):
        return self._getBool(12)

    def setHasPreview(self, value):
        self._setBool(12, value)

    def getRarity(self):
        return self._getString(13)

    def setRarity(self, value):
        self._setString(13, value)

    def getState(self):
        return RewardStatus(self._getString(14))

    def setState(self, value):
        self._setString(14, value.value)

    def _initialize(self):
        super(RewardsSlotModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addStringProperty('title', '')
        self._addStringProperty('subtitle', '')
        self._addBoolProperty('hasPreview', False)
        self._addStringProperty('rarity', '')
        self._addStringProperty('state')
