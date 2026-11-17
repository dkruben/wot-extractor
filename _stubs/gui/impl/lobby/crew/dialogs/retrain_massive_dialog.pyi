# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/retrain_massive_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits, getPurchaseMoneyState as getPurchaseMoneyState, MoneyForPurchase as MoneyForPurchase
from gui.impl.auxiliary.tankman_operations import ITEM_PRICE_FREE as ITEM_PRICE_FREE, packRetrainTankman as packRetrainTankman
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.dialogs.widgets.single_price import SinglePriceWidget as SinglePriceWidget
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencySize as CurrencySize
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.dialog_tankman_model import DialogTankmanModel as DialogTankmanModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.retrain_massive_dialog_model import RetrainMassiveDialogModel as RetrainMassiveDialogModel
from gui.impl.lobby.crew.crew_helpers.model_setters import ifWGMAvailableButtonUpdate as ifWGMAvailableButtonUpdate
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.dialogs.price_cards_content.retrain_massive_price_list import RetrainMassivePriceList as RetrainMassivePriceList
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Tankman import Tankman as Tankman
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.items_actions import factory as factory
from gui.shared.money import Money as Money
from gui.shop import showBuyGoldForCrew as showBuyGoldForCrew
from helpers import dependency as dependency
from helpers_common import getFinalRetrainCost as getFinalRetrainCost, getRetrainCost as getRetrainCost
from items.tankmen import TankmanDescr as TankmanDescr
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.impl.lobby.crew.crew_helpers.tankman_helpers import getPriceDiscountMassRetrain as getPriceDiscountMassRetrain
from skeletons.gui.shared.utils.requesters import IShopRequester as IShopRequester
_LOC = R.strings.dialogs.retrain

class RetrainMassiveDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: Any
    VIEW_MODEL = RetrainMassiveDialogModel
    _itemsCache: Any
    _appLoader: Any
    _tankmen: Any
    _vehicle: Any
    _selectedTankmenIds: Any
    _priceListContent: Any
    _toolTipMgr: Any
    _retrainCost: Any
    def __init__(self, tankmenIds, vehicleCD, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _onConsumeWalletUpdate(self, *_):
        ...
    def _onPriceChange(self, index=None):
        ...
    def _onVehiclesInventoryUpdate(self, diff):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initModel(self):
        ...
    def _updateViewModel(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _updateTankmen(self, vm):
        ...
    def _updatePrice(self, vm, idx):
        ...
    def _setResult(self, result):
        ...
    def _retrainTankmen(self):
        ...
    def __getTankmanFinalPrice(self, tankman, idx):
        ...
