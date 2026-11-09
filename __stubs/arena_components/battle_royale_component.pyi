# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/arena_components/battle_royale_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleComponent(ClientArenaComponent):
    __battleRoyaleController: Any
    __sessionProvider: Any
    __place: Any
    __defeatedTeams: Any
    onBattleRoyalePlaceUpdated: Any
    onBattleRoyaleDefeatedTeamsUpdate: Any
    onRespawnTimeFinished: Any
    def __init__(self, componentSystem):
        ...
    def setBattleRoyalePlace(self, place):
        ...
    def setDefeatedTeams(self, defeatedTeams):
        ...
    @property
    def place(self):
        ...
    @property
    def defeatedTeams(self):
        ...
    @property
    def dailyBonusFactor(self):
        ...
