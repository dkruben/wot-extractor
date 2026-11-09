# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.lobby.battle_queue.states import BattleQueueContainerState as BattleQueueContainerState
from gui.Scaleform.daapi.view.lobby.veh_post_progression.states import VehiclePostProgressionState as VehiclePostProgressionState
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.base.proto_states import _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype, generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutStatePrototype as _LoadoutStatePrototype, _ConsumablesLoadoutStatePrototype as _ConsumablesLoadoutStatePrototype
import gui.impl.lobby.hangar.playlists_states as playlists
from gui.impl.lobby.crew.states import BarracksState as BarracksState
from gui.impl.lobby.lootbox_system.states import LootBoxMainState as LootBoxMainState
from gui.impl.lobby.hangar.random.sound_manager import ALL_VEHICLES_SOUND_SPACE as ALL_VEHICLES_SOUND_SPACE
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView as playEnterTankSetupView
from gui.impl.lobby.vehicle_hub import OverviewState as OverviewState, ModulesState as ModulesState, VehSkillTreeState as VehSkillTreeState, StatsState as StatsState, ArmorState as ArmorState
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyState as LobbyState, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control import prbEntityProperty as prbEntityProperty
from last_stand.gui.impl.lobby.pre_battle_queue_view import PreBattleQueueView as PreBattleQueueView
from last_stand.gui.ls_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from last_stand.gui.scaleform.genConsts.LAST_STAND_HANGAR_ALIASES import LAST_STAND_HANGAR_ALIASES as LAST_STAND_HANGAR_ALIASES
from last_stand.gui.shared.event_dispatcher import showMetaIntroView as showMetaIntroView, showIntroVideo as showIntroVideo, showNarrationWindowView as showNarrationWindowView
from last_stand.skeletons.ls_controller import ILSController as ILSController
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from helpers import dependency as dependency
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings, setSettings as setSettings
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.shared.events import NavigationEvent as NavigationEvent
LastStandEditPlaylistsState: Any
LastStandLoadoutState: Any
_: Any
LastStandConsumableLoadoutState: Any

# decorador original: @SubScopeSubLayerState.parentOf
class LastStandModeState(LobbyState):
    STATE_ID = 'lastStand'
    lsCtrl: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _registrationTransition(self, hangar, rewardPath, states):
        ...
    @classmethod
    def _isEventPrb(cls, event):
        ...

# decorador original: @LastStandModeState.parentOf
class LastStandHangarState(SFViewLobbyState):
    STATE_ID = 'hangar'
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def registerStates(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @LastStandHangarState.parentOf
class LastStandRootHangarState(LobbyState):
    STATE_ID = '{root}'
    def __init__(self, flags=...):
        ...

# decorador original: @LastStandHangarState.parentOf
class LastStandAllVehiclesState(LobbyState):
    STATE_ID = 'allVehicles'
    __soundExtension: Any
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @LastStandModeState.parentOf
class LastStandRewardPathState(SFViewLobbyState):
    STATE_ID = LAST_STAND_HANGAR_ALIASES.LS_REWARD_PATH
    VIEW_KEY: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...

# decorador original: @BattleQueueContainerState.parentOf
class LastStandPreBattleQueueState(GuiImplViewLobbyState):
    STATE_ID = 'lastStandPreBattleQueue'
    VIEW_KEY: Any
    __startTime: Any
    def __init__(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def getNavigationDescription(self):
        ...
    def serializeParams(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @LastStandModeState.parentOf
class LastStandVehiclePreviewState(SFViewLobbyState):
    STATE_ID = LAST_STAND_HANGAR_ALIASES.LS_VEHICLE_PREVIEW
    VIEW_KEY: Any
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

# decorador original: @LastStandModeState.parentOf
class LastStandHeroTankPreviewState(SFViewLobbyState):
    STATE_ID = LAST_STAND_HANGAR_ALIASES.LS_HERO_PREVIEW
    VIEW_KEY: Any
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
    def _prepareExited(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class LastStandBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = VIEW_ALIAS.LS_BATTLE_RESULTS
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

class _LastStandLoadoutConfirmStateProto(_LoadoutConfirmStatePrototype):
    STATE_ID = 'lastStandLoadoutConfirmLeave'

class _LastStandLoadoutStateCls(_LoadoutStatePrototype):
    STATE_ID = 'loadout'
    lsCtrl: Any
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

class _LastStandConsumableLoadoutState(_ConsumablesLoadoutStatePrototype):
    STATE_ID = 'ls_consumables'
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
