# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/single_price_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel as DialogTemplateGenericTooltipViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel as CurrencyViewModel

class SinglePriceViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def cost(self):
        ...
    @staticmethod
    def getCostType():
        ...
    @property
    def tooltip(self):
        ...
    @staticmethod
    def getTooltipType():
        ...
    def getText(self):
        ...
    def setText(self, value):
        ...
    def _initialize(self):
        ...
