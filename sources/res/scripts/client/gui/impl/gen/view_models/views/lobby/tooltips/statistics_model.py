# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/statistics_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tooltips/statistics_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel

class StatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(StatisticsModel, self).__init__(properties=properties, commands=commands)

    def getElite(self):
        return self._getBool(0)

    def setElite(self, value):
        self._setBool(0, value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)

    def getPremium(self):
        return self._getBool(3)

    def setPremium(self, value):
        self._setBool(3, value)

    def getName(self):
        return self._getString(4)

    def setName(self, value):
        self._setString(4, value)

    def getNationId(self):
        return self._getNumber(5)

    def setNationId(self, value):
        self._setNumber(5, value)

    def getRole(self):
        return self._getNumber(6)

    def setRole(self, value):
        self._setNumber(6, value)

    def getRentLeftTime(self):
        return self._getNumber(7)

    def setRentLeftTime(self, value):
        self._setNumber(7, value)

    def getRentLeftBattles(self):
        return self._getNumber(8)

    def setRentLeftBattles(self, value):
        self._setNumber(8, value)

    def getRentLeftWins(self):
        return self._getNumber(9)

    def setRentLeftWins(self, value):
        self._setNumber(9, value)

    def getSlots(self):
        return self._getArray(10)

    def setSlots(self, value):
        self._setArray(10, value)

    @staticmethod
    def getSlotsType():
        return SlotModel

    def _initialize(self):
        super(StatisticsModel, self)._initialize()
        self._addBoolProperty('elite', False)
        self._addNumberProperty('level', 0)
        self._addStringProperty('type', '')
        self._addBoolProperty('premium', False)
        self._addStringProperty('name', '')
        self._addNumberProperty('nationId', 0)
        self._addNumberProperty('role', 0)
        self._addNumberProperty('rentLeftTime', 0)
        self._addNumberProperty('rentLeftBattles', 0)
        self._addNumberProperty('rentLeftWins', 0)
        self._addArrayProperty('slots', Array())
