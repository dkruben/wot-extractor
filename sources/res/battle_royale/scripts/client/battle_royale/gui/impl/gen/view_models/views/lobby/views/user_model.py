# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/user_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/user_model.py
from frameworks.wulf import ViewModel

class UserModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(UserModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIsCurrentUser(self):
        return self._getBool(1)

    def setIsCurrentUser(self, value):
        self._setBool(1, value)

    def getIsReady(self):
        return self._getBool(2)

    def setIsReady(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(UserModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addBoolProperty('isCurrentUser', False)
        self._addBoolProperty('isReady', False)
