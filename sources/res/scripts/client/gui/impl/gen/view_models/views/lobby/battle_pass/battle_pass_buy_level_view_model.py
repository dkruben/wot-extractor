# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_buy_level_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_buy_level_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel

class BattlePassBuyLevelViewModel(ViewModel):
    __slots__ = ('onChangeSelectedLevels', 'onPurchase')

    def __init__(self, properties=7, commands=2):
        super(BattlePassBuyLevelViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)

    def getLevelsTotal(self):
        return self._getNumber(2)

    def setLevelsTotal(self, value):
        self._setNumber(2, value)

    def getLevelsPassed(self):
        return self._getNumber(3)

    def setLevelsPassed(self, value):
        self._setNumber(3, value)

    def getChapterID(self):
        return self._getNumber(4)

    def setChapterID(self, value):
        self._setNumber(4, value)

    def getLevelPrice(self):
        return self._getNumber(5)

    def setLevelPrice(self, value):
        self._setNumber(5, value)

    def getPurchaseAbortedCount(self):
        return self._getNumber(6)

    def setPurchaseAbortedCount(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(BattlePassBuyLevelViewModel, self)._initialize()
        self._addViewModelProperty('rewards', UserListModel())
        self._addBoolProperty('isWalletAvailable', False)
        self._addNumberProperty('levelsTotal', 0)
        self._addNumberProperty('levelsPassed', 0)
        self._addNumberProperty('chapterID', 0)
        self._addNumberProperty('levelPrice', 0)
        self._addNumberProperty('purchaseAbortedCount', 0)
        self.onChangeSelectedLevels = self._addCommand('onChangeSelectedLevels')
        self.onPurchase = self._addCommand('onPurchase')
