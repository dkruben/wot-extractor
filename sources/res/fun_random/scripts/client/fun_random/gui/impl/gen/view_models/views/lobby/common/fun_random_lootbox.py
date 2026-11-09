# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_lootbox.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_lootbox.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

class FunRandomLootbox(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FunRandomLootbox, self).__init__(properties=properties, commands=commands)

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)

    def getIconKey(self):
        return self._getString(1)

    def setIconKey(self, value):
        self._setString(1, value)

    def getShowRewardsNames(self):
        return self._getBool(2)

    def setShowRewardsNames(self, value):
        self._setBool(2, value)

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        super(FunRandomLootbox, self)._initialize()
        self._addStringProperty('label', '')
        self._addStringProperty('iconKey', '')
        self._addBoolProperty('showRewardsNames', False)
        self._addArrayProperty('rewards', Array())
