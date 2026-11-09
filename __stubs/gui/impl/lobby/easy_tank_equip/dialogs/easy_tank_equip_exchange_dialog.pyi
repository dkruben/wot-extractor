# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/easy_tank_equip/dialogs/easy_tank_equip_exchange_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.buy_and_exchange_bottom_content_type import BuyAndExchangeBottomContentType as BuyAndExchangeBottomContentType
from gui.impl.gen.view_models.views.lobby.common.dialog_with_exchange import DialogWithExchange as DialogWithExchange
from gui.impl.lobby.dialogs.auxiliary.buy_and_exchange_state_machine import BuyAndExchangeStateEnum as BuyAndExchangeStateEnum
from gui.impl.lobby.dialogs.buy_and_exchange import BuyAndExchange as BuyAndExchange
from gui.impl.lobby.dialogs.contents.exchange_content import ExchangeContentResult as ExchangeContentResult, ExchangeMoneyInfo as ExchangeMoneyInfo
from gui.impl.lobby.easy_tank_equip.dialogs.contents.easy_tank_equip_exchange_content import EasyTankEquipExchangeContent as EasyTankEquipExchangeContent
from gui.shared.money import ZERO_MONEY as ZERO_MONEY, Currency as Currency
from gui.shared.money import Money as Money

class ExchangeToApplyEasyTankEquip(BuyAndExchange):
    __slots__: tuple
    __availableGoldAmount: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _createExchangeContent(self):
        ...
    def _exchangeComplete(self, result):
        ...
    def _stateToContent(self):
        ...
