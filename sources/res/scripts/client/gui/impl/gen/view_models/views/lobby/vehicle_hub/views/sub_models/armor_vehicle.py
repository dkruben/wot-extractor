# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_vehicle.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle_module import ArmorVehicleModule

class ArmorVehicle(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ArmorVehicle, self).__init__(properties=properties, commands=commands)

    def getConfigurationTitle(self):
        return self._getResource(0)

    def setConfigurationTitle(self, value):
        self._setResource(0, value)

    def getCurrentTurret(self):
        return self._getNumber(1)

    def setCurrentTurret(self, value):
        self._setNumber(1, value)

    def getCurrentGun(self):
        return self._getNumber(2)

    def setCurrentGun(self, value):
        self._setNumber(2, value)

    def getTurrets(self):
        return self._getArray(3)

    def setTurrets(self, value):
        self._setArray(3, value)

    @staticmethod
    def getTurretsType():
        return ArmorVehicleModule

    def getGuns(self):
        return self._getArray(4)

    def setGuns(self, value):
        self._setArray(4, value)

    @staticmethod
    def getGunsType():
        return ArmorVehicleModule

    def _initialize(self):
        super(ArmorVehicle, self)._initialize()
        self._addResourceProperty('configurationTitle', R.invalid())
        self._addNumberProperty('currentTurret', 0)
        self._addNumberProperty('currentGun', 0)
        self._addArrayProperty('turrets', Array())
        self._addArrayProperty('guns', Array())
