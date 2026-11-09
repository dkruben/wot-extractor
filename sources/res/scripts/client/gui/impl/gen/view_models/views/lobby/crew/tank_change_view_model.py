# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tank_change_view_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.tank_change_vehicle_model import TankChangeVehicleModel

class TankChangeViewModel(BaseCrewViewModel):
    __slots__ = ('onVehicleSelected', 'onResetFilters')

    def __init__(self, properties=4, commands=6):
        super(TankChangeViewModel, self).__init__(properties=properties, commands=commands)

    def getNation(self):
        return self._getString(2)

    def setNation(self, value):
        self._setString(2, value)

    def getVehicleList(self):
        return self._getArray(3)

    def setVehicleList(self, value):
        self._setArray(3, value)

    @staticmethod
    def getVehicleListType():
        return TankChangeVehicleModel

    def _initialize(self):
        super(TankChangeViewModel, self)._initialize()
        self._addStringProperty('nation', '')
        self._addArrayProperty('vehicleList', Array())
        self.onVehicleSelected = self._addCommand('onVehicleSelected')
        self.onResetFilters = self._addCommand('onResetFilters')
