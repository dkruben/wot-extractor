# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/box_reroll_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/lootbox_system/box_reroll_model.py
from frameworks.wulf import ViewModel

class BoxRerollModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BoxRerollModel, self).__init__(properties=properties, commands=commands)

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)

    def getIsEnoughMoney(self):
        return self._getBool(1)

    def setIsEnoughMoney(self, value):
        self._setBool(1, value)

    def getCurrency(self):
        return self._getString(2)

    def setCurrency(self, value):
        self._setString(2, value)

    def getPrice(self):
        return self._getNumber(3)

    def setPrice(self, value):
        self._setNumber(3, value)

    def getAttemptsLeft(self):
        return self._getNumber(4)

    def setAttemptsLeft(self, value):
        self._setNumber(4, value)

    def getHasSpecialReward(self):
        return self._getBool(5)

    def setHasSpecialReward(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(BoxRerollModel, self)._initialize()
        self._addBoolProperty('isAvailable', False)
        self._addBoolProperty('isEnoughMoney', False)
        self._addStringProperty('currency', '')
        self._addNumberProperty('price', 0)
        self._addNumberProperty('attemptsLeft', 0)
        self._addBoolProperty('hasSpecialReward', False)
