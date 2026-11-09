# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_statistics_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_statistics_model.py
from frameworks.wulf import Map, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_statistic_model import VehicleStatisticModel

class VehicleStatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(VehicleStatisticsModel, self).__init__(properties=properties, commands=commands)

    def getStatistics(self):
        return self._getMap(0)

    def setStatistics(self, value):
        self._setMap(0, value)

    @staticmethod
    def getStatisticsType():
        return (unicode, VehicleStatisticModel)

    def _initialize(self):
        super(VehicleStatisticsModel, self)._initialize()
        self._addMapProperty('statistics', Map(unicode, VehicleStatisticModel))
