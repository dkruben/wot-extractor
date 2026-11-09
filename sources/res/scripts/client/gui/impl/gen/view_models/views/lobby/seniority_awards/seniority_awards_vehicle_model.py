# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_awards_vehicle_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_awards_vehicle_model.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class SeniorityAwardsVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(SeniorityAwardsVehicleModel, self).__init__(properties=properties, commands=commands)

    def getDescription(self):
        return self._getString(10)

    def setDescription(self, value):
        self._setString(10, value)

    def getVehicleId(self):
        return self._getString(11)

    def setVehicleId(self, value):
        self._setString(11, value)

    def _initialize(self):
        super(SeniorityAwardsVehicleModel, self)._initialize()
        self._addStringProperty('description', '')
        self._addStringProperty('vehicleId', '')
