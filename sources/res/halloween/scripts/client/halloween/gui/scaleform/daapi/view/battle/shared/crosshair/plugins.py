# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/shared/crosshair/plugins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/shared/crosshair/plugins.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.crosshair.plugins import VehicleStatePlugin
from halloween.gui.battle_control.halloween_battle_constants import VEHICLE_VIEW_STATE

class HWVehicleStatePlugin(VehicleStatePlugin):

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.HW_MAX_HEALTH:
            self._setMaxHealth(value)
        super(HWVehicleStatePlugin, self)._onVehicleStateUpdated(state, value)
