# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/reward_view_rewards_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/reward_view_rewards_model.py
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.rewards_model import RewardsModel

class RewardViewRewardsModel(RewardsModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(RewardViewRewardsModel, self).__init__(properties=properties, commands=commands)

    def getCurrentProgress(self):
        return self._getNumber(14)

    def setCurrentProgress(self, value):
        self._setNumber(14, value)

    def getAnimation(self):
        return self._getString(15)

    def setAnimation(self, value):
        self._setString(15, value)

    def _initialize(self):
        super(RewardViewRewardsModel, self)._initialize()
        self._addNumberProperty('currentProgress', 0)
        self._addStringProperty('animation', '')
