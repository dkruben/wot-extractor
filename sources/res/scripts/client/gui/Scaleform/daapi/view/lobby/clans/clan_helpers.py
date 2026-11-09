# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/clan_helpers.py
from __future__ import absolute_import
import typing
from constants import ClansConfig
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getClanQuestURL(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.QUEST_URL)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getCraftMachineURL(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.CRAFT_MACHINE_URL)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getStrongholdEventEnabled(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.STRONGHOLD_EVENT_ENABLED)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getStrongholdEventUrl(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.STRONGHOLD_EVENT_URL)


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getStrongholdEventBattleModeSettings(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.STRONGHOLD_EVENT_BATTLE_MODE, ('',
                                                                                                            0))


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getClanSupplyEnabled(lobbyContext=None):
    return lobbyContext.getServerSettings().getClansConfig().get(ClansConfig.CLAN_SUPPLY_ENABLED, False)
