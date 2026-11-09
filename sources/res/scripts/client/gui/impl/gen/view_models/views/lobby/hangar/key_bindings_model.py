# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/key_bindings_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/key_bindings_model.py
from gui.impl.gen.view_models.views.lobby.common.settings_model import SettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_key_bindings_model import VehicleMenuKeyBindingsModel

class KeyBindingsModel(SettingsModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=1):
        super(KeyBindingsModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleMenu(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleMenuType():
        return VehicleMenuKeyBindingsModel

    def _initialize(self):
        super(KeyBindingsModel, self)._initialize()
        self._addViewModelProperty('vehicleMenu', VehicleMenuKeyBindingsModel())
