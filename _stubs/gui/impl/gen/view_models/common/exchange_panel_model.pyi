# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/exchange_panel_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.exchange_rate_model import ExchangeRateModel as ExchangeRateModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel

class ExchangePanelModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def fromItem(self):
        ...
    @staticmethod
    def getFromItemType():
        ...
    @property
    def toItem(self):
        ...
    @staticmethod
    def getToItemType():
        ...
    @property
    def exchangeRate(self):
        ...
    @staticmethod
    def getExchangeRateType():
        ...
    def _initialize(self):
        ...
