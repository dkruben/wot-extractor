# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/dialogs/need_repair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.need_repair_bottom_content_type import NeedRepairBottomContentType as NeedRepairBottomContentType
from gui.impl.gen.view_models.views.lobby.tank_setup.dialogs.need_repair_model import NeedRepairModel as NeedRepairModel
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContentResult as ExchangeContentResult
from gui.impl.lobby.tank_setup.dialogs.bottom_content.bottom_contents import NeedRepairBottomContent as NeedRepairBottomContent
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.shared.gui_items.gui_item_economics import Money as Money
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class NeedRepair(BuyAndExchange):
    __slots__: tuple
    __vehicle: Any
    _buyContent: Any
    _mainContent: Any
    __repairClazz: Any
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
    def _stateToContent(self):
        ...
    def _exchangeComplete(self, result):
        ...
    def _onAccept(self):
        ...
    def _onCancel(self):
        ...
    def __calculateRepairPercentage(self):
        ...
    def __getPrice(self):
        ...
