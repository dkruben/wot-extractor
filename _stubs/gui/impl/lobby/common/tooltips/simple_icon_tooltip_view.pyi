# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/common/tooltips/simple_icon_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.common.tooltips.simple_icon_tooltip_model import SimpleIconTooltipModel as SimpleIconTooltipModel, HeaderType as HeaderType
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl

class SimpleIconTooltipView(ViewImpl):
    __slots__: tuple
    __header: Any
    __body: Any
    __icon: Any
    __headerType: Any
    def __init__(self, header, body, icon, headerType):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
