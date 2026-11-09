# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/upgrades_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/upgrades_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class UpgradesState(Enum):
    ZERO_UPGRADES = 'zeroUpgrades'
    PARTIAL_UPGRADES = 'partialUpgrades'
    FULL_UPGRADES = 'fullUpgrades'


class UpgradesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(UpgradesModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return UpgradesState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)

    def getIsSelected(self):
        return self._getBool(1)

    def setIsSelected(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(UpgradesModel, self)._initialize()
        self._addStringProperty('state')
        self._addBoolProperty('isSelected', False)
