# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/vehicle_bonus.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/loadout/crew/vehicle_bonus.py
from frameworks.wulf import ViewModel

class VehicleBonus(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(VehicleBonus, self).__init__(properties=properties, commands=commands)

    def getEquipment(self):
        return self._getReal(0)

    def setEquipment(self, value):
        self._setReal(0, value)

    def getBrotherhood(self):
        return self._getReal(1)

    def setBrotherhood(self, value):
        self._setReal(1, value)

    def getOptDevices(self):
        return self._getReal(2)

    def setOptDevices(self, value):
        self._setReal(2, value)

    def getCommander(self):
        return self._getReal(3)

    def setCommander(self, value):
        self._setReal(3, value)

    def getBattleBooster(self):
        return self._getReal(4)

    def setBattleBooster(self, value):
        self._setReal(4, value)

    def _initialize(self):
        super(VehicleBonus, self)._initialize()
        self._addRealProperty('equipment', 0.0)
        self._addRealProperty('brotherhood', 0.0)
        self._addRealProperty('optDevices', 0.0)
        self._addRealProperty('commander', 0.0)
        self._addRealProperty('battleBooster', 0.0)
