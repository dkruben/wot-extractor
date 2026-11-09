# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/widget/event_shop_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/widget/event_shop_model.py
from frameworks.wulf import ViewModel

class EventShopModel(ViewModel):
    __slots__ = ('openShop', )

    def __init__(self, properties=2, commands=1):
        super(EventShopModel, self).__init__(properties=properties, commands=commands)

    def getIsWGMoneyAvailable(self):
        return self._getBool(0)

    def setIsWGMoneyAvailable(self, value):
        self._setBool(0, value)

    def getBalance(self):
        return self._getNumber(1)

    def setBalance(self, value):
        self._setNumber(1, value)

    def _initialize(self):
        super(EventShopModel, self)._initialize()
        self._addBoolProperty('isWGMoneyAvailable', False)
        self._addNumberProperty('balance', 0)
        self.openShop = self._addCommand('openShop')
