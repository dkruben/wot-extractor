# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
import BigWorld as BigWorld
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from armor_inspector_common.schemas import armorInspectorConfigSchema as armorInspectorConfigSchema
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree_model import VehSkillTreeModel as VehSkillTreeModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.vehicle_hub_view_model import VehicleHubViewModel as VehicleHubViewModel
from gui.impl.lobby.blueprints.states import BlueprintState as BlueprintState
from gui.impl.lobby.vehicle_hub.camera_mover import VehicleHubCameraMover as VehicleHubCameraMover
from gui.impl.lobby.vehicle_hub.sound_constants import VH_SOUND_SPACE as VH_SOUND_SPACE
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyState as LobbyState, LobbyStateFlags as LobbyStateFlags, LobbyStateDescription as LobbyStateDescription
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView, showHangar as showHangar
from gui.shared.utils.module_upd_available_helper import updateViewedItems as updateViewedItems
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.subhangar.subhangar_observer import selectItemByTankSize as selectItemByTankSize, hangarVehicleAABB as hangarVehicleAABB
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroups as SubhangarStateGroups, SubhangarStateGroupConfig as SubhangarStateGroupConfig
from gui.veh_post_progression.models.progression import PostProgressionCompletion as PostProgressionCompletion
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from gui.impl.lobby.vehicle_hub.vehicle_hub_main_view import VehicleHubCtx as VehicleHubCtx, VehicleHubMainView as VehicleHubMainView
_logger: Any
_CAMERA_TRANSITION_DURATION = 0.8
_TANK_SIZE_LOWER_BOUNDS: tuple

class _VehicleHubChildState(LobbyState, SubhangarStateGroupConfigProvider):
    TAB_NAME = ''
    _SUBHANGAR_GROUPS_BY_TANK_SIZE = None
    __hangarSpace: Any
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class VehicleHubState(SFViewLobbyState, EventsHandler, SubhangarStateGroupConfigProvider):
    STATE_ID = VIEW_ALIAS.VEHICLE_HUB
    VIEW_KEY: Any
    __hangarSpace: Any
    __itemsCache: Any
    __soundExtension: Any
    __cameraMover: Any
    def __init__(self, flags=...):
        ...
    @property
    def cameraMover(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    @classmethod
    def goTo(cls, vhCtx):
        ...
    def serializeParams(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def __setupTankTransformation(self):
        ...
    def _onExited(self):
        ...
    def _getEvents(self):
        ...
    def __onSpaceChanged(self):
        ...

# decorador original: @VehicleHubState.parentOf
class EntryState(LobbyState):
    STATE_ID = 'entry'

# decorador original: @VehicleHubState.parentOf
class _LoadingState(LobbyState, SubhangarStateGroupConfigProvider):
    STATE_ID = 'loading'
    __callbackDelayer: Any
    __cachedParams: Any
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __navigateBackWhenAABBAvailable(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...

# decorador original: @VehicleHubState.parentOf
class OverviewState(_VehicleHubChildState):
    STATE_ID = VehicleHubViewModel.OVERVIEW
    TAB_NAME = VehicleHubViewModel.OVERVIEW
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple

# decorador original: @VehicleHubState.parentOf
class ModulesState(_VehicleHubChildState):
    STATE_ID = VehicleHubViewModel.MODULES
    TAB_NAME = VehicleHubViewModel.MODULES
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...

# decorador original: @VehicleHubState.parentOf
class VehSkillTreeState(_VehicleHubChildState):
    STATE_ID = VehicleHubViewModel.VEH_SKILL_TREE
    TAB_NAME = VehicleHubViewModel.VEH_SKILL_TREE
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...

class _VehSkillTreeSubStateBase(LobbyState):
    def getNavigationDescription(self):
        ...

# decorador original: @VehSkillTreeState.parentOf
class VehSkillTreeInitialState(_VehSkillTreeSubStateBase):
    STATE_ID = VehSkillTreeModel.INITIAL
    __itemsCache: Any
    def _onEntered(self, event):
        ...

# decorador original: @VehSkillTreeState.parentOf
class VehSkillTreeProgressionState(_VehSkillTreeSubStateBase):
    STATE_ID = VehSkillTreeModel.TREE
    SUB_TAB_NAME = VehSkillTreeModel.TREE
    def registerTransitions(self):
        ...

# decorador original: @VehSkillTreeState.parentOf
class VehSkillTreePrestigeState(_VehSkillTreeSubStateBase):
    STATE_ID = VehSkillTreeModel.PRESTIGE
    SUB_TAB_NAME = VehSkillTreeModel.PRESTIGE
    def registerTransitions(self):
        ...

# decorador original: @VehicleHubState.parentOf
class StatsState(_VehicleHubChildState):
    STATE_ID = VehicleHubViewModel.STATS
    TAB_NAME = VehicleHubViewModel.STATS
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple
    __blur: Any
    def __init__(self, flags=...):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# decorador original: @VehicleHubState.parentOf
class ArmorState(_VehicleHubChildState):
    STATE_ID = VehicleHubViewModel.ARMOR
    TAB_NAME = VehicleHubViewModel.ARMOR
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple
    def getNavigationDescription(self):
        ...
    @staticmethod
    def _showVideo():
        ...

def registerStates(machine):
    ...
def registerTransitions(machine):
    ...
