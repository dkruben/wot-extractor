# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/prices_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.dialog_prices_content_model import DialogPricesContentModel as DialogPricesContentModel
from gui.impl.lobby.dialogs.dialog_prices_tooltip import DialogPricesTooltip as DialogPricesTooltip
from gui.impl.pub.dialog_window import DialogContent as DialogContent

class DialogPricesContent(DialogContent):
    __slots__: tuple
    __valueMainCost: Any
    __iconMainCost: Any
    __labelMainCost: Any
    __valueAdditionalCost: Any
    __iconAdditionalCost: Any
    __labelAdditionalCost: Any
    __totalCost: Any
    __labelTotalCost: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def setData(self, valueMainCost, iconMainCost, labelMainCost, valueAdditionalCost, iconAdditionalCost, labelAdditionalCost, totalCost, labelTotalCost):
        ...
