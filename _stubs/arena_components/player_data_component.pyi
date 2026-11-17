# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/arena_components/player_data_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import Event as Event
import player_ranks as player_ranks
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from gui.battle_control import avatar_getter as avatar_getter
from constants import ARENA_SYNC_OBJECTS as ARENA_SYNC_OBJECTS, PLAYER_RANK as PLAYER_RANK

class PlayerDataComponent(ClientArenaComponent):
    playerGroups: Any
    playerRank: Any
    playerGroupsEnabled: Any
    __playerGroupsEnabled: Any
    onPlayerGroupsUpdated: Any
    __playerIngameRanksEnabled: Any
    __playerRank: Any
    onCrewRolesFactorUpdated: Any
    onPlayerRankUpdated: Any
    def __init__(self, componentSystem):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def playerIngameRanksEnabled(self):
        ...
    def getTresholdForRanks(self):
        ...
    def getPlayerGroupForVehicle(self, vId):
        ...
    def getPlayerGroupForPlayer(self):
        ...
    def _vehiclePlayerGroupsUpdated(self, args):
        ...
    def __getPlayerGroups(self):
        ...
    def __getPlayerRank(self):
        ...
    def __onTeamRanksUpdated(self, args):
        ...
