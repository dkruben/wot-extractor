# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/vehicle_counter_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/vehicle_counter_model.py
from frameworks.wulf import ViewModel

class VehicleCounterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleCounterModel, self).__init__(properties=properties, commands=commands)

    def getIsVehicleCountAvailable(self):
        return self._getBool(0)

    def setIsVehicleCountAvailable(self, value):
        self._setBool(0, value)

    def getVehicleCount(self):
        return self._getNumber(1)

    def setVehicleCount(self, value):
        self._setNumber(1, value)

    def getIsSerial(self):
        return self._getBool(2)

    def setIsSerial(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(VehicleCounterModel, self)._initialize()
        self._addBoolProperty('isVehicleCountAvailable', True)
        self._addNumberProperty('vehicleCount', 0)
        self._addBoolProperty('isSerial', False)
