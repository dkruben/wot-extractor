# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_params_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_params_view_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import VehicleParamGroupViewModel

class VehicleParamsViewModel(ViewModel):
    __slots__ = ('onGroupClick', )

    def __init__(self, properties=1, commands=1):
        super(VehicleParamsViewModel, self).__init__(properties=properties, commands=commands)

    def getGroups(self):
        return self._getArray(0)

    def setGroups(self, value):
        self._setArray(0, value)

    @staticmethod
    def getGroupsType():
        return VehicleParamGroupViewModel

    def _initialize(self):
        super(VehicleParamsViewModel, self)._initialize()
        self._addArrayProperty('groups', Array())
        self.onGroupClick = self._addCommand('onGroupClick')
