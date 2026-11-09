# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/helpers/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/helpers/utils.py
from __future__ import absolute_import
import logging, BigWorld, typing
from helpers import dependency
from fort_rush.skeletons.battle_controller import IFortRushBattleController
from fort_rush_common.component_helpers import getVehicleRespawnComponent
from constants import IS_CLIENT
if typing.TYPE_CHECKING:
    from typing import Optional
    from RespawnFrameworkVehicleComponent import RespawnFrameworkVehicleComponent
_logger = logging.getLogger(__name__)
if IS_CLIENT:
    from gui.battle_control import avatar_getter
else:
    avatar_getter = None

def getCurrentTeam(guiSessionProvider=None):
    if guiSessionProvider is not None:
        arenaDP = guiSessionProvider.getArenaDP()
        if arenaDP is not None:
            return arenaDP.getNumberOfTeam()
    playerTeam = avatar_getter.getPlayerTeam()
    if playerTeam is None:
        playerTeam = avatar_getter.getObserverTeam()
    return playerTeam


def mapOwnerTeamToMarkerTeam(ownerTeam, playerTeam):
    if not ownerTeam:
        return 0
    else:
        if playerTeam is None:
            return 0
        if ownerTeam == playerTeam:
            return 1
        return 2


def retrievePlayerRespawnComponent():
    vehicle = BigWorld.entities.get(avatar_getter.getPlayerVehicleID())
    if vehicle is None:
        _logger.warning('[FORT_RUSH][RESPAWN] retrievePlayerRespawnComponent: playerVehicle is None')
        return
    else:
        respawnComponent = getVehicleRespawnComponent(vehicle)
        if respawnComponent is None:
            _logger.warning('[FORT_RUSH][RESPAWN] retrievePlayerRespawnComponent: respawnComponent is None for vehicle %s', vehicle.id)
            return
        return respawnComponent


@dependency.replace_none_kwargs(ctrl=IFortRushBattleController)
def isFREventProgressionQuest(questId, ctrl=None):
    if questId is None:
        return False
    else:
        return questId.startswith(ctrl.getConfig().progressionQuestPrefix)
