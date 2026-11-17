# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/dialogs/retrain_single_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import BigWorld as BigWorld
from typing import Any as Any, Optional as Optional
import SoundGroups as SoundGroups
from .base_crew_dialog_template_view import BaseCrewDialogTemplateView as BaseCrewDialogTemplateView
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.customization.shared import getPurchaseGoldForCredits as getPurchaseGoldForCredits, getPurchaseMoneyState as getPurchaseMoneyState, MoneyForPurchase as MoneyForPurchase
from gui.impl.auxiliary.tankman_operations import packSkills as packSkills, packBaseTankman as packBaseTankman
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.dialogs.dialog_template_button import CancelButton as CancelButton, ConfirmButton as ConfirmButton
from gui.impl.dialogs.sub_views.top_right.money_balance import MoneyBalance as MoneyBalance
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.views.dialogs.default_dialog_place_holders import DefaultDialogPlaceHolders as DefaultDialogPlaceHolders
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import ButtonType as ButtonType
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.dialogs.retrain_role_model import RetrainRoleModel as RetrainRoleModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.retrain_single_dialog_model import RetrainSingleDialogModel as RetrainSingleDialogModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.role_change_model import DisableState as DisableState
from gui.impl.lobby.crew.crew_helpers.model_setters import ifWGMAvailableButtonUpdate as ifWGMAvailableButtonUpdate
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.impl.lobby.crew.dialogs.price_cards_content.retrain_single_price_list import RetrainSinglePriceList as RetrainSinglePriceList
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.Tankman import Tankman as Tankman, NO_SLOT as NO_SLOT
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle, VEHICLE_TAGS as VEHICLE_TAGS
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.gui_items.items_actions import factory as factory
from gui.shop import showBuyGoldForCrew as showBuyGoldForCrew
from helpers import dependency as dependency
from items.tankmen import TankmanDescr as TankmanDescr
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
_LOC = R.strings.dialogs.retrain

class RetrainSingleDialog(BaseCrewDialogTemplateView):
    __slots__: tuple
    LAYOUT_ID: _Any
    VIEW_MODEL = RetrainSingleDialogModel
    _itemsCache: _Any
    _appLoader: _Any
    _tankman: _Any
    _vehicle: _Any
    _isChangeRoleVisible: _Any
    _beforeActions: _Any
    _toolTipMgr: _Any
    _nativeTankmanRoles: _Any
    _roles: _Any
    _originalTargetSlotIdx: _Any
    _targetSlotIdx: _Any
    _priceListContent: _Any
    _lastChangeRoleChecked: _Any
    _targetRole: _Any
    _isRoleChangeForced: _Any
    def __init__(self, tankmanId, vehicleCD, targetRole=None, targetSlotIdx=None, isChangeRoleVisible=False, beforeActions=None, **kwargs):
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
    def _onRoleChanged(self):
        ...
    def _onRoleSelected(self, args):
        ...
    def _onPriceChange(self, index=None):
        ...
    def _onVehiclesInventoryUpdate(self, diff):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getWarning(self):
        ...
    def _initModel(self):
        ...
    def _updateTankmanAfter(self, vm):
        ...
    def _getRoleChangeDisableState(self):
        ...
    def _updateRoles(self, vm):
        ...
    def _setResult(self, result):
        ...
    def _retrainTankmen(self):
        ...
    @staticmethod
    def __isVehicleReady(veh):
        ...
    @staticmethod
    def __getSlotByVehicleRole(requestRole, veh):
        ...
    def __isRoleChanging(self):
        ...
    def __isRoleTaken(self, role):
        ...
    def __countSlotsForRole(self, role):
        ...
    def __hasIrrelevantPerk(self):
        ...
    def __getTankmanWithTargetRole(self):
        ...
