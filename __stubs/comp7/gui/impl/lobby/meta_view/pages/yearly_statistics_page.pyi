# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/yearly_statistics_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import findFirst as findFirst
from comp7.gui.impl.gen.view_models.views.lobby.constants import Constants as Constants
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_statistics_model import YearlyStatisticsModel as YearlyStatisticsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_statistics_season_model import YearlyStatisticsSeasonModel as YearlyStatisticsSeasonModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared
from comp7.gui.impl.lobby.comp7_helpers.comp7_model_helpers import SEASONS_NUMBERS_BY_NAME as SEASONS_NUMBERS_BY_NAME
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.shared.event_dispatcher import showComp7SeasonStatisticsScreen as showComp7SeasonStatisticsScreen
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from comp7_common_const import seasonPointsCodeBySeasonNumber as seasonPointsCodeBySeasonNumber
from comp7_core.gui.impl.lobby.comp7_core_helpers.comp7_core_model_helpers import setSeasonInfo as setSeasonInfo
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class YearlyStatisticsPage(PageSubModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __comp7Controller: Any
    @property
    def pageId(self):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onRatingUpdated(self, *_):
        ...
    def __onDossierReceived(self, *_):
        ...
    def __updateSeasonModels(self, *_):
        ...
    def __invalidateCurrentSeasonCard(self):
        ...
    def __fillSeasonCard(self, seasonCard, season):
        ...
    def __setPlayerStatistics(self, seasonStatisticsModel, season):
        ...
    @staticmethod
    def __getRatingValue(hasRankReceived, value):
        ...
    @staticmethod
    def __getBattlesCountValue(season, value):
        ...
    def __isSeasonPointsReceived(self, seasonNumber):
        ...
    @staticmethod
    def __onGoToSeasonStatistics(params):
        ...
