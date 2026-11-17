# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/service_channel_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from itertools import chain as chain
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD
from gui.collection.collections_constants import COLLECTION_ITEM_PREFIX_NAME as COLLECTION_ITEM_PREFIX_NAME
from gui.server_events.bonuses import BattleTokensBonus as BattleTokensBonus
from helpers import dependency as dependency
from items import makeIntCompactDescrByID as makeIntCompactDescrByID
from items.components.c11n_constants import CustomizationNamesToTypes as CustomizationNamesToTypes
from messenger import g_settings as g_settings
from optional_bonuses import BONUS_MERGERS as BONUS_MERGERS
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Set as Set
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
_logger: Any
EOL = '\n'
DEFAULT_MESSAGE = 'defaultMessage'
MessageData: Any
_CustomizationItemData: Any

def getRewardsForBoxes(message, boxIDs):
    ...
def getRewardsForQuests(message, questIDs):
    ...
def mergeRewards(resultRewards, rewards):
    ...
def _mergeSelectableCrewbook(resultRewards, bonusName, bonusValue):
    ...
def getCustomizationItem(itemId, customizationName):
    ...
def getCustomizationItemData(itemId, customizationName):
    ...
def getDefaultMessage(normal='', bold=''):
    ...
def popCollectionEntitlements(rewards):
    ...
def parseTokenBonusCount(bonus, tokenName):
    ...
def extractLockedStyle(data):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPMAdvancedOperationAndQuest(operationID, chainID, questID, eventsCache=None):
    ...
def getPotapovQuestPopUps(message, isQuestOfThisGroup):
    ...
