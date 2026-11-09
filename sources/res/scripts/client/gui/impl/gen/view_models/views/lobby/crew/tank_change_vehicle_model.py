# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_vehicle_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_vehicle_model.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class TankChangeVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(TankChangeVehicleModel, self).__init__(properties=properties, commands=commands)

    def getIsInInventory(self):
        return self._getBool(10)

    def setIsInInventory(self, value):
        self._setBool(10, value)

    def getIsElite(self):
        return self._getBool(11)

    def setIsElite(self, value):
        self._setBool(11, value)

    def getIsSelected(self):
        return self._getBool(12)

    def setIsSelected(self, value):
        self._setBool(12, value)

    def getIsTrainingAvailable(self):
        return self._getBool(13)

    def setIsTrainingAvailable(self, value):
        self._setBool(13, value)

    def getIsWotPlusVehicle(self):
        return self._getBool(14)

    def setIsWotPlusVehicle(self, value):
        self._setBool(14, value)

    def _initialize(self):
        super(TankChangeVehicleModel, self)._initialize()
        self._addBoolProperty('isInInventory', False)
        self._addBoolProperty('isElite', False)
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isTrainingAvailable', False)
        self._addBoolProperty('isWotPlusVehicle', False)
