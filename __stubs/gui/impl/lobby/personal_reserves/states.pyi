# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/personal_reserves/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.lobby.personal_reserves.reserves_activation_view import ReservesActivationView as ReservesActivationView
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyStateDescription as LobbyStateDescription, SubScopeTopLayerState as SubScopeTopLayerState
from gui.impl.gen import R as R

# decorador original: @SubScopeTopLayerState.parentOf
class PersonalReservesState(GuiImplViewLobbyState):
    STATE_ID = 'personal_reserves'
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
