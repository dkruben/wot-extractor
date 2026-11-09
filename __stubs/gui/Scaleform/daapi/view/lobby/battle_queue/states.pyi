# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/battle_queue/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui import SystemMessages as SystemMessages
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, LobbyStateFlags as LobbyStateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from helpers.time_utils import getCurrentTimestamp as getCurrentTimestamp
_logger: Any

# decorador original: @SubScopeSubLayerState.parentOf
class BattleQueueContainerState(LobbyState):
    STATE_ID = 'battleQueue'
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def __preventTransitionCheck(self, event, state=None):
        ...

# decorador original: @BattleQueueContainerState.parentOf
class InitialQueueState(LobbyState):
    STATE_ID = 'initial'
    def _onEntered(self, event):
        ...

# decorador original: @BattleQueueContainerState.parentOf
class CommonBattleQueueState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.BATTLE_QUEUE
    VIEW_KEY: Any
    __createTime: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @BattleQueueContainerState.parentOf
class StrongholdsBattleQueueState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.BATTLE_STRONGHOLDS_QUEUE
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(_):
    ...
