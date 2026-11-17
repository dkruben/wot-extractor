# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/fun_random_hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FUN_RANDOM_BANNER_LAST_VISITED_SEASON_BORDER as FUN_RANDOM_BANNER_LAST_VISITED_SEASON_BORDER, HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS, HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS
from frameworks.wulf import WindowFlags as WindowFlags
from fun_random.gui.feature.fun_constants import FunSubModesState as FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode as hasDesiredSubMode
from fun_random.gui.filters.fun_random_carousel_filter import FunRandomCarouselFilter as FunRandomCarouselFilter
from fun_random.gui.fun_account_settings import FunSubModeAccountSettings as FunSubModeAccountSettings
from fun_random.gui.impl.lobby.hangar.base.fun_vehicles_filter_component import FunRandomVehiclesFilterComponent as FunRandomVehiclesFilterComponent
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_loadout_presenter import FunRandomLoadoutPresenter as FunRandomLoadoutPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_modifiers_presenter import FunRandomModifiersPresenter as FunRandomModifiersPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_mode_state_presenter import FunRandomModeStatePresenter as FunRandomModeStatePresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_vehicle_filters_presenter import FunRandomVehicleFiltersDataProvider as FunRandomVehicleFiltersDataProvider
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_vehicles_info_presenter import FunRandomVehiclesInfoPresenter as FunRandomVehiclesInfoPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_vehicle_inventory_presenter import FunRandomVehicleInventoryPresenter as FunRandomVehicleInventoryPresenter
from fun_random.gui.impl.lobby.hangar.presenters.fun_random_user_missions_presenter import FunRandomUserMissionsPresenter as FunRandomUserMissionsPresenter
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID as UNKNOWN_EVENT_ID
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from gui.app_loader import app_getter as app_getter
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.lobby.common.presenters.dynamic_economics_presenter import DynamicEconomicsPresenter as DynamicEconomicsPresenter
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter as CrewPresenter
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter as HangarVehicleParamsPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.hangar.presenters.pet_object_tooltip_presenter import PetObjectTooltipPresenter as PetObjectTooltipPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from gui.impl.lobby.hangar.presenters.teaser_presenter import TeaserPresenter as TeaserPresenter
from gui.impl.lobby.hangar.presenters.utils import getMenuItems as getMenuItems
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter as VehiclesStatisticsPresenter
from gui.impl.lobby.hangar.random.sound_manager import RANDOM_HANGAR_SOUND_SPACE as RANDOM_HANGAR_SOUND_SPACE
from gui.impl.lobby.hangar.base.blur import RandomHangarBlur as RandomHangarBlur
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from helpers import dependency as dependency
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from shared_utils import nextTick as nextTick
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from fun_random.gui.shared.events import FunSelectionEvent as FunSelectionEvent
from gui.impl.pub.view_impl import TViewModel as TViewModel
from hangar_selectable_objects.interfaces import ISelectableLogic as ISelectableLogic

class FunRandomHangarWindow(WindowImpl):
    _statsCollector: Any
    def __init__(self, layer, **kwargs):
        ...
    def _onReady(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class FunRandomHangar(IRoutableView, FunSubModesWatcher):
    _COMMON_SOUND_SPACE = RANDOM_HANGAR_SOUND_SPACE
    __router: Any
    __inputManager: Any
    __accountStyles: Any
    __carouselFilter: Any
    __vehicleInvFilter: Any
    __blur: Any
    def __init__(self, layoutId=..., model=...):
        ...
    @property
    def blur(self):
        ...
    def getRouterModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _finalize(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def __onSubModeChanged(self, funSelectionEvent):
        ...
    # decorador original: @hasDesiredSubMode(...)
    def __processAccountSettings(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __initializeSubSystems(self):
        ...
    def __createSelectableLogic(self):
        ...
    def __escapeHandler(self):
        ...
