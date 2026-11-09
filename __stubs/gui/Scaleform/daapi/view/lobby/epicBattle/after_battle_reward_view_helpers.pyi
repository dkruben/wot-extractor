# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/after_battle_reward_view_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from itertools import chain as chain
from helpers import dependency as dependency, int2roman as int2roman
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from epic_constants import EPIC_BATTLE_LEVEL_IMAGE_INDEX as EPIC_BATTLE_LEVEL_IMAGE_INDEX
_logger: Any
ProgressionLevelIconVO: Any

# decorador original: @dependency.replace_none_kwargs(...)
def getQuestBonuses(questsProgressData, questIDs, currentLevelQuestID, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getFinishBadgeBonuses(questsProgressData, finishQuestID, eventsCache=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getProgressionIconVO(cycleNumber, playerLevel, epicController=None):
    ...
def getProgressionIconVODict(cycleNumber, playerLevel):
    ...
def _getProgressionIconBackgroundId(level):
    ...
