# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_plugins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_plugins.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
_FRONTLINE_STATUS_EFFECTS_PRIORITY = (
 BATTLE_MARKER_STATES.STUN_STATE,
 BATTLE_MARKER_STATES.FL_REGENERATION_KIT_STATE,
 BATTLE_MARKER_STATES.REPAIRING_STATE,
 BATTLE_MARKER_STATES.ENGINEER_STATE,
 BATTLE_MARKER_STATES.HEALING_STATE,
 BATTLE_MARKER_STATES.BERSERKER_STATE,
 BATTLE_MARKER_STATES.STEALTH_STATE,
 BATTLE_MARKER_STATES.INSPIRING_STATE,
 BATTLE_MARKER_STATES.DEBUFF_STATE,
 BATTLE_MARKER_STATES.INSPIRED_STATE)

class FrontlineVehicleMarkerPlugin(VehicleMarkerPlugin):

    def _getMarkerStatusPriority(self, markerState):
        try:
            return _FRONTLINE_STATUS_EFFECTS_PRIORITY.index(markerState.statusID)
        except ValueError:
            return -1


class FrontlineRespawnableVehicleMarkerPlugin(FrontlineVehicleMarkerPlugin):

    def start(self):
        super(FrontlineRespawnableVehicleMarkerPlugin, self).start()
        self._isSquadIndicatorEnabled = False

    def _hideVehicleMarker(self, vehicleID):
        self._destroyVehicleMarker(vehicleID)
