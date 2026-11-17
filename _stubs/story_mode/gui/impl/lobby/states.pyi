# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags, LobbyStateDescription as LobbyStateDescription, TopScopeTopLayerState as TopScopeTopLayerState, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from helpers import dependency as dependency
from story_mode.gui.impl.lobby.mission_selection_view import MissionSelectionView as MissionSelectionView
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController

# decorador original: @SubScopeSubLayerState.parentOf
class StoryModeState(GuiImplViewLobbyState):
    STATE_ID = 'storyMode'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class StoryModeBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = VIEW_ALIAS.STORY_MODE_BATTLE_RESULTS
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _shallNavigateToStoryModeHangar(event, storyModeCtrl=None):
    ...
