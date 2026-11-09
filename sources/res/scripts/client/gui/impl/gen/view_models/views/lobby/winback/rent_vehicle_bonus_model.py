# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/rent_vehicle_bonus_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/winback/rent_vehicle_bonus_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.winback.vehicle_bonus_model import VehicleBonusModel

class RentType(Enum):
    TIME = 'time'
    WINS = 'wins'
    BATTLES = 'battles'


class RentVehicleBonusModel(VehicleBonusModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(RentVehicleBonusModel, self).__init__(properties=properties, commands=commands)

    def getRentType(self):
        return RentType(self._getString(19))

    def setRentType(self, value):
        self._setString(19, value.value)

    def getRentDuration(self):
        return self._getNumber(20)

    def setRentDuration(self, value):
        self._setNumber(20, value)

    def _initialize(self):
        super(RentVehicleBonusModel, self)._initialize()
        self._addStringProperty('rentType')
        self._addNumberProperty('rentDuration', 0)
