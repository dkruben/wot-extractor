# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/resources_loading_view_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from resource_well.gui.impl.gen.view_models.views.lobby.resources_tab_model import ResourcesTabModel
from resource_well.gui.impl.gen.view_models.views.lobby.vehicle_counter_model import VehicleCounterModel

class ProgressionState(Enum):
    ACTIVE = 'active'
    NOPROGRESS = 'noProgress'
    NOVEHICLES = 'noVehicles'


class ResourcesLoadingViewModel(ViewModel):
    __slots__ = ('showHangar', 'close', 'loadResources')

    def __init__(self, properties=7, commands=3):
        super(ResourcesLoadingViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleCounter(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleCounterType():
        return VehicleCounterModel

    @property
    def vehicleInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getProgressionState(self):
        return ProgressionState(self._getString(2))

    def setProgressionState(self, value):
        self._setString(2, value.value)

    def getProgression(self):
        return self._getNumber(3)

    def setProgression(self, value):
        self._setNumber(3, value)

    def getResourcesTabs(self):
        return self._getArray(4)

    def setResourcesTabs(self, value):
        self._setArray(4, value)

    @staticmethod
    def getResourcesTabsType():
        return ResourcesTabModel

    def getIsLoadingError(self):
        return self._getBool(5)

    def setIsLoadingError(self, value):
        self._setBool(5, value)

    def getShowBlur(self):
        return self._getBool(6)

    def setShowBlur(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(ResourcesLoadingViewModel, self)._initialize()
        self._addViewModelProperty('vehicleCounter', VehicleCounterModel())
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addStringProperty('progressionState')
        self._addNumberProperty('progression', 0)
        self._addArrayProperty('resourcesTabs', Array())
        self._addBoolProperty('isLoadingError', False)
        self._addBoolProperty('showBlur', False)
        self.showHangar = self._addCommand('showHangar')
        self.close = self._addCommand('close')
        self.loadResources = self._addCommand('loadResources')
