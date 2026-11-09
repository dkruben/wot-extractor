# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/comp7_light_hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from comp7_light.gui.Scaleform.genConsts.COMP7_LIGHT_HANGAR_ALIASES import COMP7_LIGHT_HANGAR_ALIASES as COMP7_LIGHT_HANGAR_ALIASES
from account_helpers.AccountSettings import HANGAR_VIEW_SETTINGS as HANGAR_VIEW_SETTINGS, HANGAR_KEY_BINDINGS as HANGAR_KEY_BINDINGS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.hangar.hangar_settings_model import HangarSettingsModel as HangarSettingsModel
from gui.impl.gen.view_models.views.lobby.hangar.key_bindings_model import KeyBindingsModel as KeyBindingsModel
from gui.impl.lobby.common.presenters.settings_presenter import SettingsPresenter as SettingsPresenter
from gui.impl.lobby.easy_tank_equip.easy_tank_equip_presenter import EasyTankEquipPresenter as EasyTankEquipPresenter
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from shared_utils import nextTick as nextTick
from gui.impl.lobby.hangar.base.blur import RandomHangarBlur as RandomHangarBlur
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from comp7_light.gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_filter import Comp7LightCarouselFilter as Comp7LightCarouselFilter
from comp7_light.gui.impl.lobby.alert_message_presenter import AlertMessagePresenter as AlertMessagePresenter
from comp7_light.gui.impl.lobby.hangar.presenters.comp7_light_loadout_presenter import Comp7LightLoadoutPresenter as Comp7LightLoadoutPresenter
from comp7_light.gui.impl.lobby.role_skill_slot_presenter import Comp7LightRoleSkillSlotPresenter as Comp7LightRoleSkillSlotPresenter
from comp7_light.gui.impl.lobby.season_modifier_presenter import SeasonModifierPresenter as SeasonModifierPresenter
from comp7_light.gui.impl.lobby.user_missions_presenter import Comp7LightUserMissionsPresenter as Comp7LightUserMissionsPresenter
from frameworks.wulf import WindowFlags as WindowFlags
from gui.app_loader import app_getter as app_getter
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.impl.lobby.hangar.presenters.crew_presenter import CrewPresenter as CrewPresenter
from gui.impl.lobby.hangar.presenters.hangar_vehicle_params_presenter import HangarVehicleParamsPresenter as HangarVehicleParamsPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from comp7_light.gui.impl.lobby.hangar.presenters.comp7_light_optional_devices_assistant_presenter import Comp7LightOptionalDevicesAssistantPresenter as Comp7LightOptionalDevicesAssistantPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from gui.impl.lobby.hangar.presenters.teaser_presenter import TeaserPresenter as TeaserPresenter
from gui.impl.lobby.hangar.presenters.utils import getMenuItems as getMenuItems
from comp7_core.gui.impl.lobby.hangar.presenters.comp7_core_vehicle_filters_presenter import Comp7CoreVehicleFiltersDataProvider as Comp7CoreVehicleFiltersDataProvider
from gui.impl.lobby.hangar.presenters.vehicle_inventory_presenter import VehicleInventoryPresenter as VehicleInventoryPresenter
from gui.impl.lobby.hangar.presenters.vehicle_menu_presenter import VehicleMenuPresenter as VehicleMenuPresenter
from gui.impl.lobby.hangar.presenters.vehicle_statistics_presenter import VehiclesStatisticsPresenter as VehiclesStatisticsPresenter
from comp7_light.gui.impl.lobby.hangar.presenters.comp7_light_vehicles_info_presenter import Comp7LightVehiclesInfoPresenter as Comp7LightVehiclesInfoPresenter
from gui.impl.lobby.hangar.random.random_hangar import RANDOM_HANGAR_SOUND_SPACE as RANDOM_HANGAR_SOUND_SPACE
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from helpers import dependency as dependency
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from gui.impl.pub.view_impl import TViewModel as TViewModel
from hangar_selectable_objects.interfaces import ISelectableLogic as ISelectableLogic
_logger: Any

class Comp7LightHangarWindow(WindowImpl):
    _statsCollector: Any
    def __init__(self, layer, *_, **__):
        ...
    def _onReady(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class Comp7LightHangar(IRoutableView):
    _COMMON_SOUND_SPACE = RANDOM_HANGAR_SOUND_SPACE
    __inputManager: Any
    __routerObserver: Any
    __vehicleFilter: Any
    __carouselFilter: Any
    __accountStyles: Any
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
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onShown(self):
        ...
    def _initialize(self, *args, **kwargs):
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

def _createComp7LightCriteria():
    ...
