# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from account_helpers.AccountSettings import HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS, HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter as VehiclesInfoPresenter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.presenters.lootbox_entry_point_presenter import LootboxEntryPointPresenter as LootboxEntryPointPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.hangar.presenters.optional_devices_assistant_presenter import OptionalDevicesAssistantPresenter as OptionalDevicesAssistantPresenter
from gui.impl.lobby.hangar.presenters.utils import getSharedMenuItems as getSharedMenuItems
from gui.impl.lobby.hangar.presenters.vehicle_filters_presenter import VehicleFiltersDataProvider as VehicleFiltersDataProvider
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from gui.impl.lobby.hangar.presenters.vehicle_playlists_presenter import VehiclePlaylistsPresenter as VehiclePlaylistsPresenter
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from last_stand.gui.impl.lobby.base_view import SwitcherPresenter as SwitcherPresenter
from last_stand.gui.impl.lobby.battle_result_view import BattleResultView as BattleResultView
from last_stand.gui.impl.lobby.ls_vehicle_params_view import LSVehicleParamsPresenter as LSVehicleParamsPresenter
from last_stand.gui.impl.lobby.crew.ls_crew_presenter import LSCrewPresenter as LSCrewPresenter
from last_stand.gui.impl.lobby.vehicles_data_providers.ls_vehicle_daily_presenter import LSVehiclesDailyPresenter as LSVehiclesDailyPresenter
from last_stand.gui.impl.lobby.vehicles_data_providers.ls_vehicle_filter import LSBattleCarouselFilter as LSBattleCarouselFilter
from last_stand.gui.impl.lobby.vehicles_data_providers.ls_vehicle_inventory_presenter import LSVehicleInventoryPresenter as LSVehicleInventoryPresenter
from last_stand.gui.impl.lobby.vehicles_data_providers.ls_vehicle_statistics_presenter import LSVehiclesStatisticsPresenter as LSVehiclesStatisticsPresenter
from last_stand.gui.impl.lobby.vehicles_data_providers.ls_vehicles_filter_component import LSVehiclesFilterComponent as LSVehiclesFilterComponent
from last_stand.gui.impl.lobby.widgets.ls_loadout import LastStandLoadoutPresenter as LastStandLoadoutPresenter
from last_stand.gui.impl.lobby.widgets.parallax_view import ParallaxView as ParallaxView
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from frameworks.wulf import WindowStatus as WindowStatus, WindowFlags as WindowFlags
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.app_loader import app_getter as app_getter
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.shared import g_eventBus as g_eventBus, events as events
from last_stand.gui.impl.gen.view_models.views.lobby.hangar_view_model import HangarViewModel as HangarViewModel
from last_stand.gui.impl.lobby.widgets.difficulty_view import DifficultyView as DifficultyView
from last_stand.gui.shared.event_dispatcher import showInfoPage as showInfoPage, showNarrationWindowView as showNarrationWindowView
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.gui.sounds.sound_constants import HANGAR_SOUND_SETTINGS as HANGAR_SOUND_SETTINGS
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader, INotificationWindowController as INotificationWindowController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
_logger: Any

# base nao representavel no stub: ViewComponent[...]
class HangarView(IRoutableView):
    _guiLoader: Any
    lsCtrl: Any
    _hangarSpace: Any
    _notificationMgr: Any
    _settingsCore: Any
    _difficultyController: Any
    _COMMON_SOUND_SPACE = HANGAR_SOUND_SETTINGS
    LAYOUT_ID: Any
    __inputManager: Any
    __ammoPanel: Any
    __prevOptimizationEnabled: Any
    __selectedMissionIndex: Any
    __needSlideToNext: Any
    _router: Any
    __allModeVehicleFilter: Any
    __accountVehicleFilter: Any
    __carouselFilter: Any
    __accountStyles: Any
    def __init__(self, layoutId=..., model=...):
        ...
    @property
    def viewModel(self):
        ...
    def getRouterModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _getChildComponents(self):
        ...
    def _initializeRouter(self):
        ...
    def _onClose(self):
        ...
    def __escapeHandler(self):
        ...
    def __onSettingsUpdated(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __setBackground(self, *args, **kwargs):
        ...
    def __fillCore(self):
        ...
    def __onAboutClick(self):
        ...
    def __windowStatusChanged(self, uniqueID, newStatus):
        ...
    def __onViewLoaded(self):
        ...
    def __onNarrationClick(self):
        ...

class HangarWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
