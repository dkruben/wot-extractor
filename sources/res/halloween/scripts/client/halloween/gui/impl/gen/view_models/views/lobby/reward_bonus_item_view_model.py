# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_bonus_item_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/reward_bonus_item_view_model.py
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class RewardBonusItemViewModel(BonusItemViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(RewardBonusItemViewModel, self).__init__(properties=properties, commands=commands)

    def getIsSecretReward(self):
        return self._getBool(9)

    def setIsSecretReward(self, value):
        self._setBool(9, value)

    def getSecretRewardTooltipMessage(self):
        return self._getString(10)

    def setSecretRewardTooltipMessage(self, value):
        self._setString(10, value)

    def _initialize(self):
        super(RewardBonusItemViewModel, self)._initialize()
        self._addBoolProperty('isSecretReward', False)
        self._addStringProperty('secretRewardTooltipMessage', '')
