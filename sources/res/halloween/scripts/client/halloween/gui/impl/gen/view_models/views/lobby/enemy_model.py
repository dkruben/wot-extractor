# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/enemy_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/enemy_model.py
from frameworks.wulf import ViewModel

class EnemyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(EnemyModel, self).__init__(properties=properties, commands=commands)

    def getIntCD(self):
        return self._getNumber(0)

    def setIntCD(self, value):
        self._setNumber(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getResourceKey(self):
        return self._getString(2)

    def setResourceKey(self, value):
        self._setString(2, value)

    def getRole(self):
        return self._getString(3)

    def setRole(self, value):
        self._setString(3, value)

    def getAbility(self):
        return self._getString(4)

    def setAbility(self, value):
        self._setString(4, value)

    def getUnlockedByMission(self):
        return self._getNumber(5)

    def setUnlockedByMission(self, value):
        self._setNumber(5, value)

    def getHasShopStyle(self):
        return self._getBool(6)

    def setHasShopStyle(self, value):
        self._setBool(6, value)

    def getIsNew(self):
        return self._getBool(7)

    def setIsNew(self, value):
        self._setBool(7, value)

    def getIsLocked(self):
        return self._getBool(8)

    def setIsLocked(self, value):
        self._setBool(8, value)

    def _initialize(self):
        super(EnemyModel, self)._initialize()
        self._addNumberProperty('intCD', 0)
        self._addStringProperty('name', '')
        self._addStringProperty('resourceKey', '')
        self._addStringProperty('role', '')
        self._addStringProperty('ability', '')
        self._addNumberProperty('unlockedByMission', 0)
        self._addBoolProperty('hasShopStyle', False)
        self._addBoolProperty('isNew', False)
        self._addBoolProperty('isLocked', False)
