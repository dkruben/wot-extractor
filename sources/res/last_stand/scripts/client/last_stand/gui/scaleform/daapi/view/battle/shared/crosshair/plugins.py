# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/shared/crosshair/plugins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/shared/crosshair/plugins.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.crosshair.plugins import VehicleStatePlugin
from last_stand.gui.battle_control.ls_battle_constants import VEHICLE_VIEW_STATE

class LSVehicleStatePlugin(VehicleStatePlugin):

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.LS_MAX_HEALTH:
            self._setMaxHealth(value)
        super(LSVehicleStatePlugin, self)._onVehicleStateUpdated(state, value)
