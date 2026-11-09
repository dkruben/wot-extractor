# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_reward_award_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_reward_award_view_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class ShopOnOpenState(Enum):
    AVAILABLE = 'available'
    NOT_AVAILABLE = 'notAvailable'
    DISABLED = 'disabled'


class SeniorityRewardAwardViewModel(ViewModel):
    __slots__ = ('onOpenBtnClick', 'onShopBtnClick')

    def __init__(self, properties=5, commands=2):
        super(SeniorityRewardAwardViewModel, self).__init__(properties=properties, commands=commands)

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)

    def getMaxCategory(self):
        return self._getString(1)

    def setMaxCategory(self, value):
        self._setString(1, value)

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getSpecialCurrencyCount(self):
        return self._getNumber(3)

    def setSpecialCurrencyCount(self, value):
        self._setNumber(3, value)

    def getShopOnOpenState(self):
        return ShopOnOpenState(self._getString(4))

    def setShopOnOpenState(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(SeniorityRewardAwardViewModel, self)._initialize()
        self._addStringProperty('category', '')
        self._addStringProperty('maxCategory', '')
        self._addArrayProperty('bonuses', Array())
        self._addNumberProperty('specialCurrencyCount', -1)
        self._addStringProperty('shopOnOpenState', ShopOnOpenState.NOT_AVAILABLE.value)
        self.onOpenBtnClick = self._addCommand('onOpenBtnClick')
        self.onShopBtnClick = self._addCommand('onShopBtnClick')
