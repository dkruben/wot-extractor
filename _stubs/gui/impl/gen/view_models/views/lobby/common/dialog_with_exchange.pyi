# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/dialog_with_exchange.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.impl.gen.view_models.common.exchange_panel_model import ExchangePanelModel as ExchangePanelModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel as FullScreenDialogWindowModel

class DialogWithExchange(FullScreenDialogWindowModel):
    __slots__: tuple
    def __init__(self, properties=15, commands=3):
        ...
    @property
    def exchangePanel(self):
        ...
    @staticmethod
    def getExchangePanelType():
        ...
    @property
    def lacksMoney(self):
        ...
    @staticmethod
    def getLacksMoneyType():
        ...
    def getBottomContentType(self):
        ...
    def setBottomContentType(self, value):
        ...
    def getExchangeState(self):
        ...
    def setExchangeState(self, value):
        ...
    def _initialize(self):
        ...
