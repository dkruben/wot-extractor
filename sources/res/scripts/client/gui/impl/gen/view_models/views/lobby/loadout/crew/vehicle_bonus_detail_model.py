# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/vehicle_bonus_detail_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/vehicle_bonus_detail_model.py
from frameworks.wulf import ViewModel

class VehicleBonusDetailModel(ViewModel):
    __slots__ = ()
    COMMANDER = 'commander'
    BROTHERHOOD = 'brotherhood'

    def __init__(self, properties=3, commands=0):
        super(VehicleBonusDetailModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)

    def getBonus(self):
        return self._getReal(2)

    def setBonus(self, value):
        self._setReal(2, value)

    def _initialize(self):
        super(VehicleBonusDetailModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('type', '')
        self._addRealProperty('bonus', 0.0)
