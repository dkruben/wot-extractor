# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl import backport as backport
from gui.impl.lobby.dog_tags.animated_dog_tags_view import AnimatedDogTagsView as AnimatedDogTagsView
from gui.impl.lobby.dog_tags.dog_tags_view import DogTagsView as DogTagsView
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeTopLayerState as SubScopeTopLayerState, LobbyStateDescription as LobbyStateDescription, LobbyState as LobbyState, TopScopeTopLayerState as TopScopeTopLayerState, SubScopeSubLayerState as SubScopeSubLayerState
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showDogTagCustomizationConfirmDialog as showDogTagCustomizationConfirmDialog
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from wg_async import wg_async as wg_async, wg_await as wg_await
from account_helpers.dog_tags import DogTags as DogTagsAccountHelper

# decorador original: @TopScopeTopLayerState.parentOf
class DogTagConfirmState(LobbyState):
    STATE_ID = 'dogTagConfirmLeave'
    def getNavigationDescription(self):
        ...
    # decorador original: @wg_async
    def _onEntered(self, event):
        ...
    @staticmethod
    def __equipDogTag(selectedBackground, selectedEngraving):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class DogTagState(GuiImplViewLobbyState):
    STATE_ID = 'dogTags'
    VIEW_KEY: Any
    __uiLoader: Any
    def __init__(self):
        ...
    @property
    def selectedBackground(self):
        ...
    @property
    def selectedEngraving(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _dogTagConfirm(self, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class AnimatedDogTagState(GuiImplViewLobbyState):
    STATE_ID = 'animatedDogTags'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
