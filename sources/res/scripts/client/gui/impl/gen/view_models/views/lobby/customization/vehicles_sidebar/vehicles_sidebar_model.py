# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/customization/vehicles_sidebar/vehicles_sidebar_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/customization/vehicles_sidebar/vehicles_sidebar_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.customization.vehicles_sidebar.vehicles_sidebar_item_model import VehiclesSidebarItemModel

class VehiclesSidebarModel(ViewModel):
    __slots__ = ('onClose', )

    def __init__(self, properties=1, commands=1):
        super(VehiclesSidebarModel, self).__init__(properties=properties, commands=commands)

    def getVehiclesSelection(self):
        return self._getArray(0)

    def setVehiclesSelection(self, value):
        self._setArray(0, value)

    @staticmethod
    def getVehiclesSelectionType():
        return VehiclesSidebarItemModel

    def _initialize(self):
        super(VehiclesSidebarModel, self)._initialize()
        self._addArrayProperty('vehiclesSelection', Array())
        self.onClose = self._addCommand('onClose')
