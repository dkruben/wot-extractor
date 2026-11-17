# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from fun_random_common.fun_constants import FunSubModeImpl as FunSubModeImpl
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher, FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.lobby.feature.fun_random_tier_list_view import FunRandomTierListView as FunRandomTierListView
from fun_random.gui.shared.fun_system_factory import collectBattleResultsSubPresenters as collectBattleResultsSubPresenters
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState, LobbyStateFlags as LobbyStateFlags
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES as FUNRANDOM_ALIASES
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.framework.managers.loaders import GuiImplViewLoadParams as GuiImplViewLoadParams
from gui.shared.utils.functions import getViewName as getViewName

# decorador original: @SubScopeSubLayerState.parentOf
class FunRandomProgressionState(ViewLobbyState):
    STATE_ID = FUNRANDOM_ALIASES.FUN_PROGRESSION
    VIEW_KEY: Any
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class FunRandomTierListState(GuiImplViewLobbyState):
    STATE_ID = 'funRandomTierList'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _getViewLoadParams(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class FunPostBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = FUNRANDOM_ALIASES.FUN_POST_BATTLE_RESULTS
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getViewKey(self, params=None):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
