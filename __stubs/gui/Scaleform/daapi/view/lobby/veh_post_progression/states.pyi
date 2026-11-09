# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import BECOME_ELITE_VEHICLES_WATCHED as BECOME_ELITE_VEHICLES_WATCHED
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.veh_post_progression.post_progression_intro import getPostProgressionInfoWindowProc as getPostProgressionInfoWindowProc
from gui.lobby_state_machine.states import ViewLobbyState as ViewLobbyState, LobbyStateDescription as LobbyStateDescription, SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState

# decorador original: @SubScopeSubLayerState.parentOf
class VehiclePostProgressionState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEH_POST_PROGRESSION
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class VehiclePostProgressionCmpState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEH_POST_PROGRESSION_CMP
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
