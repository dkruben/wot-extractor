# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/tooltips/selectable_reward_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/tooltips/selectable_reward_tooltip_model.py
from frameworks.wulf import ViewModel

class SelectableRewardTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SelectableRewardTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def getPurchaseDiscount(self):
        return self._getNumber(1)

    def setPurchaseDiscount(self, value):
        self._setNumber(1, value)

    def getResearchDiscount(self):
        return self._getNumber(2)

    def setResearchDiscount(self, value):
        self._setNumber(2, value)

    def getIsDiscount(self):
        return self._getBool(3)

    def setIsDiscount(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(SelectableRewardTooltipModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addNumberProperty('purchaseDiscount', 0)
        self._addNumberProperty('researchDiscount', 0)
        self._addBoolProperty('isDiscount', False)
