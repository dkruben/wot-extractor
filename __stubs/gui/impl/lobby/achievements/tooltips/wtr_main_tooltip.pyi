# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/tooltips/wtr_main_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.gen.view_models.views.lobby.achievements.rank_model import RankModel as RankModel
from gui.impl.gen.view_models.views.lobby.achievements.tooltips.wtr_main_tooltip_view_model import WtrMainTooltipViewModel as WtrMainTooltipViewModel
from gui.impl.lobby.achievements.profile_utils import getNormalizedValue as getNormalizedValue
from achievements20.WTRStageChecker import WTRStageChecker as WTRStageChecker
from gui.impl.gen import R as R
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class WTRMainTooltip(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    __userId: Any
    def __init__(self, userId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __fillRanks(self, model, stages):
        ...
