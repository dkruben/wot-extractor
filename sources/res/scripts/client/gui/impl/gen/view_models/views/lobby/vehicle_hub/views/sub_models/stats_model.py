# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/stats_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/stats_model.py
from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_shell_param_model import SpecialShellParamModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.special_vehicle_param_model import SpecialVehicleParamModel

class StatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(StatsModel, self).__init__(properties=properties, commands=commands)

    @property
    def specialMechanic(self):
        return self._getViewModel(0)

    @staticmethod
    def getSpecialMechanicType():
        return VehicleMechanicModel

    def getSpecialMechanicParams(self):
        return self._getArray(1)

    def setSpecialMechanicParams(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSpecialMechanicParamsType():
        return SpecialVehicleParamModel

    def getShellParams(self):
        return self._getMap(2)

    def setShellParams(self, value):
        self._setMap(2, value)

    @staticmethod
    def getShellParamsType():
        return (unicode, SpecialShellParamModel)

    def _initialize(self):
        super(StatsModel, self)._initialize()
        self._addViewModelProperty('specialMechanic', VehicleMechanicModel())
        self._addArrayProperty('specialMechanicParams', Array())
        self._addMapProperty('shellParams', Map(unicode, SpecialShellParamModel))
