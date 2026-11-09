# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/TargetDesignatorTargetController.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/TargetDesignatorTargetController.py
from __future__ import absolute_import
import typing
from functools import partial
from PlayerEvents import g_playerEvents
from constants import DIRECT_DETECTION_TYPE
from gui.battle_control.avatar_getter import isFPV, getVehicleIDAttached
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID, VEHICLE_VIEW_STATE
from gui.shared import EVENT_BUS_SCOPE, events, g_eventBus
from helpers.dependency import descriptor
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.components.vehicle_component import VehicleDynamicComponent
if typing.TYPE_CHECKING:
    from gui.Scaleform.daapi.view.battle.shared.markers2d import MarkersManager
    from gui.Scaleform.daapi.view.battle.shared.markers2d.vehicle_plugins import VehicleMarkerPlugin

class TargetDesignatorTargetController(VehicleDynamicComponent):
    session = descriptor(IBattleSessionProvider)

    def __init__(self):
        super(TargetDesignatorTargetController, self).__init__()
        g_eventBus.addListener(events.MarkersManagerEvent.MARKERS_CREATED, self.__onMarkersManagerMarkersCreated, EVENT_BUS_SCOPE.BATTLE)
        self.session.shared.vehicleState.onVehicleControlling += self.__onVehicleControlling
        self.isFPV = partial(isFPV, self.entity.id)
        self._initComponent()

    def __onMarkersManagerMarkersCreated(self, event):
        g_eventBus.removeListener(events.MarkersManagerEvent.MARKERS_CREATED, self.__onMarkersManagerMarkersCreated, EVENT_BUS_SCOPE.BATTLE)
        if not self.isAppearanceReady():
            return
        manager = event.getMarkersManager()
        plugin = manager.getPlugin('vehicles')
        vehID = self.entity.id
        handle = plugin.getVehicleMarkerID(vehID)
        plugin.updateTargetDesignatorSpottedMarkerTimer(vehID, handle, self)

    def onDestroy(self):
        g_eventBus.removeListener(events.MarkersManagerEvent.MARKERS_CREATED, self.__onMarkersManagerMarkersCreated, EVENT_BUS_SCOPE.BATTLE)
        self.session.shared.vehicleState.onVehicleControlling -= self.__onVehicleControlling
        super(TargetDesignatorTargetController, self).onDestroy()

    def set_spottedMarker(self, _):
        self._updateComponentAppearance()

    def set_hasUnspottedIndicator(self, _):
        if self.entity.id != getVehicleIDAttached():
            return
        g_playerEvents.onObservedByEnemy(DIRECT_DETECTION_TYPE.UNSPOTTED, bool(self.hasUnspottedIndicator))

    def _onComponentAppearanceUpdate(self, **kwargs):
        super(TargetDesignatorTargetController, self)._onComponentAppearanceUpdate(**kwargs)
        self.__update()

    def __onVehicleControlling(self, _):
        self._updateComponentAppearance()

    def __update(self):
        vehID = self.entity.id
        self.session.shared.feedback.onVehicleFeedbackReceived(FEEDBACK_EVENT_ID.TARGET_DESIGNATOR_SPOTTED_MARKER, vehID, self)
        self.session.invalidateVehicleState(VEHICLE_VIEW_STATE.TARGET_DESIGNATOR, self, vehID)
