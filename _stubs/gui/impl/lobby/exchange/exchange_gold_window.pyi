# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/exchange_gold_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.shared.utils.decorators import adisp_process as adisp_process
from exchange.personal_discounts_constants import EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_gold_model import ExchangeRateGoldModel as ExchangeRateGoldModel
from gui.impl.lobby.exchange.base_exchange_window import BaseExchangeWindow as BaseExchangeWindow
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger as GoldToCreditsExchanger
_logger: Any

class ExchangeGoldView(BaseExchangeWindow):
    __slots__: tuple
    def __init__(self, layoutID, ctx=None, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @adisp_process(...)
    def _onExchange(self, data):
        ...
