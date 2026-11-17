# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import typing as typing
from functools import partial as partial
from collections import namedtuple as namedtuple, OrderedDict as OrderedDict
from future.utils import itervalues as itervalues
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import VIEWED_MODULES_SECTION as VIEWED_MODULES_SECTION
from armor_inspector_common.schemas import armorInspectorConfigSchema as armorInspectorConfigSchema
from frameworks.wulf import WindowFlags as WindowFlags
from frameworks_common.state_machine import StateIdsObserver as StateIdsObserver
from Event import Event as Event
from collector_vehicle import CollectorVehicleConsts as CollectorVehicleConsts
from gui import g_tankActiveCamouflage as g_tankActiveCamouflage
from gui.shared.events import VehicleBuyEvent as VehicleBuyEvent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.comparison_model import ComparisonModel as ComparisonModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.menu_item_model import MenuItemModel as MenuItemModel
from gui.impl.lobby.vehicle_hub.sub_presenters.research_purchase_sub_presenter import ResearchPurchaseSubPresenter as ResearchPurchaseSubPresenter
from gui.impl.lobby.vehicle_hub.vehicle_hub_characteristics_presenter import VehicleHubCharacteristicsPresenter as VehicleHubCharacteristicsPresenter
from gui.impl.lobby.vehicle_hub.vehicle_hub_wallet_presenter import VehicleHubWalletPresenter as VehicleHubWalletPresenter
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.vehicle_hub_view_model import VehicleHubViewModel as VehicleHubViewModel
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.gen import R as R
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.lobby_state_machine.routable_view import IRoutableView as IRoutableView
from gui.impl.lobby.vehicle_hub.sub_presenters.presenters_map import PresentersMap as PresentersMap, SubModelInfo as SubModelInfo
from gui.shared.utils.module_upd_available_helper import getVehicleResearchInfo as getVehicleResearchInfo
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import RS_PDATA_KEY as RS_PDATA_KEY
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket, IRentalsController as IRentalsController
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict
_REQUIRED_TAGS: list
VehicleHubCtx: Any

class _VehicleHubStatesObserver(StateIdsObserver):
    __itemsCache: Any
    __vhCtx: Any
    onNavigationChanged: Any
    def __init__(self, vhCtx):
        ...
    def onEnterState(self, state, event):
        ...
    def __setupPreviewTank(self, vhCtx):
        ...

class VehicleHubMainView(ViewComponent, IRoutableView):
    __comparisonBasket: Any
    __itemsCache: Any
    __rentals: Any
    __contentPresentersMap: Any
    __activeTab: Any
    __vhCtx: Any
    __lsmObserver: Any
    __researchPurchase: Any
    __router: Any
    def __init__(self, ctx, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def currentPresenter(self):
        ...
    @property
    def vehicleCtx(self):
        ...
    def getRouterModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def stateExited(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getChildComponents(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _getListeners(self):
        ...
    def _finalize(self):
        ...
    @property
    def __vehicle(self):
        ...
    def __getUnviewedResearchedModulesCount(self):
        ...
    def __getVehSkillTreeVisibility(self):
        ...
    def __getMenuItems(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setCommonInfo(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateComparisonInfo(self, model=None):
        ...
    def __onClientUpdate(self, diff, _):
        ...
    def __onTradeOffSelectedChanged(self, _=None):
        ...
    def __onVehicleBecomeElite(self, elite):
        ...
    def __onAccountSettingsChanging(self, key, _):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateMenuItems(self, model=None):
        ...
    def __onAddToComparison(self):
        ...
    def __onVehCompareBasketChanged(self, _):
        ...
    def __onNavigationChanged(self, state, event):
        ...
    def __onInventoryUpdate(self, invDiff):
        ...
    def __onVehsLockUpdate(self, _=None):
        ...
    def __onRentChange(self, vehicles):
        ...
    def __onVehicleHubCtxChanged(self, vhCtx):
        ...
    def __switchSubView(self, tabName, vhCtx=None):
        ...
    def __registerSubModels(self):
        ...
    def __clearAllSubPresenters(self):
        ...
    @staticmethod
    def __onMoveSpace(args=None):
        ...
    @staticmethod
    def __onMouseOver3dScene(args):
        ...
    @staticmethod
    def __onResize(args):
        ...
    @property
    def __disabledTabs(self):
        ...

class VehicleHubWindow(WindowImpl):
    def __init__(self, layer, ctx, **kwargs):
        ...
