# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_confirm_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_confirm_model.py
from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from resource_well.gui.impl.gen.view_models.views.lobby.loading_resource_model import LoadingResourceModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel

class OperationType(IntEnum):
    RETURN = 0
    CONTRIBUTE = 1
    SWITCH = 2


class ResourcesLoadingConfirmModel(ViewModel):
    __slots__ = ('confirm', 'cancel', 'close')

    def __init__(self, properties=5, commands=3):
        super(ResourcesLoadingConfirmModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    def getOperationType(self):
        return OperationType(self._getNumber(1))

    def setOperationType(self, value):
        self._setNumber(1, value.value)

    def getProgressDiff(self):
        return self._getNumber(2)

    def setProgressDiff(self, value):
        self._setNumber(2, value)

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)

    def getResources(self):
        return self._getArray(4)

    def setResources(self, value):
        self._setArray(4, value)

    @staticmethod
    def getResourcesType():
        return LoadingResourceModel

    def _initialize(self):
        super(ResourcesLoadingConfirmModel, self)._initialize()
        self._addViewModelProperty('vehicleCounter', VehicleCounterModel())
        self._addNumberProperty('operationType')
        self._addNumberProperty('progressDiff', 0)
        self._addStringProperty('vehicleName', '')
        self._addArrayProperty('resources', Array())
        self.confirm = self._addCommand('confirm')
        self.cancel = self._addCommand('cancel')
        self.close = self._addCommand('close')
