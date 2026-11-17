# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, UntrackedState as UntrackedState, LobbyStateFlags as LobbyStateFlags
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS

# decorador original: @SubScopeSubLayerState.parentOf
class ShopState(SFViewLobbyState):
    STATE_ID = 'shop'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def registerTransitions(self):
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
def registerTransitions(_):
    ...
