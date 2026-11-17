# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/challenges/challenge_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from account_helpers.AccountSettings import ChallengesMissions as ChallengesMissions
from helpers import dependency as dependency, time_utils as time_utils
from gui.challenges.challenges_helpers import TIME_BEFORE_END_OF_EXPIRATION as TIME_BEFORE_END_OF_EXPIRATION, getSettings as getSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Iterator as Iterator, List as List
from challenges_common import ChallengeConfig as ChallengeConfig, ChallengeTypes as ChallengeTypes, ChallengeDifficulties as ChallengeDifficulties, ChallengeMainRewardTypes as ChallengeMainRewardTypes
from gui.server_events.event_items import Quest as Quest
_logger: Any

class ChallengeItem(object):
    __itemsCache: Any
    __eventsCache: Any
    config: Any
    def __init__(self, config):
        ...
    @property
    def challengeID(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def difficulty(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def challengeType(self):
        ...
    @property
    def startTime(self):
        ...
    @property
    def finishTime(self):
        ...
    @property
    def expireTime(self):
        ...
    @property
    def isExpiringSoon(self):
        ...
    @property
    def allowedCompletions(self):
        ...
    @property
    def freeRestartsPerCompletion(self):
        ...
    @property
    def attempts(self):
        ...
    @property
    def questsIDs(self):
        ...
    @property
    def usedFreeRestarts(self):
        ...
    @property
    def isVisited(self):
        ...
    @property
    def restartPrice(self):
        ...
    @property
    def name(self):
        ...
    @property
    def mainRewardType(self):
        ...
    def getTokenID(self, tokenType):
        ...
    def iterQuests(self):
        ...
