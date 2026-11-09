# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/reward_product_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/reward_product_model.py
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel
from comp7.gui.impl.gen.view_models.views.lobby.comp7_bonus_model import Comp7BonusModel

class RewardProductModel(BaseProductModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(RewardProductModel, self).__init__(properties=properties, commands=commands)

    @property
    def reward(self):
        return self._getViewModel(9)

    @staticmethod
    def getRewardType():
        return Comp7BonusModel

    def _initialize(self):
        super(RewardProductModel, self)._initialize()
        self._addViewModelProperty('reward', Comp7BonusModel())
