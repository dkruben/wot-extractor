# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/players_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from sys import maxsize as maxsize
import BigWorld as BigWorld
from battle_royale.gui.Scaleform.daapi.view.battle.respawn_message_panel import RESPAWNING_TIMER_DELAY as RESPAWNING_TIMER_DELAY
from battle_royale.gui.Scaleform.daapi.view.battle.shared.utils import getVehicleLevel as getVehicleLevel
from battle_royale.gui.battle_control.controllers.spawn_ctrl import ISpawnListener as ISpawnListener
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi.view.meta.BattleRoyaleTeamPanelMeta import BattleRoyaleTeamPanelMeta as BattleRoyaleTeamPanelMeta
from gui.battle_control.arena_info import vos_collections as vos_collections
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController as IArenaVehiclesController
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener as IBattleFieldListener
from gui.clans.formatters import getClanAbbrevString as getClanAbbrevString
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import getTypeVPanelIconPath as getTypeVPanelIconPath
from helpers import dependency as dependency, int2roman as int2roman
from items.battle_royale import isSpawnedBot as isSpawnedBot
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO as VehicleArenaInfoVO
_logger: Any

class PlayersPanel(IBattleFieldListener, IArenaVehiclesController, ISpawnListener, BattleRoyaleTeamPanelMeta):
    __slots__: tuple
    __sessionProvider: Any
    _HEALTH_PERCENT = 100
    __vehicleIDs: Any
    __selectedByVehicleIds: Any
    __spawnPointsViewActive: Any
    __isRespawning: Any
    __respawningDelayCallbackID: Any
    def __init__(self):
        ...
    @property
    def selfVehicleIndex(self):
        ...
    def showSpawnPoints(self):
        ...
    def closeSpawnPoints(self):
        ...
    def updatePoint(self, vehicleId, pointId, prevPointId):
        ...
    def updateVehiclesStats(self, updated, arenaDP):
        ...
    def updateVehiclesInfo(self, updated, arenaDP):
        ...
    def invalidateVehicleStatus(self, _, vInfoVO, __):
        ...
    def __clearDelayCallback(self):
        ...
    def updateTeammateRespawnTime(self, timeLeft):
        ...
    def updateRespawnTime(self, timeLeft, selfVehicle=True):
        ...
    def updateRespawningStatus(self, timeLeft, selfVehicle):
        ...
    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onPlayerTeamChanged(self, _):
        ...
    def __init(self):
        ...
    def __initSquadPlayers(self):
        ...
    def __initSquadState(self):
        ...
    def __updateSquadStatus(self):
        ...
    def __updateVehicleStatus(self, vInfoVO):
        ...
    def __isVehOpacityMax(self, vInfoVO):
        ...
    @staticmethod
    def __getFrags(frags):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
