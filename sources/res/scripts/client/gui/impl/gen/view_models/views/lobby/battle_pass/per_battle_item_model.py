# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/per_battle_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/per_battle_item_model.py
from frameworks.wulf import ViewModel

class PerBattleItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PerBattleItemModel, self).__init__(properties=properties, commands=commands)

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)

    def getWinPoint(self):
        return self._getNumber(1)

    def setWinPoint(self, value):
        self._setNumber(1, value)

    def getLosePoint(self):
        return self._getNumber(2)

    def setLosePoint(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PerBattleItemModel, self)._initialize()
        self._addStringProperty('label', '')
        self._addNumberProperty('winPoint', 0)
        self._addNumberProperty('losePoint', 0)
