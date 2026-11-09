# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shared/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeTopLayerState as SubScopeTopLayerState

# decorador original: @SubScopeTopLayerState.parentOf
class BrowserLobbyTopState(SFViewLobbyState):
    STATE_ID = 'browser'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, ctx):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _getViewLoadCtx(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
