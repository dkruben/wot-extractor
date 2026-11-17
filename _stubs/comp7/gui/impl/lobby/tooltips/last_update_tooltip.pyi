# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/last_update_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.last_update_tooltip_model import LastUpdateTooltipModel as LastUpdateTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class LastUpdateTooltip(ViewImpl):
    __slots__: tuple
    __comp7Controller: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, description, updateTime=None, *args, **kwargs):
        ...
