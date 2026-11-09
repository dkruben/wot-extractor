# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/tooltips/extended_text_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.extended_text_tooltip_model import ExtendedTextTooltipModel as ExtendedTextTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class ExtendedTextTooltip(ViewImpl):
    __slots__: tuple
    __text: Any
    __stringifyKwargs: Any
    def __init__(self, text, stringifyKwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
