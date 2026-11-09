# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/completed_progression_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/gui/impl/gen/view_models/views/lobby/completed_progression_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class CompletedProgressionViewModel(ViewModel):
    __slots__ = ('onViewLoaded', 'onClose', 'onShowVehicle', 'onAboutClick')

    def __init__(self, properties=3, commands=4):
        super(CompletedProgressionViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getHasStyle(self):
        return self._getBool(1)

    def setHasStyle(self, value):
        self._setBool(1, value)

    def getPersonalNumber(self):
        return self._getString(2)

    def setPersonalNumber(self, value):
        self._setString(2, value)

    def _initialize(self):
        super(CompletedProgressionViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addBoolProperty('hasStyle', False)
        self._addStringProperty('personalNumber', '')
        self.onViewLoaded = self._addCommand('onViewLoaded')
        self.onClose = self._addCommand('onClose')
        self.onShowVehicle = self._addCommand('onShowVehicle')
        self.onAboutClick = self._addCommand('onAboutClick')
