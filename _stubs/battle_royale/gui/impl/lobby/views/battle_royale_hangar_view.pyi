# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_royale_hangar_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle, g_currentVehicle as g_currentVehicle
from battle_royale.gui.impl.lobby.views.presenters.battle_royale_event_presenter import BattleRoyaleEventPresenter as BattleRoyaleEventPresenter
from battle_royale.gui.Scaleform.daapi.view.lobby.hangar.carousel.filter import RoyaleCarouselFilter as RoyaleCarouselFilter
from battle_royale.gui.impl.lobby.views.user_missions.hangar_widget.presenters.user_missions_presenter import BattleRoyaleUserMissionsPresenter as BattleRoyaleUserMissionsPresenter
from battle_royale.gui.impl.lobby.views.presenters.vehicle_filters_presenter import BattleRoyaleVehicleFiltersPresenter as BattleRoyaleVehicleFiltersPresenter
from battle_royale.gui.impl.lobby.views.presenters.vehicles_inventory_presenter import BattleRoyaleVehiclesInventoryPresenter as BattleRoyaleVehiclesInventoryPresenter
from battle_royale.gui.impl.lobby.views.presenters.battle_type_selector_presenter import BattleTypeSelectorPresenter as BattleTypeSelectorPresenter
from battle_royale.gui.impl.lobby.views.presenters.alert_message_presenter import AlertMessagePresenter as AlertMessagePresenter
from battle_royale.gui.impl.lobby.views.presenters.header_presenter import HeaderPresenter as HeaderPresenter
from battle_royale.gui.impl.lobby.views.presenters.loadout_panel_presenter.loadout_panel_presenter import LoadoutContainerPresenter as LoadoutContainerPresenter
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.app_loader import app_getter as app_getter
from frameworks.wulf import WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.pub import WindowImpl as WindowImpl
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showLobbyMenu as showLobbyMenu
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel as RouterModel
from gui.impl.lobby.hangar.base.account_styles import AccountStyles as AccountStyles
from gui.impl.lobby.hangar.base.vehicles_filter_component import VehiclesFilterComponent as VehiclesFilterComponent
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.impl.lobby.hangar.presenters.hero_tank_presenter import HeroTankPresenter as HeroTankPresenter
from gui.impl.lobby.hangar.presenters.space_interaction_presenter import SpaceInteractionPresenter as SpaceInteractionPresenter
from gui.impl.lobby.hangar.presenters.utils import getMenuItems as getMenuItems
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from hangar_selectable_objects import HangarSelectableLogic as HangarSelectableLogic
from gui.impl.lobby.hangar.presenters.lootbox_entry_point_presenter import LootboxEntryPointPresenter as LootboxEntryPointPresenter
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.impl.pub.view_impl import TViewModel as TViewModel
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria
from hangar_selectable_objects.interfaces import ISelectableLogic as ISelectableLogic
_logger: Any

class BattleRoyaleHangarWindow(WindowImpl):
    __battleRoyale: Any
    __BACKGROUND_ALPHA = 0.0
    __background_alpha__: Any
    def __init__(self, layer, **kwargs):
        ...
    def _onReady(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleHangarView(IRoutableView):
    __routerObserver: Any
    __inputManager: Any
    __vehicleFilter: Any
    __carouselFilter: Any
    __accountStyles: Any
    def __init__(self, layoutId, model=...):
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
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onShown(self):
        ...
    # decorador original: @app_getter
    def __app(self):
        ...
    def __createSelectableLogic(self):
        ...
    def __escapeHandler(self):
        ...
    @staticmethod
    def __battleRoyalVehicleCriteria():
        ...
