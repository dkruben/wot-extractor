# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/box_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/box_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.slot_model import SlotModel

class BoxModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BoxModel, self).__init__(properties=properties, commands=commands)

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)

    def getCountToGuaranteed(self):
        return self._getNumber(2)

    def setCountToGuaranteed(self, value):
        self._setNumber(2, value)

    def getGuaranteedLimit(self):
        return self._getNumber(3)

    def setGuaranteedLimit(self, value):
        self._setNumber(3, value)

    def getSlots(self):
        return self._getArray(4)

    def setSlots(self, value):
        self._setArray(4, value)

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getRerollCurrency(self):
        return self._getString(5)

    def setRerollCurrency(self, value):
        self._setString(5, value)

    def getRerollPrices(self):
        return self._getArray(6)

    def setRerollPrices(self, value):
        self._setArray(6, value)

    @staticmethod
    def getRerollPricesType():
        return int

    def _initialize(self):
        super(BoxModel, self)._initialize()
        self._addStringProperty('category', '')
        self._addNumberProperty('count', 0)
        self._addNumberProperty('countToGuaranteed', 0)
        self._addNumberProperty('guaranteedLimit', 0)
        self._addArrayProperty('slots', Array())
        self._addStringProperty('rerollCurrency', '')
        self._addArrayProperty('rerollPrices', Array())
