# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/tooltips/kpi_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.achievements.achievements_constants import KPITypes as KPITypes
from gui.impl.lobby.achievements.profile_utils import getFormattedValue as getFormattedValue
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.kpi_tooltip_view_model import KpiTooltipViewModel as KpiTooltipViewModel
from skeletons.gui.shared import IItemsCache as IItemsCache
KPI_STATTS: dict

class KPITooltip(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __kpiType: Any
    __userId: Any
    def __init__(self, kpiType, userId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __getStats(self, kpiType):
        ...
    def __getVehicleInfo(self, intCD):
        ...
