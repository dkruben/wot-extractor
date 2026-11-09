# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/battle/battle_page/respawn_ammunition_panel_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/battle/battle_page/respawn_ammunition_panel_view_model.py
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class RespawnAmmunitionPanelViewModel(AmmunitionPanelViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(RespawnAmmunitionPanelViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(7)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def _initialize(self):
        super(RespawnAmmunitionPanelViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
