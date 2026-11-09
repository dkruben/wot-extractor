# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_param_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_param_view_model.py
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import VehicleParamBaseViewModel

class VehicleParamViewModel(VehicleParamBaseViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(VehicleParamViewModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(5)

    def setName(self, value):
        self._setString(5, value)

    def getParentID(self):
        return self._getString(6)

    def setParentID(self, value):
        self._setString(6, value)

    def _initialize(self):
        super(VehicleParamViewModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('parentID', '')
