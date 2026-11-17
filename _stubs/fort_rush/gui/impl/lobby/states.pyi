# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from fort_rush.gui.impl.lobby.fort_rush_progression_view import FortRushProgressionView as FortRushProgressionView
from fort_rush.gui.scaleform.genConsts.FORT_RUSH_HANGAR_ALIASES import FORT_RUSH_HANGAR_ALIASES as FORT_RUSH_HANGAR_ALIASES
from fort_rush.gui.shared.event_dispatcher import showFortRushInfoPage as showFortRushInfoPage
from fort_rush_common.fort_rush_constants import QUEUE_TYPE as QUEUE_TYPE
from fort_rush.skeletons.battle_controller import IFortRushBattleController as IFortRushBattleController
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import generateBasicHangarStateClasses as generateBasicHangarStateClasses, generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype
from gui.impl.lobby.hangar.playlists_states import generateVehiclePlayListClasses as generateVehiclePlayListClasses
from gui.impl.lobby.hangar.states import HangarState as HangarState, EasyTankEquipState as EasyTankEquipState
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState, GuiImplViewLobbyState as GuiImplViewLobbyState, SFViewLobbyState as SFViewLobbyState, LobbyStateDescription as LobbyStateDescription, LobbyState as LobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.shared.utils.functions import getViewName as getViewName
from helpers import dependency as dependency
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
FortRushHangarState: Any
FortRushRootHangarState: Any
FortRushAllVehiclesState: Any
FortRushEasyTankEquipState: Any
FortRushEditVehiclePlaylistsState: Any
FortRushLoadoutState: Any
_: Any
FortRushShellsLoadoutState: Any

class FortRushStateIDs(object):
    HANGAR = 'fortRushHangar'
    LOADOUT_LEAVE = 'fortRushLoadoutConfirmLeave'
    PBS = 'fortRushPBS'
    OVERVIEW = 'overview'
    TEAM_SCORE = 'teamScore'
    PROGRESSION = 'progression'

class _HangarStateProto(SFViewLobbyState):
    STATE_ID = FortRushStateIDs.HANGAR
    VIEW_KEY: Any
    _fortRushCtrl: Any
    def registerTransitions(self):
        ...
    def _hijackTransitionCondition(self, _):
        ...

class _LoadoutConfirmStateProto(_LoadoutConfirmStatePrototype):
    STATE_ID = FortRushStateIDs.LOADOUT_LEAVE

# decorador original: @SubScopeTopLayerState.parentOf
class FortRushProgressionState(GuiImplViewLobbyState):
    STATE_ID = FortRushStateIDs.PROGRESSION
    VIEW_KEY: Any
    def __init__(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class FortRushPostBattleResultState(SFViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = FortRushStateIDs.PBS
    VIEW_KEY: Any
    __cachedArenaId: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def goTo(cls, arenaUniqueID):
        ...
    def registerStates(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def getViewKey(self, params=None):
        ...

class PostBattleTab(LobbyState):
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @FortRushPostBattleResultState.parentOf
class _OverviewTab(PostBattleTab):
    STATE_ID = FortRushStateIDs.OVERVIEW

# decorador original: @FortRushPostBattleResultState.parentOf
class _TeamScoreTab(PostBattleTab):
    STATE_ID = FortRushStateIDs.TEAM_SCORE

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
def _isInPrb(event):
    ...
