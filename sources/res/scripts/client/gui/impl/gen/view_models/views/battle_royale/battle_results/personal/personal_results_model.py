# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/personal/personal_results_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle_royale/battle_results/personal/personal_results_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.battle_reward_item_model import BattleRewardItemModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.stat_item_model import StatItemModel

class PersonalResultsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PersonalResultsModel, self).__init__(properties=properties, commands=commands)

    def getFinishResultLabel(self):
        return self._getResource(0)

    def setFinishResultLabel(self, value):
        self._setResource(0, value)

    def getStatsList(self):
        return self._getArray(1)

    def setStatsList(self, value):
        self._setArray(1, value)

    @staticmethod
    def getStatsListType():
        return StatItemModel

    def getBattleRewardsList(self):
        return self._getArray(2)

    def setBattleRewardsList(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBattleRewardsListType():
        return BattleRewardItemModel

    def getBattleRewardsListWithPremium(self):
        return self._getArray(3)

    def setBattleRewardsListWithPremium(self, value):
        self._setArray(3, value)

    @staticmethod
    def getBattleRewardsListWithPremiumType():
        return BattleRewardItemModel

    def _initialize(self):
        super(PersonalResultsModel, self)._initialize()
        self._addResourceProperty('finishResultLabel', R.invalid())
        self._addArrayProperty('statsList', Array())
        self._addArrayProperty('battleRewardsList', Array())
        self._addArrayProperty('battleRewardsListWithPremium', Array())
