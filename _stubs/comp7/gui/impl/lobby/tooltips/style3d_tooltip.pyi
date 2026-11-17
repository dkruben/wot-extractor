# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/style3d_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.style3d_tooltip_model import Style3dTooltipModel as Style3dTooltipModel
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.customization.shared import getSuitableText as getSuitableText
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService

class Style3dTooltip(ViewImpl):
    __slots__: tuple
    __c11nService: Any
    def __init__(self, styleId, vehiclesStr=None, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, styleId, vehiclesStr, **kwargs):
        ...
