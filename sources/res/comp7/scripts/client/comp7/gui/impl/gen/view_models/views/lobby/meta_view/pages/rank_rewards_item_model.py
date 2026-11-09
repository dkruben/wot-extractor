# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/rank_rewards_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/rank_rewards_item_model.py
from frameworks.wulf import Array
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel

class RankRewardsItemModel(ProgressionItemBaseModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RankRewardsItemModel, self).__init__(properties=properties, commands=commands)

    def getHasRewardsReceived(self):
        return self._getBool(4)

    def setHasRewardsReceived(self, value):
        self._setBool(4, value)

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)

    @staticmethod
    def getRewardsType():
        return Comp7BonusModel

    def _initialize(self):
        super(RankRewardsItemModel, self)._initialize()
        self._addBoolProperty('hasRewardsReceived', False)
        self._addArrayProperty('rewards', Array())
