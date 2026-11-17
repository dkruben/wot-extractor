# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/discount_info_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_discount_model import DiscountType as DiscountType, ShowFormat as ShowFormat
from gui.impl.common.components_presenter import BaseSubModelViewWithToolTips as BaseSubModelViewWithToolTips
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider

class ExchangeDiscountView(BaseSubModelViewWithToolTips):
    __exchangeRatesProvider: Any
    __exchangeType: Any
    def __init__(self, exchangeType, *args, **kwargs):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def getViewModel(self):
        ...
    @property
    def _exchangeRate(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _getDiscountInfo(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updateDiscountInfo(self, model=None):
        ...
    def __setDiscountInfo(self, model):
        ...
