# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicles_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicles_info_model.py
from frameworks.wulf import Map, ViewModel

class VehiclesInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(VehiclesInfoModel, self).__init__(properties=properties, commands=commands)

    def getVehicles(self):
        return self._getMap(0)

    def setVehicles(self, value):
        self._setMap(0, value)

    @staticmethod
    def getVehiclesType():
        return (unicode, unicode)

    def _initialize(self):
        super(VehiclesInfoModel, self)._initialize()
        self._addMapProperty('vehicles', Map(unicode, unicode))
