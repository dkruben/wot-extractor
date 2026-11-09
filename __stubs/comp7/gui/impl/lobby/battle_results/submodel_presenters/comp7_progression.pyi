# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/comp7_progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from shared_utils import findFirst as findFirst
from comp7.gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as COMP7_TOOLTIPS
from comp7.gui.impl.gen.view_models.views.lobby.comp7_battle_results_view_model import Comp7BattleResultsViewModel as Comp7BattleResultsViewModel, WarningType as WarningType
from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName as SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel as ProgressionItemModel
from comp7.gui.impl.gen.view_models.views.lobby.season_model import SeasonState as SeasonState
from comp7.gui.impl.gen.view_models.views.lobby.year_model import YearState as YearState
from comp7.gui.impl.lobby.battle_results.submodel_presenters.battle_info import isDeserter as isDeserter
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared, comp7_model_helpers as comp7_model_helpers
from comp7.gui.impl.lobby.meta_view import meta_view_helper as meta_view_helper
from comp7_common.comp7_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers as comp7_core_model_helpers
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from frameworks.wulf import ViewModel as ViewModel

class Comp7ProgressionSubPresenter(BattleResultsSubPresenter):
    __comp7Controller: Any
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def __packProgressionData(self, model, battleResults):
        ...
    # decorador original: @dependency.replace_none_kwargs(...)
    def __setQualificationData(self, model, battleResults, comp7Controller=None):
        ...
    def __setRankData(self, model, prevRating, currentRating, ratingDelta, rank):
        ...
    def __setProgressionItems(self, model, rating):
        ...
    def __setUnRankedBattleTypes(self, model):
        ...
