# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_inventory_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from account_helpers.telecom_rentals import TelecomRentals as TelecomRentals
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicles_inventory_model import VehiclesInventoryModel as VehiclesInventoryModel
from gui.impl.lobby.tooltips.carousel_vehicle_tooltip import CarouselVehicleTooltipView as CarouselVehicleTooltipView
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.battle_pass.battle_pass_helpers import getSupportedCurrentArenaBonusType as getSupportedCurrentArenaBonusType
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.items_actions import factory as ActionsFactory
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from telecom_rentals_common import ROSTER_EXPIRATION_TOKEN_NAME as ROSTER_EXPIRATION_TOKEN_NAME, PARTNERSHIP_TOKEN_NAME as PARTNERSHIP_TOKEN_NAME
from gui.impl.lobby.hangar.base.hangar_interfaces import IVehicleFilter as IVehicleFilter

# base nao representavel no stub: ViewComponent[...]
class VehicleInventoryPresenter(IGlobalListener):
    _itemsCache: Any
    __battlePass: Any
    __lobbyContext: Any
    __vehiclesFilter: Any
    __telecomRentals: Any
    def __init__(self, vehiclesFilter):
        ...
    def onPrbEntitySwitched(self, _=None):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getIsBpEntityValid(self):
        ...
    def _getCallbacks(self):
        ...
    def _autoSelectVehicle(self):
        ...
    def __onVehicleChanged(self):
        ...
    def __onBattlePassSettingsChanged(self, *_):
        ...
    def __onSelectVehicle(self, vehId):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __onGoBuyVehicle(self):
        ...
    def __onBuySlot(self):
        ...
    def __onGoRecoverVehicle(self):
        ...
    def __getCurrentArenaBonusType(self):
        ...
    def __updateModel(self):
        ...
    def __invalidateSelectedVehicle(self):
        ...
    def __updateSelectedModel(self):
        ...
    def __getTelecomRentStatus(self):
        ...
    def __isTelecomRentalsEnabled(self):
        ...
    def __onTelecomPendingRentChanged(self, vehCD):
        ...
    def __onTokensUpdated(self, diff):
        ...
