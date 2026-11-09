# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_value_price.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/blueprints/blueprint_value_price.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BlueprintValuePrice(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BlueprintValuePrice, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getString(0)

    def setValue(self, value):
        self._setString(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)

    def getNotEnough(self):
        return self._getBool(3)

    def setNotEnough(self, value):
        self._setBool(3, value)

    def getHasDelimeter(self):
        return self._getBool(4)

    def setHasDelimeter(self, value):
        self._setBool(4, value)

    def getItemCD(self):
        return self._getNumber(5)

    def setItemCD(self, value):
        self._setNumber(5, value)

    def getTooltipId(self):
        return self._getString(6)

    def setTooltipId(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(BlueprintValuePrice, self)._initialize()
        self._addStringProperty('value', '0')
        self._addStringProperty('type', 'custom')
        self._addResourceProperty('icon', R.invalid())
        self._addBoolProperty('notEnough', False)
        self._addBoolProperty('hasDelimeter', False)
        self._addNumberProperty('itemCD', 0)
        self._addStringProperty('tooltipId', '')
