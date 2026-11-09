# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/flag/flag_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/flag/flag_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class FlagViewModel(ViewModel):
    __slots__ = ()
    WIN = 'win'
    DRAW = 'tie'
    LOSE = 'lose'

    def __init__(self, properties=3, commands=0):
        super(FlagViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getWinStatus(self):
        return self._getString(1)

    def setWinStatus(self, value):
        self._setString(1, value)

    def getAchievements(self):
        return self._getArray(2)

    def setAchievements(self, value):
        self._setArray(2, value)

    @staticmethod
    def getAchievementsType():
        return PostbattleAchievementModel

    def _initialize(self):
        super(FlagViewModel, self)._initialize()
        self._addViewModelProperty('router', RouterModel())
        self._addStringProperty('winStatus', '')
        self._addArrayProperty('achievements', Array())
