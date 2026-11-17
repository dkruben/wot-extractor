# wot-extractor: STUB (.pyi) gerado a partir de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.vehicle_hub import OverviewState as OverviewState
from gui.impl.lobby.vehicle_hub.states import VehicleHubState as VehicleHubState
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyStateDescription as LobbyStateDescription, SubScopeSubLayerState as SubScopeSubLayerState
from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import StylePreviewState as StylePreviewState
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from open_bundle.gui.impl.lobby.main_view import MainView as MainView
from open_bundle.gui.shared.event_dispatcher import showIntro as showIntro
from open_bundle.helpers.account_settings import isIntroShown as isIntroShown
from open_bundle.helpers.resources import getTextResource as getTextResource
from typing import Optional as Optional
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine

# decorador original: @SubScopeSubLayerState.parentOf
class OpenBundleState(GuiImplViewLobbyState):
    STATE_ID = 'openBundle'
    VIEW_KEY: Any
    __params: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
