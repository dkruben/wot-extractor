# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/damage_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/damage_panel.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel, _STATE_HANDLERS
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class HalloweenDamagePanel(DamagePanel):

    def __init__(self):
        super(HalloweenDamagePanel, self).__init__()
        _STATE_HANDLERS[VEHICLE_VIEW_STATE.HW_DRAIN_LIFE] = _STATE_HANDLERS[VEHICLE_VIEW_STATE.FIRE]
        self._prevFireStateValue = False
        self.__prevDrainStateValue = False

    def _onVehicleStateUpdated(self, state, value):
        if state == VEHICLE_VIEW_STATE.FIRE:
            self._prevFireStateValue = value
        elif state == VEHICLE_VIEW_STATE.HW_DRAIN_LIFE:
            if not (value or self._prevFireStateValue or self.__prevDrainStateValue):
                return
            self.__prevDrainStateValue = value
            if self._prevFireStateValue and not value:
                return
        super(HalloweenDamagePanel, self)._onVehicleStateUpdated(state, value)
