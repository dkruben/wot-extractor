# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/leaderboard_reward_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/leaderboard_reward_tooltip_model.py
from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.reward_points_place_model import RewardPointsPlaceModel

class LeaderboardRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LeaderboardRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getBattleTypes(self):
        return self._getArray(0)

    def setBattleTypes(self, value):
        self._setArray(0, value)

    @staticmethod
    def getBattleTypesType():
        return unicode

    def getBattleModes(self):
        return self._getArray(1)

    def setBattleModes(self, value):
        self._setArray(1, value)

    @staticmethod
    def getBattleModesType():
        return Array[RewardPointsPlaceModel]

    def _initialize(self):
        super(LeaderboardRewardTooltipModel, self)._initialize()
        self._addArrayProperty('battleTypes', Array())
        self._addArrayProperty('battleModes', Array())
