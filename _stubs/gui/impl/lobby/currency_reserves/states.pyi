# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/currency_reserves/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeTopLayerState as SubScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.impl.gen import R as R
from gui.impl.lobby.currency_reserves.currency_reserves_view import CurrencyReservesView as CurrencyReservesView

# decorador original: @SubScopeTopLayerState.parentOf
class CurrencyReservesState(GuiImplViewLobbyState):
    STATE_ID = 'currencyReserves'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
