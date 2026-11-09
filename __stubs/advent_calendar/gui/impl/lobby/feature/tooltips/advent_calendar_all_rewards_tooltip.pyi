# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/tooltips/advent_calendar_all_rewards_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from advent_calendar.gui.feature.constants import PROGRESSION_REWARD_TYPE_TO_ICON as PROGRESSION_REWARD_TYPE_TO_ICON
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.all_rewards_tooltip_view_model import AllRewardsTooltipViewModel as AllRewardsTooltipViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.tooltips.bonus_item_view_model import BonusItemViewModel as BonusItemViewModel
from advent_calendar.gui.impl.lobby.feature.bonus_grouper import QuestRewardsGroups as QuestRewardsGroups
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
_QUEST_REWARDS_GROUPS_ORDER: tuple

class AdventCalendarAllRewardsTooltip(ViewImpl):
    __adventCalendarController: Any
    def __init__(self, *args):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    @staticmethod
    def __processRewardGroups(rewardGroups):
        ...

def _rewardsGroupsSortOrder(bonusGroup):
    ...
