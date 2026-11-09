# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/bonus_value_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/bonus_value_model.py
from frameworks.wulf import ViewModel

class BonusValueModel(ViewModel):
    __slots__ = ()
    MUL_VALUE = 'mul'

    def __init__(self, properties=4, commands=0):
        super(BonusValueModel, self).__init__(properties=properties, commands=commands)

    def getValueKey(self):
        return self._getString(0)

    def setValueKey(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def getValueType(self):
        return self._getString(2)

    def setValueType(self, value):
        self._setString(2, value)

    def getIsDebuff(self):
        return self._getBool(3)

    def setIsDebuff(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(BonusValueModel, self)._initialize()
        self._addStringProperty('valueKey', '')
        self._addRealProperty('value', 0.0)
        self._addStringProperty('valueType', 'mul')
        self._addBoolProperty('isDebuff', False)
