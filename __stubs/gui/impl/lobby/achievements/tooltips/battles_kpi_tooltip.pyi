# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/tooltips/battles_kpi_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.battles_kpi_tooltip_view_model import BattlesKpiTooltipViewModel as BattlesKpiTooltipViewModel
from gui.impl.lobby.achievements.profile_utils import formatPercent as formatPercent, getFormattedValue as getFormattedValue, getNormalizedValue as getNormalizedValue
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from skeletons.gui.shared import IItemsCache as IItemsCache

class BattlesKPITooltip(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __userId: Any
    def __init__(self, userId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
