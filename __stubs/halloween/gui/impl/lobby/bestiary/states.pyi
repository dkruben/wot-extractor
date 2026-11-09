# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/bestiary/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
import BigWorld as BigWorld
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.vehicle_hub.camera_mover import VehicleHubCameraMover as VehicleHubCameraMover
from gui.impl.lobby.vehicle_hub.sound_constants import VH_SOUND_SPACE as VH_SOUND_SPACE
from gui.lobby_state_machine.events import _BackNavigationGeneratedNavigationEvent as _BackNavigationGeneratedNavigationEvent
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SFViewLobbyState as SFViewLobbyState, LobbyStateFlags as LobbyStateFlags, LobbyState as LobbyState, LobbyStateDescription as LobbyStateDescription
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.events import NavigationEvent as NavigationEvent
from gui.subhangar.subhangar_observer import selectItemByTankSize as selectItemByTankSize, hangarVehicleAABB as hangarVehicleAABB
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroups as SubhangarStateGroups, SubhangarStateGroupConfig as SubhangarStateGroupConfig
from halloween.gui.impl.lobby.hw_helpers.bestiary_helper import getOutfit as getOutfit
from halloween.gui.scaleform.genConsts.HALLOWEEN_HANGAR_ALIASES import HALLOWEEN_HANGAR_ALIASES as HALLOWEEN_HANGAR_ALIASES
from halloween.skeletons.halloween_bestiary_controller import IHalloweenBestiaryController as IHalloweenBestiaryController
from halloween_common.configs.halloween_bestiary import EnemyModel as EnemyModel
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from sound_gui_manager import ViewSoundExtension as ViewSoundExtension
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
_CAMERA_TRANSITION_DURATION = 0.8
_TANK_SIZE_LOWER_BOUNDS: tuple

# decorador original: @SubScopeSubLayerState.parentOf
class HWBestiaryState(SFViewLobbyState, SubhangarStateGroupConfigProvider):
    STATE_ID = HALLOWEEN_HANGAR_ALIASES.HALLOWEEN_BESTIARY
    VIEW_KEY: Any
    __hangarSpace: Any
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
    def goTo(cls, vehIntCD=None):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...
    def __setupTankTransformation(self):
        ...
    def _onExited(self):
        ...

# decorador original: @HWBestiaryState.parentOf
class HWBestiaryEntryState(LobbyState):
    STATE_ID = 'hwBestiaryEntry'

# decorador original: @HWBestiaryState.parentOf
class HWBestiaryOverviewState(LobbyState, SubhangarStateGroupConfigProvider):
    STATE_ID = 'hwBestiaryOverview'
    _SUBHANGAR_GROUPS_BY_TANK_SIZE: tuple
    hwBestiaryCtrl: Any
    def registerTransitions(self):
        ...
    def _onEntered(self, event):
        ...
    def getNavigationDescription(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...

# decorador original: @HWBestiaryState.parentOf
class _HWBestiaryLoadingState(LobbyState, SubhangarStateGroupConfigProvider):
    STATE_ID = 'hwBestiaryLoading'
    itemsCache: Any
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
