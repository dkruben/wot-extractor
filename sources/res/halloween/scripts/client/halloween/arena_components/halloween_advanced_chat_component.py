# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/arena_components/halloween_advanced_chat_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/arena_components/halloween_advanced_chat_component.py
from __future__ import absolute_import
import BigWorld
from arena_components.advanced_chat_component import AdvancedChatComponent
from battleground.location_point_manager import g_locationPointManager
from gui.battle_control import avatar_getter
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES, MarkerType
from halloween_common.halloween_constants import HalloweenMarkerComponentNames
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS

class HWAdvancedChatComponent(AdvancedChatComponent):

    def cleanupBCMarkers(self):
        chatCommands = self.sessionProvider.shared.chatCommands
        arenaDP = self.sessionProvider.getArenaDP()
        if not chatCommands:
            return
        if arenaDP:
            for vInfo in arenaDP.getVehiclesInfoIterator():
                if not arenaDP.isAlly(vInfo.vehicleID) or avatar_getter.getPlayerVehicleID() == vInfo.vehicleID:
                    continue
                chatCommands.sendClearChatCommandsFromTarget(vInfo.vehicleID, MarkerType.VEHICLE_MARKER_TYPE.name)

        self._removeReplyContributionFromPlayer(avatar_getter.getPlayerVehicleID(), MarkerType.INVALID_MARKER_TYPE, -1)
        markedAreas = g_locationPointManager.markedAreas
        removeIDs = markedAreas.keys()
        for targetID in removeIDs:
            markerData = markedAreas[targetID]
            action = _ACTIONS.battleChatCommandFromActionID(markerData.commandID).name
            if action == BATTLE_CHAT_COMMAND_NAMES.GOING_THERE:
                chatCommands.sendCancelReplyChatCommand(targetID, action)
            else:
                self._tryRemovingCommandFromMarker(markerData.commandID, targetID, forceRemove=True)

    def _getActionMarker(self, cmdID, cmdTargetID):
        command = _ACTIONS.battleChatCommandFromActionID(cmdID)
        if command.name in (BATTLE_CHAT_COMMAND_NAMES.MOVE_TO_TARGET_POINT,
         BATTLE_CHAT_COMMAND_NAMES.MOVING_TO_TARGET_POINT):
            entity = BigWorld.entities.get(cmdTargetID)
            if entity and HalloweenMarkerComponentNames.SOULS_COLLECTOR in entity.dynamicComponents:
                return 'eventCollector'
            if entity and HalloweenMarkerComponentNames.CAMP in entity.dynamicComponents:
                return 'eventCamp'
            return None
        return _ACTIONS.battleChatCommandFromActionID(cmdID).vehMarker
