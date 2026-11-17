# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/ranked_efficiency_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.ranked_efficiency_tooltip_model import RankedEfficiencyTooltipModel as RankedEfficiencyTooltipModel
from gui.impl.gen.view_models.views.lobby.dog_tags.ranked_season_efficiency_model import RankedSeasonEfficiencyModel as RankedSeasonEfficiencyModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.ranked_battles.constants import RankedDossierKeys as RankedDossierKeys, SeasonResultTokenPatterns as SeasonResultTokenPatterns
from helpers import dependency as dependency
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import Array as Array
EFFICIENCY_DIGITS = 2

class RankedEfficiencyTooltip(ViewImpl):
    __rankedController: Any
    __itemsCache: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __addPassedSeasons(self, itemsArr):
        ...
    def __addCurrentSeason(self, itemsArr):
        ...
    def __addFutureSeasons(self, itemsArr):
        ...
    def __checkInLeague(self, seasonID):
        ...
    def __getPassedSeasonEfficiency(self, seasonID):
        ...
    def __getSeasonModel(self, efficiency, state, efficiencyState=...):
        ...
