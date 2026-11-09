# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/rank_compatibility_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Optional as Optional
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.rank_compatibility_tooltip_model import RankCompatibilityTooltipModel as RankCompatibilityTooltipModel
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class RankCompatibilityTooltip(ViewImpl):
    __slots__: tuple
    __comp7Controller: Any
    __squadSize: Any
    __rankRangeRestriction: Any
    def __init__(self, squadSize, rankRngRestr, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
