# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.lobby.crew.barracks_view import BarracksView as BarracksView
from gui.impl.lobby.crew.container_vews.quick_training.quick_training_view import QuickTrainingView as QuickTrainingView
from gui.impl.lobby.crew.member_change_view import MemberChangeView as MemberChangeView
from gui.impl.lobby.crew.tank_change_view import TankChangeView as TankChangeView
from gui.impl.lobby.crew.tankman_container_view import TankmanContainerView as TankmanContainerView
from gui.lobby_state_machine.events import _BackNavigationGeneratedNavigationEvent as _BackNavigationGeneratedNavigationEvent
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyStateDescription as LobbyStateDescription, SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showCrewAboutView as showCrewAboutView
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT, NO_TANKMAN as NO_TANKMAN
from helpers import dependency as dependency
from skeletons.gui.game_control import ICrewController as ICrewController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache

class _RemovableFromHistoryMixin(object):
    def canBeRemovedFromHistory(self, state, params):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class BarracksState(GuiImplViewLobbyState):
    STATE_ID = 'barracks'
    VIEW_KEY: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class PersonalCaseState(GuiImplViewLobbyState, _RemovableFromHistoryMixin):
    __crewController: Any
    STATE_ID = 'personalCase'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def compareParams(self, params, otherParams):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _focusView(self, view, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class TankChangeState(GuiImplViewLobbyState, _RemovableFromHistoryMixin):
    __crewController: Any
    STATE_ID = 'tankChange'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _focusView(self, view, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class MemberChangeState(GuiImplViewLobbyState):
    __crewController: Any
    STATE_ID = 'memberChange'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _focusView(self, view, event):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class QuickTrainingState(GuiImplViewLobbyState, _RemovableFromHistoryMixin):
    __crewController: Any
    STATE_ID = 'quickTraining'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def compareParams(self, params, otherParams):
        ...
    def _focusView(self, view, event):
        ...

def registerStates(machine):
    ...
def registerTransitions(_):
    ...
