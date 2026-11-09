# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/daily_experience/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.lobby.daily_experience.daily_experience_view import DailyExperienceView as DailyExperienceView
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeTopLayerState as SubScopeTopLayerState, LobbyStateDescription as LobbyStateDescription
from gui.impl.gen import R as R
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine

# decorador original: @SubScopeTopLayerState.parentOf
class DailyExperienceState(GuiImplViewLobbyState):
    STATE_ID = 'dailyExperience'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
