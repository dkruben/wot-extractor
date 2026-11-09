# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/rewards_selection_view/reward_option_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/rewards_selection_view/reward_option_model.py
from frameworks.wulf import ViewModel

class RewardOptionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardOptionModel, self).__init__(properties=properties, commands=commands)

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getGiftId(self):
        return self._getNumber(2)

    def setGiftId(self, value):
        self._setNumber(2, value)

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def getCount(self):
        return self._getNumber(4)

    def setCount(self, value):
        self._setNumber(4, value)

    def getDescription(self):
        return self._getString(5)

    def setDescription(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(RewardOptionModel, self)._initialize()
        self._addStringProperty('iconName', '')
        self._addStringProperty('name', '')
        self._addNumberProperty('giftId', 0)
        self._addStringProperty('tooltipId', '')
        self._addNumberProperty('count', 0)
        self._addStringProperty('description', '')
