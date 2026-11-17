# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, LobbyStateFlags as LobbyStateFlags, SubScopeSubLayerState as SubScopeSubLayerState, ViewLobbyState as ViewLobbyState

class _VehiclePreviewStateProto(ViewLobbyState):
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _prepareCamera(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class VehiclePreviewStateWithTopPanel(LobbyState):
    STATE_ID = 'vehiclePreviewWithTopPanel'
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class VehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.VEHICLE_PREVIEW
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class HeroTankPreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.HERO_VEHICLE_PREVIEW
    VIEW_KEY: Any
    def _prepareCamera(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @VehiclePreviewStateWithTopPanel.parentOf
class ConfigurableVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.CONFIGURABLE_VEHICLE_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class RentalVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.RENTAL_VEHICLE_PREVIEW
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class TradeInVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.TRADE_IN_VEHICLE_PREVIEW
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class MarathonVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.MARATHON_VEHICLE_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class OfferGiftVehiclePreviewState(_VehiclePreviewStateProto):
    STATE_ID = VIEW_ALIAS.OFFER_GIFT_VEHICLE_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

class _StylePreviewStateProto(ViewLobbyState):
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _prepareCamera(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @VehiclePreviewStateWithTopPanel.parentOf
class StylePreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_PREVIEW
    VIEW_KEY: Any

# decorador original: @SubScopeSubLayerState.parentOf
class StyleProgressionPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_PROGRESSION_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class StyleBuyingPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.STYLE_BUYING_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class ShowcaseStyleBuyingPreviewState(_StylePreviewStateProto):
    STATE_ID = VIEW_ALIAS.SHOWCASE_STYLE_BUYING_PREVIEW
    VIEW_KEY: Any
    def _getViewLoadCtx(self, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
