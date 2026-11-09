# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, ViewLobbyState as ViewLobbyState, LobbyStateDescription as LobbyStateDescription
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket

# decorador original: @SubScopeSubLayerState.parentOf
class VehicleCompareState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEHICLE_COMPARE
    VIEW_KEY: Any
    comparisonBasket: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class VehicleCompareConfiguratorState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.VEHICLE_COMPARE_MAIN_CONFIGURATOR
    VIEW_KEY: Any
    comparisonBasket: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
