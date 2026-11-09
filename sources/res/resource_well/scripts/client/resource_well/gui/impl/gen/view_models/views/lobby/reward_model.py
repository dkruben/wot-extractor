# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/reward_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/reward_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class RewardState(Enum):
    ACTIVE = 'ACTIVE'
    NOT_AVAILABLE = 'NOT_AVAILABLE'
    ALREADY_IN_GARAGE = 'ALREADY_IN_GARAGE'
    ALREADY_RECEIVED = 'ALREADY_RECEIVED'
    SOLD_OUT = 'SOLD_OUT'
    COUNT_NOT_AVAILABLE = 'COUNT_NOT_AVAILABLE'


class RewardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(RewardModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getRewardId(self):
        return self._getString(1)

    def setRewardId(self, value):
        self._setString(1, value)

    def getHasStyle(self):
        return self._getBool(2)

    def setHasStyle(self, value):
        self._setBool(2, value)

    def getVehiclesLeftCount(self):
        return self._getNumber(3)

    def setVehiclesLeftCount(self, value):
        self._setNumber(3, value)

    def getVehiclesLimit(self):
        return self._getNumber(4)

    def setVehiclesLimit(self, value):
        self._setNumber(4, value)

    def getPersonalNumber(self):
        return self._getString(5)

    def setPersonalNumber(self, value):
        self._setString(5, value)

    def getState(self):
        return RewardState(self._getString(6))

    def setState(self, value):
        self._setString(6, value.value)

    def _initialize(self):
        super(RewardModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addStringProperty('rewardId', '')
        self._addBoolProperty('hasStyle', False)
        self._addNumberProperty('vehiclesLeftCount', 0)
        self._addNumberProperty('vehiclesLimit', 0)
        self._addStringProperty('personalNumber', '')
        self._addStringProperty('state')
