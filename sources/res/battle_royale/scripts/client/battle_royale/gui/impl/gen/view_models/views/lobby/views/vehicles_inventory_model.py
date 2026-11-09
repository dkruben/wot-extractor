# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/vehicles_inventory_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/vehicles_inventory_model.py
from frameworks.wulf import Map, ViewModel

class VehiclesInventoryModel(ViewModel):
    __slots__ = ('onSelect', )
    NO_VEHICLE_ID = -1

    def __init__(self, properties=3, commands=1):
        super(VehiclesInventoryModel, self).__init__(properties=properties, commands=commands)

    def getCurrentVehicleIntCD(self):
        return self._getNumber(0)

    def setCurrentVehicleIntCD(self, value):
        self._setNumber(0, value)

    def getCurrentVehicleInventoryId(self):
        return self._getNumber(1)

    def setCurrentVehicleInventoryId(self, value):
        self._setNumber(1, value)

    def getVehicles(self):
        return self._getMap(2)

    def setVehicles(self, value):
        self._setMap(2, value)

    @staticmethod
    def getVehiclesType():
        return (unicode, unicode)

    def _initialize(self):
        super(VehiclesInventoryModel, self)._initialize()
        self._addNumberProperty('currentVehicleIntCD', -1)
        self._addNumberProperty('currentVehicleInventoryId', -1)
        self._addMapProperty('vehicles', Map(unicode, unicode))
        self.onSelect = self._addCommand('onSelect')
