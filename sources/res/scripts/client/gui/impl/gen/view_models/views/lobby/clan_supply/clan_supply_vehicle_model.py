# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/clan_supply_vehicle_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/clan_supply_vehicle_model.py
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class ClanSupplyVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(ClanSupplyVehicleModel, self).__init__(properties=properties, commands=commands)

    def getFullName(self):
        return self._getString(10)

    def setFullName(self, value):
        self._setString(10, value)

    def _initialize(self):
        super(ClanSupplyVehicleModel, self)._initialize()
        self._addStringProperty('fullName', '')
