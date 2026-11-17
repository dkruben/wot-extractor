# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/points_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from last_stand.gui.impl.gen.view_models.views.lobby.tooltips.points_tooltip_view_model import PointsTooltipViewModel as PointsTooltipViewModel
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand.skeletons.ls_shop_controller import ILSShopController as ILSShopController
from helpers import dependency as dependency
from shared_utils import first as first

class PointsTooltipView(ViewImpl):
    __slots__: tuple
    lsCtrl: Any
    lsShopCtrl: Any
    __isPostBattle: Any
    __ctx: Any
    def __init__(self, isPostBattle, ctx=None, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
