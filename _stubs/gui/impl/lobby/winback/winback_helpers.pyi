# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/winback/winback_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import OrderedDict as OrderedDict, defaultdict as defaultdict
from copy import deepcopy as deepcopy
from enum import Enum as Enum
import typing as typing
from blueprints.BlueprintTypes import BlueprintTypes as BlueprintTypes
from blueprints.FragmentTypes import getFragmentType as getFragmentType
from goodies.goodie_constants import GOODIE_VARIETY as GOODIE_VARIETY
from goodies.goodie_helpers import RESOURCES as RESOURCES
from gui.impl.gen.view_models.views.lobby.winback.winback_reward_view_model import RewardName as RewardName
from gui.selectable_reward.constants import SELECTABLE_BONUS_NAME as SELECTABLE_BONUS_NAME
from gui.server_events import conditions as conditions
from gui.server_events.bonuses import getMergedBonusesFromDicts as getMergedBonusesFromDicts, mergeBonuses as mergeBonuses
from helpers import dependency as dependency
from shared_utils import first as first, findFirst as findFirst
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Optional as Optional, Dict as Dict, List as List
from gui.server_events.event_items import Quest as Quest
from gui.server_events.bonuses import SimpleBonus as SimpleBonus, SelectableBonus as SelectableBonus
_logger: Any
TOKEN_TO_REWARD_MAPPING: dict

class SelectableTypes(object):
    VEHICLE = 'vehicle'
    DISCOUNT = 'discount'
    BLUEPRINTS = 'blueprints'

class WinbackQuestTypes(Enum):
    NORMAL = 'normal'
    COMPENSATION = 'compensation'

# decorador original: @dependency.replace_none_kwargs(...)
def getDiscountFromGoody(goodyID, goodiesCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDiscountFromBlueprint(blueprintCD, count=1, itemsCache=None, lobbyContext=None):
    ...
def getLevelFromSelectableToken(tokenID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getWinbackCompletedQuestsCount(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getNonCompensationToken(tokenId, itemsCache=None):
    ...
def getWinbackQuestsData(sortedQuests, dailyQuestTokensCount):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getSortedWinbackQuests(winBackQuests, dailyQuestTokensCount, winbackController=None):
    ...
def getLastWinbackQuestData(sortedQuests, winBackData):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def extendLastQuestBonuses(winBackBonuses, eventsCache=None):
    ...
def filterWinbackQuests(questsPairs, countCompletedQuests):
    ...
