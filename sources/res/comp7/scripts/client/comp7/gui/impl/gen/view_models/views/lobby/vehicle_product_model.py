# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/vehicle_product_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/vehicle_product_model.py
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class VehicleProductModel(BaseProductModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(VehicleProductModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(9)

    @staticmethod
    def getVehicleInfoType():
        return VehicleModel

    def getCanGoToHangar(self):
        return self._getBool(10)

    def setCanGoToHangar(self, value):
        self._setBool(10, value)

    def _initialize(self):
        super(VehicleProductModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleModel())
        self._addBoolProperty('canGoToHangar', False)
