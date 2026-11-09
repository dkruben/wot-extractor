# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from account_helpers.AccountSettings import HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS, HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS
from gui.impl.lobby.hangar.presenters.pet_object_tooltip_presenter import PetObjectTooltipPresenter as PetObjectTooltipPresenter
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from fort_rush.account_helpers import account_settings as fort_rush_account_settings
from fort_rush.gui.fort_rush_gui_constants import PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from fort_rush.gui.filters.fort_rush_carousel_filter import FortRushCarouselFilter as FortRushCarouselFilter
from fort_rush_common.fort_rush_constants import FORT_RUSH_VEHICLE_TAG as FORT_RUSH_VEHICLE_TAG
from fort_rush.gui.impl.lobby.presenters.fort_rush_lobby_vehicle_filters_presenter import FortRushLobbyVehicleFiltersPresenter as FortRushLobbyVehicleFiltersPresenter
from fort_rush.gui.impl.lobby.presenters.fort_rush_lobby_vehicles_info_presenter import FortRushLobbyVehiclesInfoPresenter as FortRushLobbyVehiclesInfoPresenter
from fort_rush.gui.impl.lobby.presenters.loadout_presenter import FortRushLoadoutPresenter as FortRushLoadoutPresenter
from fort_rush.gui.impl.lobby.user_missions.fort_rush_user_missions_presenter import FortRushUserMissionsPresenter as FortRushUserMissionsPresenter
from frameworks.wulf import WindowFlags as WindowFlags
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.app_loader import app_getter as app_getter
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_constants import AmmunitionPanelConstants as AmmunitionPanelConstants
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.common.presenters.dynamic_economics_presenter import DynamicEconomicsPresenter as DynamicEconomicsPresenter
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_presenter import EasyTankEquipPresenter as EasyTankEquipPresenter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.base.blur import RandomHangarBlur as RandomHangarBlur
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter as CrewPresenter
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter as HangarVehicleParamsPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from gui.impl.lobby.hangar.presenters.utils import RANDOM_MENU_ITEMS as RANDOM_MENU_ITEMS
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter as VehicleInventoryPresenter
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from gui.impl.lobby.hangar.presenters.vehicle_playlists_presenter import VehiclePlaylistsPresenter as VehiclePlaylistsPresenter
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter as VehiclesStatisticsPresenter
from gui.impl.lobby.common.presenters.manage_vehicle_playlists_presenter import ManageableVehiclePlaylistsPresenter as ManageableVehiclePlaylistsPresenter
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.prb_control import prb_getters as prb_getters
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.shared.utils import SelectorBattleTypesUtils as SelectorBattleTypesUtils
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from shared_utils import nextTick as nextTick
from gui.impl.pub.view_impl import TViewModel as TViewModel
EXT_MODE_CRITERIA: Any

class FortRushHangarWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...

# base nao representavel no stub: ViewComponent[...]
class FortRushHangarView(IRoutableView):
    LAYOUT_ID: Any
    __inputManager: Any
    __isUnitJoiningInProgress: Any
    __timer: Any
    __router: Any
    __allModeVehicleFilter: Any
    __accountVehicleFilter: Any
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
    def _initializeRouter(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _finalize(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __escapeHandler(self):
        ...
    def __createSelectableLogic(self):
        ...
    def __onPrebattleInvitationAccepted(self, *args):
        ...
    def __onResetUnitJoiningProgress(self):
        ...
    def __onUnitJoined(self, *args):
        ...

def _showLoadout():
    ...
def _restoreLastSelectedVehicle():
    ...
def _onCurrentVehicleChanged():
    ...
