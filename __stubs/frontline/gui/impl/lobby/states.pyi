# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from frontline.constants.aliases import FrontlineHangarAliases as FrontlineHangarAliases
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineConst as FrontlineConst
from frontline.gui.impl.gen.view_models.views.lobby.views.info_page_scroll_to_section import InfoPageScrollToSection as InfoPageScrollToSection
from frontline.gui.impl.lobby.progression_screen_view import ProgressionScreenView as ProgressionScreenView
from gui import SystemMessages as SystemMessages
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype, generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription, LobbyStateFlags as LobbyStateFlags, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared.event_dispatcher import showFrontlineInfoWindow as showFrontlineInfoWindow
from gui.shared.utils.functions import getViewName as getViewName
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.game_control import ILoadoutController as ILoadoutController
from frontline.gui.frontline_helpers import becomeNonPlayerState as becomeNonPlayerState
import gui.impl.lobby.hangar.playlists_states as playlists
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from frontline.gui.impl.lobby.hangar_view import FrontlineHangar as FrontlineHangar
EditFrontlinePlaylistsState: Any
FrontlineLoadoutStateBase: Any
_: Any
FrontlineLoadoutSectionState: Any
FrontlineShellsLoadoutState: Any

class FrontlineStateIDs(object):
    FRONTLINE = 'frontline'
    HANGAR = 'hangar'
    ROOT = '{root}'
    LOADOUT_CONFIRM_LEAVE = 'frontline/loadoutConfirmLeave'
    ALL_VEHICLES = 'allVehicles'
    PROGRESSION_SCREEN = 'frontlineProgressionScreen'
    BATTLE_ABILITIES = FrontlineConst.BATTLE_ABILITIES
    BATTLE_RESULTS = 'fl_battleResults'
    OVERVIEW = 'overview'
    TEAM_SCORE = 'teamScore'
    FINANCIAL_REPORT = 'financialReport'

# decorador original: @SubScopeSubLayerState.parentOf
class FrontlineModeState(LobbyState):
    STATE_ID = FrontlineStateIDs.FRONTLINE
    __epicController: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _hijackTransitionCondition(self, _):
        ...

# decorador original: @FrontlineModeState.parentOf
class FrontlineHangarState(SFViewLobbyState):
    STATE_ID = FrontlineStateIDs.HANGAR
    VIEW_KEY: Any
    __appLoader: Any
    __hangarObserver: Any
    def __init__(self, flags=...):
        ...
    def registerStates(self):
        ...
    def __getView(self):
        ...

# decorador original: @FrontlineHangarState.parentOf
class FrontlineRootHangarState(LobbyState):
    STATE_ID = FrontlineStateIDs.ROOT
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...

class _FlLoadoutConfirmStatePrototype(_LoadoutConfirmStatePrototype):
    STATE_ID = FrontlineStateIDs.LOADOUT_CONFIRM_LEAVE

# decorador original: @FrontlineHangarState.parentOf
class FrontlineAllVehiclesState(LobbyState):
    STATE_ID = FrontlineStateIDs.ALL_VEHICLES
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @FrontlineModeState.parentOf
class ProgressionScreenState(GuiImplViewLobbyState):
    STATE_ID = FrontlineStateIDs.PROGRESSION_SCREEN
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...
    def __openInfoView(self):
        ...

class _BattleAbilitiesLoadoutStatePrototype(LobbyState):
    def getNavigationDescription(self):
        ...
    @staticmethod
    def __openInfoView(*_):
        ...

# decorador original: @FrontlineLoadoutStateBase.parentOf
class FrontlineBattleAbilitiesLoadoutState(FrontlineLoadoutSectionState, _BattleAbilitiesLoadoutStatePrototype):
    STATE_ID: Any

class FrontlineLoadoutState(FrontlineLoadoutStateBase):
    __loadoutController: Any
    def registerStates(self):
        ...
    def _onExited(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @FrontlineModeState.parentOf
class FrontlinePostBattleResultsState(SFViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = FrontlineStateIDs.BATTLE_RESULTS
    VIEW_KEY: Any
    __hangarSpace: Any
    __battleResults: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def goTo(cls, arenaUniqueID):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def registerStates(self):
        ...
    # decorador original: @prbDispatcherProperty
    def prbDispatcher(self):
        ...
    def __preventNavigationOutside(self, event):
        ...
    def getViewKey(self, params=None):
        ...
    def __getView(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

class PostBattleTab(LobbyState):
    __hangarSpace: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @FrontlinePostBattleResultsState.parentOf
class _OverviewTab(PostBattleTab):
    STATE_ID = FrontlineStateIDs.OVERVIEW

# decorador original: @FrontlinePostBattleResultsState.parentOf
class _TeamScoreTab(PostBattleTab):
    STATE_ID = FrontlineStateIDs.TEAM_SCORE

# decorador original: @FrontlinePostBattleResultsState.parentOf
class _FinancialReportTab(PostBattleTab):
    STATE_ID = FrontlineStateIDs.FINANCIAL_REPORT

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
