# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_attacker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/armor_attacker.py
from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_shell_model import ArmorShellModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_vehicle_module import ArmorVehicleModule

class ArmorAttacker(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(ArmorAttacker, self).__init__(properties=properties, commands=commands)

    @property
    def vehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    def getCurrentGun(self):
        return self._getNumber(1)

    def setCurrentGun(self, value):
        self._setNumber(1, value)

    def getCurrentShell(self):
        return self._getNumber(2)

    def setCurrentShell(self, value):
        self._setNumber(2, value)

    def getGuns(self):
        return self._getArray(3)

    def setGuns(self, value):
        self._setArray(3, value)

    @staticmethod
    def getGunsType():
        return ArmorVehicleModule

    def getShells(self):
        return self._getString(4)

    def setShells(self, value):
        self._setString(4, value)

    def getShellDetails(self):
        return self._getMap(5)

    def setShellDetails(self, value):
        self._setMap(5, value)

    @staticmethod
    def getShellDetailsType():
        return (int, ArmorShellModel)

    def _initialize(self):
        super(ArmorAttacker, self)._initialize()
        self._addViewModelProperty('vehicle', VehicleModel())
        self._addNumberProperty('currentGun', 0)
        self._addNumberProperty('currentShell', 0)
        self._addArrayProperty('guns', Array())
        self._addStringProperty('shells', '')
        self._addMapProperty('shellDetails', Map(int, ArmorShellModel))
