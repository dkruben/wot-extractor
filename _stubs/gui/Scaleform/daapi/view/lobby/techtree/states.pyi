# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.techtree.settings import SelectedNation as SelectedNation
from gui.Scaleform.daapi.view.lobby.vehicle_compare.states import VehicleCompareState as VehicleCompareState
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.lobby_state_machine.states import LobbyState as LobbyState, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription
from gui.impl import backport as backport
from gui.impl.gen import R as R

# decorador original: @SubScopeSubLayerState.parentOf
class TechtreeState(SFViewLobbyState):
    STATE_ID = VIEW_ALIAS.LOBBY_TECHTREE
    VIEW_KEY: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _targetsTechtreeState(self, event):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def serializeParams(self):
        ...

# decorador original: @TechtreeState.parentOf
class DefaultTechtreeState(LobbyState):
    STATE_ID = 'default'
    def registerTransitions(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
