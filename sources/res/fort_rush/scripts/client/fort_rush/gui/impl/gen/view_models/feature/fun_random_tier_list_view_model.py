# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/feature/fun_random_tier_list_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/feature/fun_random_tier_list_view_model.py
from frameworks.wulf import Array, ViewModel
from fort_rush.gui.impl.gen.view_models.views.lobby.common.fun_random_lootbox import FunRandomLootbox

class FunRandomTierListViewModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=2, commands=1):
        super(FunRandomTierListViewModel, self).__init__(properties=properties, commands=commands)

    def getLootBoxes(self):
        return self._getArray(0)

    def setLootBoxes(self, value):
        self._setArray(0, value)

    @staticmethod
    def getLootBoxesType():
        return FunRandomLootbox

    def getAssetsPointer(self):
        return self._getString(1)

    def setAssetsPointer(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(FunRandomTierListViewModel, self)._initialize()
        self._addArrayProperty('lootBoxes', Array())
        self._addStringProperty('assetsPointer', 'undefined')
        self.onClose = self._addCommand('onClose')
