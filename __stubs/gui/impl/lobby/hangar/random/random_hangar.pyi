# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/random/random_hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers.AccountSettings import HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS, HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.app_loader import app_getter as app_getter
from gui.filters.battle_pass_carousel_filter import BattlePassCarouselFilter as BattlePassCarouselFilter
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.lobby.common.presenters.manage_vehicle_playlists_presenter import ManageableVehiclePlaylistsPresenter as ManageableVehiclePlaylistsPresenter
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter as VehiclesInfoPresenter
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_presenter import EasyTankEquipPresenter as EasyTankEquipPresenter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.base.blur import RandomHangarBlur as RandomHangarBlur
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter as CrewPresenter
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter as HangarVehicleParamsPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter as LoadoutPresenter
from gui.impl.lobby.hangar.presenters.lootbox_entry_point_presenter import LootboxEntryPointPresenter as LootboxEntryPointPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.hangar.presenters.optional_devices_assistant_presenter import OptionalDevicesAssistantPresenter as OptionalDevicesAssistantPresenter
from gui.impl.lobby.hangar.presenters.pet_object_tooltip_presenter import PetObjectTooltipPresenter as PetObjectTooltipPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from gui.impl.lobby.hangar.presenters.teaser_presenter import TeaserPresenter as TeaserPresenter
from gui.impl.lobby.hangar.presenters.user_missions_presenter import UserMissionsPresenter as UserMissionsPresenter
from gui.impl.lobby.hangar.presenters.utils import getMenuItems as getMenuItems
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider as VehicleFiltersDataProvider
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter as VehicleInventoryPresenter
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from gui.impl.lobby.hangar.presenters.vehicle_playlists_presenter import VehiclePlaylistsPresenter as VehiclePlaylistsPresenter
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter as VehiclesStatisticsPresenter
from gui.impl.lobby.hangar.presenters.main_plugins_presenter import MainPluginsPresenter as MainPluginsPresenter
from gui.impl.lobby.hangar.random.sound_manager import RANDOM_HANGAR_SOUND_SPACE as RANDOM_HANGAR_SOUND_SPACE
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.shared.system_factory import collectDynamicRandomHangarPresenters as collectDynamicRandomHangarPresenters
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from helpers import dependency as dependency
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from shared_utils import nextTick as nextTick
from skeletons.gui.offers import IOffersBannerController as IOffersBannerController
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from gui.impl.pub.view_impl import TViewModel as TViewModel
from hangar_selectable_objects.interfaces import ISelectableLogic as ISelectableLogic
RANDOM_MODE_CRITERIA: Any

class HangarWindow(WindowImpl):
    _statsCollector: Any
    def __init__(self, layer, **kwargs):
        ...
    def _onReady(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class RandomHangar(IRoutableView):
    _COMMON_SOUND_SPACE = RANDOM_HANGAR_SOUND_SPACE
    __offersBannerController: Any
    __inputManager: Any
    __randomVehicleFilter: Any
    __randomInvVehicleFilter: Any
    __carouselFilter: Any
    __accountStyles: Any
    __blur: Any
    _router: Any
    def __init__(self, layoutId=..., model=...):
        ...
    @property
    def blur(self):
        ...
    def getRouterModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _initializeRouter(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _onHidden(self):
        ...
    def _finalize(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __createSelectableLogic(self):
        ...
    def __escapeHandler(self):
        ...
