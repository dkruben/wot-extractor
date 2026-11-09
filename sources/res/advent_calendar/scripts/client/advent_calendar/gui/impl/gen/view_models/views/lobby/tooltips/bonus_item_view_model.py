# wot-extractor: codigo DESCOMPILADO de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/tooltips/bonus_item_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/tooltips/bonus_item_view_model.py
from frameworks.wulf import Array, ViewModel

class BonusItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BonusItemViewModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getArray(1)

    def setValue(self, value):
        self._setArray(1, value)

    @staticmethod
    def getValueType():
        return unicode

    def getIconName(self):
        return self._getString(2)

    def setIconName(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(BonusItemViewModel, self)._initialize()
        self._addStringProperty('type', '')
        self._addArrayProperty('value', Array())
        self._addStringProperty('iconName', '')
