# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/clan_supply/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.gen import R as R
from gui.impl.lobby.clan_supply.main_view import MainView as MainView
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, GuiImplViewLobbyState as GuiImplViewLobbyState

# decorador original: @SubScopeSubLayerState.parentOf
class ClanSupplyState(GuiImplViewLobbyState):
    STATE_ID = 'clanSupply'
    VIEW_KEY: Any
    def __init__(self):
        ...
    @classmethod
    def goTo(cls, tabId, **params):
        ...
    def registerTransitions(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
