# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/widget/bonus_model.py
from frameworks.wulf import ViewModel

class BonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)

    def getIndex(self):
        return self._getNumber(0)

    def setIndex(self, value):
        self._setNumber(0, value)

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def getTooltipContentId(self):
        return self._getString(4)

    def setTooltipContentId(self, value):
        self._setString(4, value)

    def getProbability(self):
        return self._getNumber(5)

    def setProbability(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addNumberProperty('index', 0)
        self._addStringProperty('name', '')
        self._addStringProperty('value', '')
        self._addStringProperty('tooltipId', '')
        self._addStringProperty('tooltipContentId', '')
        self._addNumberProperty('probability', 0)
