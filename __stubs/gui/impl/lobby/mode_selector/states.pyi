# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.mode_selector.battle_session_view import BattleSessionView as BattleSessionView
from gui.impl.lobby.mode_selector.mode_selector_view import ModeSelectorView as ModeSelectorView
from gui.lobby_state_machine.states import SubScopeTopLayerState as SubScopeTopLayerState, GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyState as LobbyState, LobbyStateFlags as LobbyStateFlags, LobbyStateDescription as LobbyStateDescription
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher

# decorador original: @SubScopeTopLayerState.parentOf
class ModeSelectorState(LobbyState):
    STATE_ID = 'modeSelector'
    @classmethod
    def goTo(cls, provider=None, subSelectorCallback=None):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @ModeSelectorState.parentOf
class EntryState(GuiImplViewLobbyState):
    STATE_ID = 'entry'
    VIEW_KEY: Any
    __isNavigationVisible: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @ModeSelectorState.parentOf
class BattleSessionState(GuiImplViewLobbyState):
    STATE_ID = 'battleSession'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
