# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crystals_promo/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.impl.gen import R as R
from gui.impl.lobby.crystals_promo.crystals_promo_view import CrystalsPromoView as CrystalsPromoView

# decorador original: @TopScopeTopLayerState.parentOf
class CrystalsPromoState(GuiImplViewLobbyState):
    STATE_ID = 'crystalsPromo'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
