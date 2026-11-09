# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/missions_progress/comp7_customization_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from shared_utils import first as first
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_customization_quest_progress_model import Comp7CustomizationQuestProgressModel as Comp7CustomizationQuestProgressModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_customization_quests_progress_model import Comp7CustomizationQuestsProgressModel as Comp7CustomizationQuestsProgressModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getComp7ProgressionStyle as getComp7ProgressionStyle
from comp7.gui.shared.missions.packers.events import Comp7WeeklyQuestPacker as Comp7WeeklyQuestPacker
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.impl.backport.backport_tooltip import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events import conditions as conditions
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from comp7.gui.impl.gen.view_models.views.lobby.comp7_battle_results_view_model import Comp7BattleResultsViewModel as Comp7BattleResultsViewModel

# base nao representavel no stub: ViewComponent[...]
class Comp7CustomizationProgressPresenter(IProgressionCategoryPresenter):
    __eventsCache: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __allCommonQuests: Any
    __progress: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, allCommonQuests):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...
    def __createModel(self, quest, pCur, pPrev, isCompleted):
        ...
    def __getEarnedPoints(self, data, pCur, pPrev, isCompleted, totalProgress):
        ...
    def __getCustomizationData(self, questID):
        ...
