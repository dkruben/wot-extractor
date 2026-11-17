# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/missions_progress/progress_filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7.gui.impl.lobby.battle_results.missions_progress.research import Comp7VehicleProgressHelper as Comp7VehicleProgressHelper
from shared_utils import findFirst as findFirst
from comp7.gui.impl.lobby.comp7_helpers.comp7_c11n_helpers import getComp7ProgressionStyle as getComp7ProgressionStyle
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import isComp7Quest as isComp7Quest, getComp7QuestType as getComp7QuestType
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from comp7_common_const import Comp7QuestType as Comp7QuestType
from gui.battle_results.progress.progress_filters import commonBattleQuestsProgressFilter as commonBattleQuestsProgressFilter
from gui.battle_results.progress.progress_helpers import isQuestCompleted as isQuestCompleted
from gui.battle_results.progress.progress_helpers import packQuestProgressData as packQuestProgressData
from helpers import dependency as dependency
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo

# decorador original: @dependency.replace_none_kwargs(...)
def comp7WeeklyQuestsProgressFilter(reusable, comp7WeeklyQuestsCtrl=None):
    ...
def comp7CustomizationQuestsProgressFilter(reusable, allCommonQuests):
    ...
def comp7VehicleProgressFilter(reusable):
    ...
def comp7CommonBattleQuestsProgressFilter(reusable, allCommonQuests):
    ...
def _getComp7StyleProgressionQuestIDs():
    ...
