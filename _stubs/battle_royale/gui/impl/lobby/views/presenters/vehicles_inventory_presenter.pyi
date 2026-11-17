# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/presenters/vehicles_inventory_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import typing as typing
from future.utils import viewvalues as viewvalues
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from battle_royale.gui.impl.gen.view_models.views.lobby.views.vehicles_inventory_model import VehiclesInventoryModel as VehiclesInventoryModel
from battle_royale.gui.impl.lobby.tooltips.vehicle_tooltip_view import VehicleTooltipView as VehicleTooltipView
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IRentalsController as IRentalsController
from skeletons.gui.shared import IItemsCache as IItemsCache
from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType as CoinType
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.requesters import RequestCriteria as RequestCriteria

# base nao representavel no stub: ViewComponent[...]
class BattleRoyaleVehiclesInventoryPresenter:
    __itemsCache: Any
    __rentalsCtrl: Any
    __customizationService: Any
    __brController: Any
    __vehiclesComponent: Any
    __vehiclesCriteria: Any
    def __init__(self, vehiclesComponent, vehiclesCriteria):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _toModelItem(self, vehicle):
        ...
    @staticmethod
    def __getVehicleStatus(vehicle):
        ...
    def __onVehicleClientStateChanged(self, vehicles=None):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __onVehicleChanged(self):
        ...
    def __setItem(self, model, vehicle):
        ...
    def __setupVehicles(self, model, vehicles):
        ...
    def __onUpdateVehicles(self, diff):
        ...
    def __onSelectVehicle(self, vehId):
        ...
    def __updateModel(self):
        ...
    def __setupCurrentVehicle(self, model):
        ...
