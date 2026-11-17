# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/missions_progress/comp7_weekly_missions_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from shared_utils import first as first
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_weekly_quest_progress_model import Comp7WeeklyQuestProgressModel as Comp7WeeklyQuestProgressModel
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_weekly_quests_progress_model import Comp7WeeklyQuestsProgressModel as Comp7WeeklyQuestsProgressModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import getWeeklyPBSBonusPacker as getWeeklyPBSBonusPacker, packQuestBonuses as packQuestBonuses
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isComp7Quest as isComp7Quest, getComp7QuestType as getComp7QuestType, getComp7WeeklyQuestsCompleteToken as getComp7WeeklyQuestsCompleteToken
from comp7.gui.shared.missions.packers.events import Comp7WeeklyQuestPacker as Comp7WeeklyQuestPacker, Comp7TokenQuestPacker as Comp7TokenQuestPacker
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from comp7_common_const import Comp7QuestType as Comp7QuestType
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.battle_results.progress.progress_helpers import getReceivedTokensInfo as getReceivedTokensInfo
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events import conditions as conditions
from helpers import dependency as dependency
from comp7.gui.impl.gen.view_models.views.lobby.comp7_battle_results_view_model import Comp7BattleResultsViewModel as Comp7BattleResultsViewModel

# base nao representavel no stub: ViewComponent[...]
class Comp7WeeklyMissionsProgressPresenter(IProgressionCategoryPresenter):
    __comp7WeeklyQuestsCtrl: Any
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __progress: Any
    __tooltipData: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, **_):
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
    def __updateModel(self):
        ...
    def __packQuestModel(self, quest, pCur, pPrev, reset, complete, questTokensCount):
        ...
    def __packUncompletedTokenQuestModel(self, questTokensCount):
        ...
    def __getNextTokenQuest(self, currentProgress):
        ...
    def __getNeededTokensCount(self, quest):
        ...
    def __getTokenQuestProgress(self, questTokensCount):
        ...
    def __packBonuses(self, model, quest):
        ...
    def __updateRewardsInTooltips(self, qID, packedBonuses, packedTooltips):
        ...
    def __getEarnedPoints(self, data, pCur, pPrev):
        ...
