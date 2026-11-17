# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.lobby_state_machine.states import SubScopeTopLayerState as SubScopeTopLayerState, SFViewLobbyState as SFViewLobbyState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyState as LobbyState
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import AmmunitionSetupViewEvent as AmmunitionSetupViewEvent
from helpers.dependency import replace_none_kwargs as replace_none_kwargs
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from wg_async import wg_async as wg_async, BrokenPromiseError as BrokenPromiseError
from gui.impl.lobby.tank_setup.ammunition_setup.base import BaseAmmunitionSetupView as BaseAmmunitionSetupView
from gui.lobby_state_machine.states import LobbyStateDescription as LobbyStateDescription
_logger: Any

# decorador original: @SubScopeTopLayerState.parentOf
class LegacyAmmunitionState(SFViewLobbyState):
    STATE_ID = 'legacyAmmunition'
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    def _hasChanges(self, _):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class LegacyAmmunitionConfirmationState(LobbyState):
    STATE_ID = 'legacyAmmuntionConfirmLeave'
    def getNavigationDescription(self):
        ...
    # decorador original: @wg_async
    def _onEntered(self, event):
        ...
    def __continueOriginalNavigation(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
# decorador original: @replace_none_kwargs(...)
def _getAmmunitionSubView(appLoader=None):
    ...
