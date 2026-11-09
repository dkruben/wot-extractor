# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/br_base_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/br_base_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.leaderboard_model import LeaderboardModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.player_battle_type_status_model import PlayerBattleTypeStatusModel

class BrBaseViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BrBaseViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def leaderboardModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getLeaderboardModelType():
        return LeaderboardModel

    @property
    def playerBattleTypeStatus(self):
        return self._getViewModel(1)

    @staticmethod
    def getPlayerBattleTypeStatusType():
        return PlayerBattleTypeStatusModel

    def _initialize(self):
        super(BrBaseViewModel, self)._initialize()
        self._addViewModelProperty('leaderboardModel', LeaderboardModel())
        self._addViewModelProperty('playerBattleTypeStatus', PlayerBattleTypeStatusModel())
