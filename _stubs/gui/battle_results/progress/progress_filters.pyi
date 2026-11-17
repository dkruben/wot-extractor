# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/progress/progress_filters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import copy as copy
import typing as typing
import constants as constants
import personal_missions as personal_missions
from future.utils import itervalues as itervalues, viewitems as viewitems
from challenges_common import isChallengeQuest as isChallengeQuest
from gui.battle_results.progress.progress_helpers import packQuestProgressData as packQuestProgressData, isQuestCompleted as isQuestCompleted, getPrestigeProgress as getPrestigeProgress, isPMOperationAndMissionEnabled as isPMOperationAndMissionEnabled
from gui.server_events.events_helpers import isPremium as isPremium, isDailyQuest as isDailyQuest, isWeeklyQuest as isWeeklyQuest, isBattleMattersQuestID as isBattleMattersQuestID, isCommonBattleQuest as isCommonBattleQuest
from gui.server_events.finders import getBranchByOperationId as getBranchByOperationId
from potapov_quests import isWithoutAwardListBranchQuest as isWithoutAwardListBranchQuest
from skeletons.gui.server_events import IEventsCache as IEventsCache
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH
from gui.battle_results.progress.research import VehicleProgressHelper as VehicleProgressHelper
from gui.impl.lobby.challenges.views_helpers import parseChallengeQuestId as parseChallengeQuestId
from skeletons.gui.game_control import IBattlePassController as IBattlePassController
from skeletons.gui.challenges import IChallengesController as IChallengesController
from typing import List as List, Tuple as Tuple
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
from gui.server_events.event_items import PersonalMission as PersonalMission
from gui.server_events.personal_missions_cache import PersonalMissionsCache as PersonalMissionsCache

def battleMattersProgressFilter(reusable, allCommonQuests):
    ...
def dailyQuestsProgressFilter(reusable, allCommonQuests):
    ...
def weeklyQuestsProgressFilter(reusable, allCommonQuests):
    ...
def battlePassProgressFilter(reusable):
    ...
def prestigeProgressFilter(reusable):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def personalMissionProgressFilter(reusable, eventsCache=None):
    ...
def vehicleProgressFilter(reusable):
    ...
def commonBattleQuestsProgressFilter(reusable, allCommonQuests):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def challengesMissionsProgressFilter(reusable, allCommonQuests, challenges=None):
    ...
