# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/refill_shells.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.fitting_types import FittingTypes as FittingTypes
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.confirm_bottom_content_type import ConfirmBottomContentType as ConfirmBottomContentType
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.refill_shells_model import RefillShellsModel as RefillShellsModel
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContentResult as ExchangeContentResult
from gui.impl.lobby.dialogs.contents.multiple_items_content import MultipleItemsContent as MultipleItemsContent
from gui.impl.lobby.tank_setup.dialogs.bottom_content.bottom_contents import PriceBottomContent as PriceBottomContent
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO as ITEM_PRICE_ZERO
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice

class RefillShells(BuyAndExchange):
    __slots__: tuple
    __price: Any
    _buyContent: Any
    _mainContent: Any
    __shells: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def _exchangeComplete(self, result):
        ...
    def _stateToContent(self):
        ...
    def _buyNotRequiredAccept(self):
        ...

class ExitFromShellsConfirm(RefillShells):
    __slots__: tuple
    __rollBack: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getAdditionalData(self):
        ...
    def _onCancelClicked(self):
        ...
