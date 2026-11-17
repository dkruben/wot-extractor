# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/weekly_quests_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_UI_SECTION as COMP7_UI_SECTION, COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT as COMP7_WEEKLY_QUESTS_PAGE_TOKENS_COUNT
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.progress_points_model import ProgressPointsModel as ProgressPointsModel
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import getComp7BonusPacker as getComp7BonusPacker, packTokensRewardsQuestBonuses as packTokensRewardsQuestBonuses, packQuestBonuses as packQuestBonuses
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isWeeklyRewardClaimable as isWeeklyRewardClaimable, isWeeklyRewardClaimed as isWeeklyRewardClaimed
from comp7.gui.impl.lobby.meta_view.pages import PageSubModelPresenter as PageSubModelPresenter
from comp7.gui.shared.event_dispatcher import showComp7WeeklyQuestsRewardsSelectionWindow as showComp7WeeklyQuestsRewardsSelectionWindow
from comp7.gui.shared.missions.packers.events import Comp7WeeklyQuestPacker as Comp7WeeklyQuestPacker
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.weekly_quests_model import ChoiceRewardState as ChoiceRewardState
from typing import Dict as Dict, Iterator as Iterator, List as List, Optional as Optional, Tuple as Tuple, Union as Union
from comp7.gui.game_control.comp7_controller import Comp7Controller as Comp7Controller
from comp7.gui.game_control.comp7_weekly_quests_controller import Comp7WeeklyQuestsController as Comp7WeeklyQuestsController, _Comp7WeeklyQuests as _Comp7WeeklyQuests
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.quest_card_model import QuestCardModel as QuestCardModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.weekly_quests_model import WeeklyQuestsModel as WeeklyQuestsModel
from frameworks.wulf import ViewEvent as ViewEvent
from gui.impl.backport import TooltipData as TooltipData
from gui.server_events.event_items import Quest as Quest, TokenQuest as TokenQuest
_logger: Any

class WeeklyQuestsPage(PageSubModelPresenter):
    pageId = MetaRootViews.WEEKLYQUESTS
    __comp7Controller: Any
    __comp7WeeklyQuestsCtrl: Any
    __slots__: tuple
    __tooltipDataById: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def viewModel(self):
        ...
    def initialize(self, **params):
        ...
    def finalize(self):
        ...
    def createToolTip(self, event):
        ...
    def _getEvents(self):
        ...
    def __onWeeklyQuestsUpdated(self, quests):
        ...
    @staticmethod
    def __onGoToRewardsSelection():
        ...
    def __updateData(self, quests):
        ...
    @staticmethod
    def __getClaimWeeklyRewardButtonState():
        ...
    def __updateQuestCardModels(self, sortedBattleQuests):
        ...
    def __updateProgressPointModels(self, tokenQuests, numBattleQuestsToCompleteByTokenQuestIdx):
        ...
    def __updateRewardsInTooltips(self, qID, packedBonuses, tooltipsData):
        ...
    @staticmethod
    def __sliceOffCompletedWeeksExceptLast(weeklyQuests, questsPerWeek):
        ...
    @staticmethod
    def __setProgressAnimationToBeShown(model, numCompletedBattleQuests):
        ...
    def __onAnimationEnd(self):
        ...
