# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_royale_reward_points.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_royale_reward_points.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tooltips.reward_points_by_place_model import RewardPointsByPlaceModel

class BattleRoyaleRewardPoints(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleRoyaleRewardPoints, self).__init__(properties=properties, commands=commands)

    def getSoloMode(self):
        return self._getArray(0)

    def setSoloMode(self, value):
        self._setArray(0, value)

    @staticmethod
    def getSoloModeType():
        return RewardPointsByPlaceModel

    def getSquadMode(self):
        return self._getArray(1)

    def setSquadMode(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSquadModeType():
        return RewardPointsByPlaceModel

    def _initialize(self):
        super(BattleRoyaleRewardPoints, self)._initialize()
        self._addArrayProperty('soloMode', Array())
        self._addArrayProperty('squadMode', Array())
