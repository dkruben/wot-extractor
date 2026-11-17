# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/directive_conversion_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.directive_conversion_tooltip_model import DirectiveConversionTooltipModel as DirectiveConversionTooltipModel
from gui.impl.lobby.crew.utils import BOOSTER_ICON_MAPPING as BOOSTER_ICON_MAPPING
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache

class DirectiveConversionTooltip(ViewImpl):
    _itemsCache: Any
    __slots__: tuple
    __oldDirective: Any
    __newDirective: Any
    __amount: Any
    def __init__(self, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
