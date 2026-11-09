# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/summary/statistic_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/summary/statistic_item_model.py
from frameworks.wulf import ViewModel

class StatisticItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StatisticItemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getMainValue(self):
        return self._getString(1)

    def setMainValue(self, value):
        self._setString(1, value)

    def getAdditionalValue(self):
        return self._getString(2)

    def setAdditionalValue(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(StatisticItemModel, self)._initialize()
        self._addStringProperty('type', 'battles')
        self._addStringProperty('mainValue', '')
        self._addStringProperty('additionalValue', '')
