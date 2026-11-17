# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from fun_random.gui.battle_results.packers.fun_progression_helpers import FunPbsProgressionHelper as FunPbsProgressionHelper, FunPbsUnlimitedProgressionHelper as FunPbsUnlimitedProgressionHelper
from fun_random.gui.feature.util.fun_helpers import isFunProgressionUnlimitedTrigger as isFunProgressionUnlimitedTrigger
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin, FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.impl.gen.view_models.views.lobby.feature.battle_results.fun_random_progress_model import FunRandomProgressModel as FunRandomProgressModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packBonuses as packBonuses, packStageRewards as packStageRewards, sortFunProgressionBonuses as sortFunProgressionBonuses
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen import R as R
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip as AdditionalRewardsTooltip
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
_RewardsData: Any

class FunProgressionSubPresenter(BattleResultsSubPresenter, FunProgressionWatcher, FunAssetPacksMixin):
    __rewardsData: Any
    def __init__(self, viewModel, parentView):
        ...
    def finalize(self):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def __packModel(self, model, progressionData):
        ...
    @staticmethod
    def __createProgressionHelper(questsProgress):
        ...
