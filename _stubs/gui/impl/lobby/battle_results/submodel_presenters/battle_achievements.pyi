# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/battle_achievements.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
import json as json
from frameworks.wulf import Array as Array
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.battle_results.pbs_helpers.common import getPersonalAchievements as getPersonalAchievements
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.postbattle_achievement_model import PostbattleAchievementModel as PostbattleAchievementModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.pbs_helpers.common import _AchievementData as _AchievementData
AchievementTooltipType: tuple

class BattleAchievementsSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def packBattleResults(self, battleResults):
        ...
    def __setAchievementsResults(self, achievement):
        ...
