# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS, HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS
from frontline.gui.impl.lobby.presenters.alert_presenter import AlertPresenter as AlertPresenter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.hangar.base.sound_constants import HangarSoundStates as HangarSoundStates
from gui.impl.lobby.hangar.presenters.vehicle_playlists_presenter import VehiclePlaylistsPresenter as VehiclePlaylistsPresenter
from gui.impl.lobby.hangar.presenters.pet_object_tooltip_presenter import PetObjectTooltipPresenter as PetObjectTooltipPresenter
from gui.sounds.epic_sound_constants import EPIC_SOUND as EPIC_SOUND
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from gui.impl.lobby.hangar.base.blur import RandomHangarBlur as RandomHangarBlur
from shared_utils import nextTick as nextTick
from gui.impl.pub import WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.game_loading.resources.consts import Milestones as Milestones
from frameworks.wulf import WindowFlags as WindowFlags
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.app_loader import app_getter as app_getter
from gui.impl.lobby.hangar.presenters.utils import getMenuItems as getMenuItems
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter as VehiclesInfoPresenter
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from frontline.gui.impl.lobby.presenters.frontline_loadout_presenter import FrontlineLoadoutPresenter as FrontlineLoadoutPresenter
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from frontline.gui.impl.lobby.presenters.fl_vehicle_inventory_presenter import FLVehicleInventoryPresenter as FLVehicleInventoryPresenter
from frontline.gui.impl.lobby.presenters.fl_vehicles_statistics_presenter import FLVehiclesStatisticsPresenter as FLVehiclesStatisticsPresenter
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter as CrewPresenter
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter as HangarVehicleParamsPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.common.presenters.manage_vehicle_playlists_presenter import ManageableVehiclePlaylistsPresenter as ManageableVehiclePlaylistsPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from gui.impl.lobby.hangar.presenters.teaser_presenter import TeaserPresenter as TeaserPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.optional_devices_assistant_presenter import OptionalDevicesAssistantPresenter as OptionalDevicesAssistantPresenter
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider as VehicleFiltersDataProvider
from frontline.gui.impl.lobby.tooltips.level_reserves_tooltip import LevelReservesTooltip as LevelReservesTooltip
from frontline.gui.Scaleform.daapi.view.battle.frontline_battle_carousel import BattleCarouselFilter as BattleCarouselFilter
from frontline.constants.aliases import FrontlineHangarAliases as FrontlineHangarAliases
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from gui.impl.pub.view_impl import TViewModel as TViewModel
from typing import Optional as Optional

class FrontlineHangarWindow(WindowImpl):
    _statsCollector: Any
    def __init__(self, layer, *_, **__):
        ...
    def _onReady(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class FrontlineHangar(IRoutableView):
    _COMMON_SOUND_SPACE: Any
    __routerObserver: Any
    __inputManager: Any
    __carouselFilter: Any
    __accountStyles: Any
    __baseCriteria: Any
    __vehicleFilter: Any
    __invVehicleFilter: Any
    __blur: Any
    def __init__(self, layoutId=..., model=...):
        ...
    @property
    def blur(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getRouterModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __escapeHandler(self):
        ...

def _createFrontlineCriteria():
    ...
