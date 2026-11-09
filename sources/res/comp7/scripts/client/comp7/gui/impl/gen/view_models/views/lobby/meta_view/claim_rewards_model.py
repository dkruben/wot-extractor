# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/claim_rewards_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/claim_rewards_model.py
from frameworks.wulf import ViewModel

class ClaimRewardsModel(ViewModel):
    __slots__ = ('onGoToRewardSelection', )

    def __init__(self, properties=2, commands=1):
        super(ClaimRewardsModel, self).__init__(properties=properties, commands=commands)

    def getRewardsCount(self):
        return self._getNumber(0)

    def setRewardsCount(self, value):
        self._setNumber(0, value)

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(ClaimRewardsModel, self)._initialize()
        self._addNumberProperty('rewardsCount', 0)
        self._addBoolProperty('isDisabled', False)
        self.onGoToRewardSelection = self._addCommand('onGoToRewardSelection')
