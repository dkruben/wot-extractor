# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/vehicles_daily_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/gen/view_models/views/lobby/widgets/vehicles_daily_model.py
from frameworks.wulf import Map, ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.vehicle_daily_model import VehicleDailyModel

class VehiclesDailyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(VehiclesDailyModel, self).__init__(properties=properties, commands=commands)

    def getDailyVehicles(self):
        return self._getMap(0)

    def setDailyVehicles(self, value):
        self._setMap(0, value)

    @staticmethod
    def getDailyVehiclesType():
        return (unicode, VehicleDailyModel)

    def _initialize(self):
        super(VehiclesDailyModel, self)._initialize()
        self._addMapProperty('dailyVehicles', Map(unicode, VehicleDailyModel))
