# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.vehicle_preview.states import VehiclePreviewState as BaseVehiclePreviewState
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState
from resource_well.gui.shared.event_dispatcher import openInfoPageScreen as openInfoPageScreen

class BaseProgressionState(ViewLobbyState):
    def getBackNavigationDescription(self, params):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class ProgressionState(BaseProgressionState):
    STATE_ID = 'resourceWell/progression'
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class ProgressionCompletedState(BaseProgressionState):
    STATE_ID = 'resourceWell/completed'
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class VehiclePreviewState(BaseVehiclePreviewState):
    STATE_ID = VIEW_ALIAS.RESOURCE_WELL_VEHICLE_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
