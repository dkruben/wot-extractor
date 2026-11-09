# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/veh_skill_tree/tooltips/rewards_slot_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/veh_skill_tree/tooltips/rewards_slot_tooltip_model.py
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class RewardsSlotTooltipModel(IconBonusModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(RewardsSlotTooltipModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(9)

    def setTitle(self, value):
        self._setString(9, value)

    def getSubtitle(self):
        return self._getString(10)

    def setSubtitle(self, value):
        self._setString(10, value)

    def getDescription(self):
        return self._getString(11)

    def setDescription(self, value):
        self._setString(11, value)

    def getRarity(self):
        return self._getString(12)

    def setRarity(self, value):
        self._setString(12, value)

    def _initialize(self):
        super(RewardsSlotTooltipModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('subtitle', '')
        self._addStringProperty('description', '')
        self._addStringProperty('rarity', '')
