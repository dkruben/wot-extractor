# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.storage_view import StorageView as StorageView
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader

# decorador original: @SubScopeSubLayerState.parentOf
class StorageState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.LOBBY_STORAGE
    VIEW_KEY: Any
    __appLoader: Any
    def registerTransitions(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class OfferGiftsState(ViewLobbyState):
    STATE_ID = VIEW_ALIAS.OFFER_GIFT_VIEW
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    @classmethod
    def goTo(cls, offerID=None, overrideSuccessCallback=None, overrideOnBackCallback=None):
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
