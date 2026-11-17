# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/wot_plus/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS

# decorador original: @TopScopeTopLayerState.parentOf
class WotPlusInfoState(SFViewLobbyState):
    STATE_ID = 'wotPlusInfo'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(_):
    ...
