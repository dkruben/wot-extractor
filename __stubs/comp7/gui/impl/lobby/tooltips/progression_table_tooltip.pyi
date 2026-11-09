# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/progression_table_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel as ProgressionItemModel
from comp7.gui.impl.gen.view_models.views.lobby.tooltips.progression_table_tooltip_model import ProgressionTableTooltipModel as ProgressionTableTooltipModel
from comp7.gui.impl.lobby.comp7_helpers import comp7_model_helpers as comp7_model_helpers, comp7_shared as comp7_shared
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import getSeasonNameEnum as getSeasonNameEnum
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.lobby.meta_view import meta_view_helper as meta_view_helper
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class ProgressionTableTooltip(ViewImpl):
    __slots__: tuple
    __comp7Controller: Any
    def __init__(self, layoutID=...):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def __updateTooltipProgressionData(self, *_):
        ...
    def __setupRanksTable(self, viewModel):
        ...
