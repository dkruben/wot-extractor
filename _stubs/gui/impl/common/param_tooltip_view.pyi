# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/param_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.param_tooltip_model import ParamTooltipModel as ParamTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl

class ParamTooltipView(ViewImpl):
    _tooltipType: Any
    _params: Any
    def __init__(self, tooltipType, params, resId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
