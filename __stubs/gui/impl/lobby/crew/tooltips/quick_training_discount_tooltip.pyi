# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/quick_training_discount_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.quick_training_discount_tooltip_model import QuickTrainingDiscountTooltipModel as QuickTrainingDiscountTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class QuickTrainingDiscountTooltip(ViewImpl):
    __slots__: tuple
    _oldFreeXpBase: Any
    _newFreeXpBase: Any
    _oldXpExchange: Any
    _newXpExchange: Any
    def __init__(self, oldXpExchange, newXpExchange, oldFreeXpBase=1, newFreeXpBase=1):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
