# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from gui.Scaleform.daapi.view.lobby.battle_queue.states import BattleQueueContainerState as BattleQueueContainerState
from gui.Scaleform.daapi.view.lobby.battle_queue.states import CommonBattleQueueState as CommonBattleQueueState
from gui.Scaleform.daapi.view.lobby.shared.states import BrowserLobbyTopState as BrowserLobbyTopState
from gui.Scaleform.daapi.view.lobby.veh_post_progression.states import VehiclePostProgressionState as VehiclePostProgressionState
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_results.service import PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.crew.states import BarracksState as BarracksState
from gui.impl.lobby.hangar.base.proto_states import generateBasicLoadoutStateClasses as generateBasicLoadoutStateClasses, _LoadoutConfirmStatePrototype as _LoadoutConfirmStatePrototype, _ConsumablesLoadoutStatePrototype as _ConsumablesLoadoutStatePrototype, _LoadoutStatePrototype as _LoadoutStatePrototype
from gui.impl.lobby.hangar.states import HangarState as HangarState
from gui.impl.lobby.tank_setup.tank_setup_sounds import playEnterTankSetupView as playEnterTankSetupView
from gui.impl.lobby.vehicle_hub import OverviewState as OverviewState, ModulesState as ModulesState, VehSkillTreeState as VehSkillTreeState, StatsState as StatsState, ArmorState as ArmorState
from gui.lobby_state_machine.states import GuiImplViewLobbyState as GuiImplViewLobbyState, LobbyState as LobbyState, SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateFlags as LobbyStateFlags, SubScopeTopLayerState as SubScopeTopLayerState, TopScopeTopLayerState as TopScopeTopLayerState, LobbyStateDescription as LobbyStateDescription, ViewLobbyState as ViewLobbyState
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.shared.events import NavigationEvent as NavigationEvent
from halloween.gui.impl.lobby.bestiary.states import HWBestiaryState as HWBestiaryState
from halloween.gui.impl.lobby.bundle_view import BundleView as BundleView
from halloween.gui.impl.lobby.pre_battle_queue_view import PreBattleQueueView as PreBattleQueueView
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from halloween.gui.shared.event_dispatcher import showIntroVideo as showIntroVideo, showMetaIntroView as showMetaIntroView
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.gui.halloween_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from helpers import dependency as dependency
from gui.impl.lobby.vehicle_hub.states import VehicleHubState as VehicleHubState
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
HalloweenLoadoutState: Any
_: Any
HalloweenConsumablesLoadoutState: Any

# decorador original: @SubScopeSubLayerState.parentOf
class HalloweenModeState(LobbyState):
    STATE_ID = 'halloween'
    halloweenCtrl: Any
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def _registrationTransition(self, hangar, rewardPath, states):
        ...
    @classmethod
    def _isEventPrb(cls, event):
        ...

# decorador original: @HalloweenModeState.parentOf
class HalloweenHangarState(SFViewLobbyState):
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

# decorador original: @HalloweenHangarState.parentOf
class HalloweenRootHangarState(LobbyState):
    STATE_ID = '{root}'
    def __init__(self, flags=...):
        ...

# decorador original: @HalloweenModeState.parentOf
class RewardPathState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_REWARD_PATH
    VIEW_KEY: Any
    halloweenCtrl: Any
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

# decorador original: @BattleQueueContainerState.parentOf
class HalloweenPreBattleQueueState(GuiImplViewLobbyState):
    STATE_ID = 'halloweenPreBattleQueue'
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

# decorador original: @HalloweenModeState.parentOf
class HalloweenVehiclePreviewState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_VEHICLE_PREVIEW
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

# decorador original: @HalloweenModeState.parentOf
class HalloweenHeroTankPreviewState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_HERO_PREVIEW
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

# decorador original: @SubScopeTopLayerState.parentOf
class HalloweenExchangeScreenState(GuiImplViewLobbyState):
    STATE_ID = 'halloweenExchangeScreenState'
    VIEW_KEY: Any
    def __init__(self, flags=...):
        ...
    def getNavigationDescription(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class HalloweenBattleResultsState(ViewLobbyState, PostBattleResultsStateMixin):
    STATE_ID = VIEW_ALIAS.HALLOWEEN_BATTLE_RESULTS
    VIEW_KEY: Any
    def registerTransitions(self):
        ...

class _HalloweenLoadoutConfirmStateProto(_LoadoutConfirmStatePrototype):
    STATE_ID = 'halloweenLoadoutConfirmLeave'

class _HalloweenLoadoutStateCls(_LoadoutStatePrototype):
    STATE_ID = 'loadout'
    def _onEntered(self, event):
        ...

class _HalloweenConsumableLoadoutState(_ConsumablesLoadoutStatePrototype):
    STATE_ID = 'hw_consumables'
    def getNavigationDescription(self):
        ...

# decorador original: @HalloweenModeState.parentOf
class AnomaliesState(SFViewLobbyState):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_ANOMALIES
    VIEW_KEY: Any
    def getNavigationDescription(self):
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
