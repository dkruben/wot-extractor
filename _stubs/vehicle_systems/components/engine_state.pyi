# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_systems/components/engine_state.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from random import uniform as uniform
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD
from helpers import dependency as dependency
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, GameplayStateID as GameplayStateID
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_StateConvertor: dict
_ENGINE_START_STATE_IDS: tuple

class EngineState(object):
    NORMAL = 0
    REPAIRED = 1
    CRITICAL = 2
    DESTROYED = 3

class EngineLoad(object):
    _STOPPED = 0
    _IDLE = 1
    _MEDIUM = 2
    _HIGH = 3

def getEngineStateFromName(stateName):
    ...
def checkEngineStart(detailedEngineState, period):
    ...
def notifyEngineOnArenaPeriodChange(detailedEngineState, period):
    ...
def _delayEngineStart(detailedEngineState, _=None, __=None):
    ...
def _getTimeToBattleStart(arena):
    ...
