# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/sub_systems/pbh_gamelogic_observer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from gui.battle_control.controllers.prebattle_highlights.sub_systems.base_sub_system import BasePbhSubSystem as BasePbhSubSystem
from helpers import dependency as dependency
from skeletons.gameplay import IGameplayLogic as IGameplayLogic, GameplayStateID as GameplayStateID, PlayerEventID as PlayerEventID
from typing import Optional as Optional
from frameworks_common.state_machine import State as State, StateEvent as StateEvent
_logger: Any

class PbhGameLogicObserver(BasePbhSubSystem, BaseStateObserver):
    __gameplayLogic: Any
    __stateReached: Any
    __prebattlePeriodReached: Any
    def __init__(self, readyCallback):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def isReady(self):
        ...
    def startFlow(self):
        ...
    def stopFlow(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def postPbhEnd(self):
        ...
    def __onArenaPeriodChange(self, period, *args):
        ...
    def __tryCallReadyCallback(self):
        ...
