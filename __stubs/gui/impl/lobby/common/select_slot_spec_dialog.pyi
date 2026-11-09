# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/select_slot_spec_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from wg_async import wg_async as wg_async, wg_await as wg_await
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.dialogs.dialogs import showSingleDialogWithResultData as showSingleDialogWithResultData
from gui.impl.gen.view_models.views.lobby.common.buy_and_exchange_bottom_content_type import BuyAndExchangeBottomContentType as BuyAndExchangeBottomContentType
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_content_model import SelectSlotSpecDialogContentModel as SelectSlotSpecDialogContentModel
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_model import SelectSlotSpecDialogModel as SelectSlotSpecDialogModel
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_slot_model import SelectSlotSpecDialogSlotModel as SelectSlotSpecDialogSlotModel
from gui.impl.gen.view_models.views.lobby.common.select_slot_spec_dialog_spec_model import SelectSlotSpecDialogSpecModel as SelectSlotSpecDialogSpecModel
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder as PriceModelBuilder
from gui.impl.gen import R as R
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.money import Money as Money
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from frameworks.wulf import Window as Window
TContentModel = SelectSlotSpecDialogContentModel

# base nao representavel no stub: BuyAndExchange[...]
class SelectSlotSpecDialog:
    __slots__: tuple
    __itemsCache: Any
    _price: Any
    _vehicle: Any
    _slotIdx: Any
    _freeChange: Any
    _mainContent: Any
    def __init__(self, vehicle, slotIdx=None):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getAdditionalData(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onInventoryResync(self, reason, diff):
        ...
    def _buyNotRequiredAccept(self):
        ...
    def _stateToContent(self):
        ...
    def _onAcceptClicked(self):
        ...
    def _skipNeedExchangeState(self):
        ...

# base nao representavel no stub: BaseSubModelView[...]
class SelectSlotSpecDialogMainContent:
    __slots__: tuple
    _vehicle: Any
    _slotIdx: Any
    _startIdx: Any
    def __init__(self, vehicle, viewModel, slotIdx=None):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def setSlots(self, model, optDevices):
        ...
    def setAvailableSpecs(self, model, optDevices):
        ...
    def getSelectedSlot(self):
        ...
    @staticmethod
    def _fillSpecsModel(model, categories):
        ...
    def __setSelectedSpecIdx(self, model, slotData):
        ...

# decorador original: @wg_async
def showDialog(vehicle, parent=None):
    ...
