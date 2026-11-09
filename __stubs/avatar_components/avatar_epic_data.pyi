# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/avatar_epic_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import Event as Event
import constants as constants
from ReservesEvents import randomReservesEvents as randomReservesEvents
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME, _MISSION_SECTOR_ID_MAPPING as _MISSION_SECTOR_ID_MAPPING
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from constants import DEATH_ZONES as DEATH_ZONES, SECTOR_STATE as SECTOR_STATE, VEHICLE_HIT_FLAGS as VHF
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
_logger: Any
_KB_MAPPING: dict
_COMMAND_TO_LANE_MAPPING: dict
_ATTACKER_POSTFIX = '_ATK'
_DEFENDER_POSTFIX = '_DEF'

class AvatarEpicData(object):
    __lastPlayerSectorGroupID: Any
    __isCurrentPlayerSectorGroupAllowed: Any
    __lastTimerTypeForSectorGroup: Any
    __playerUnderFire: Any
    __frontLineDevInfoEnabled: Any
    __devEvtManager: Any
    onFrontLineInfoUpdated: Any
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def onRandomReserveOffer(self, offer, level, slotIdx):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomeNonPlayer(self):
        ...
    def showDestructibleShotResults(self, destructibleEntityID, hitFlagsList):
        ...
    def onDestructibleDestroyed(self, destructibleEntityID, shooterID):
        ...
    def welcomeToSector(self, sectorID, groupID, groupState, goodGroup, actionTime, actionDuration):
        ...
    def onStepRepairPointAction(self, repairPointIndex, action, nextActionTime, pointsHealed):
        ...
    def onSectorBaseAction(self, sectorBaseID, action, nextActionTime):
        ...
    def enteringProtectionZone(self, zoneID):
        ...
    def leavingProtectionZone(self, zoneID):
        ...
    def protectionZoneShooting(self, zoneID):
        ...
    def onXPUpdated(self, xpValue):
        ...
    def onCrewRoleFactorAndRankUpdate(self, newFactor, allyVehID, allyNewRank):
        ...
    def syncPurchasedAbilities(self, purchasedAbilities):
        ...
    def onRankUpdate(self, newRank):
        ...
    def enableFrontLineDevInfo(self, enable):
        ...
    def toggleFrontLineDevInfo(self):
        ...
    def onSectorShooting(self, sectorID):
        ...
    def frontLineInformationUpdate(self, params):
        ...
    def __sendGlobalChatCmdIfPossible(self, key):
        ...
    def __playSound(self, eventName):
        ...
