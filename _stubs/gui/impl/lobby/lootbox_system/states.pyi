# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from frameworks.wulf import WindowLayer as WindowLayer
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.main_view_model import SubViewID as SubViewID
from gui.lootbox_system.base.awards_manager import AwardsManager as AwardsManager
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.lootbox_system.base.common import REROLLABLE_BOX_OPEN_COUNT as REROLLABLE_BOX_OPEN_COUNT, getTextResource as getTextResource
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.lobby_state_machine.states import StateFlags as StateFlags, LobbyStateFlags as LobbyStateFlags, SubScopeSubLayerState as SubScopeSubLayerState, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, SFViewLobbyState as SFViewLobbyState
from gui.shared.system_factory import collectLootBoxInfoPage as collectLootBoxInfoPage, collectLootBoxMainView as collectLootBoxMainView
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
_REWARD_SUBVIEW_IDS: tuple

class _LootBoxBaseState(SFViewLobbyState):
    _lootBoxes: Any
    _shouldRedirectToHangar: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    @classmethod
    def goTo(cls, ctx):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def isLootBoxesAvailable(self):
        ...
    def updateCachedCtx(self, params):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def __onStatusChanged(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class LootBoxState(LobbyState):
    __appLoader: Any
    __previouslyVisibleLayers: Any
    def __init__(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getVisibleLayers(self):
        ...

# decorador original: @LootBoxState.parentOf
class LootBoxInfoState(_LootBoxBaseState):
    STATE_ID = 'lootBoxInfoState'
    VIEW_KEY: Any
    def getViewKey(self, params=None):
        ...

# decorador original: @LootBoxState.parentOf
class LootBoxMainState(_LootBoxBaseState):
    STATE_ID = 'lootBoxMainState'
    VIEW_KEY: Any
    def _onEntered(self, event):
        ...
    def getViewKey(self, params=None):
        ...
    def registerTransitions(self):
        ...

# decorador original: @LootBoxState.parentOf
class LootBoxAutoOpenState(_LootBoxBaseState):
    STATE_ID = 'lootBoxAutoOpenState'
    VIEW_KEY: Any
    _shouldRedirectToHangar: Any
    def __init__(self, flags=...):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
