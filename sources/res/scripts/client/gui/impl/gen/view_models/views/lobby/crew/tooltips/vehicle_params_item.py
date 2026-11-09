# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_item.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/vehicle_params_item.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ValueStyleEnum(Enum):
    GREENBRIGHT = 'greenBright'
    RED = 'red'
    WHITEORANGE = 'whiteOrange'
    YELLOW = 'yellow'
    WHITESPANISH = 'whiteSpanish'


class VehicleParamsItem(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleParamsItem, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)

    def getAsteriskIcon(self):
        return self._getResource(4)

    def setAsteriskIcon(self, value):
        self._setResource(4, value)

    def _initialize(self):
        super(VehicleParamsItem, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('value', '')
        self._addResourceProperty('icon', R.invalid())
        self._addBoolProperty('isEnabled', True)
        self._addResourceProperty('asteriskIcon', R.invalid())
