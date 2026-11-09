# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/quests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
from future.utils import listvalues as listvalues
import typing as typing
import BigWorld as BigWorld
from constants import EVENT_TYPE as EVENT_TYPE
from gui import SystemMessages as SystemMessages
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.pm_constants import DISCARDABLE_OPERATIONS_IDS as DISCARDABLE_OPERATIONS_IDS, PM_SUIT_OP_PLUGIN_ERR_RESPONSE as PM_SUIT_OP_PLUGIN_ERR_RESPONSE
from gui.shared.gui_items.processors import Processor as Processor, makeI18nError as makeI18nError, makeI18nSuccess as makeI18nSuccess, makeSuccess as makeSuccess, plugins as plugins
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency
from items import ITEM_TYPES as ITEM_TYPES, tankmen as tankmen
from personal_missions import PM_BRANCH as PM_BRANCH
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import PersonalMission as PersonalMission
_logger: Any

class _PMRequest(Processor):
    _branch: Any
    _quests: Any
    def __init__(self, personalMissions, branch):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def _getQuestsData(self, methodcaller):
        ...
    def _getQuestsNames(self):
        ...
    @staticmethod
    def _pushMessage(text, title, priority, messageType=...):
        ...

class PMQuestSelect(_PMRequest):
    eventsCache: Any
    def __init__(self, branch, personalMission, isOperationActivation=False):
        ...
    def _getMessagePrefix(self):
        ...
    def _removeFromSameChain(self, quests, newQuests):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class PMOperationSelect(_PMRequest):
    __eventsCache: Any
    __pmCache: Any
    __operationID: Any
    __isFirstTimeEntrance: Any
    __branches: Any
    __inProgressPMOperations: Any
    __currentActivePMOperation: Any
    def __init__(self, branch, operationID, missions=None, skipValidation=False, isFirstTimeEntrance=False):
        ...
    def _getMessagePrefix(self):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class PMDiscard(_PMRequest):
    eventsCache: Any
    def __init__(self, personalMission, branch):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _getMessagePrefix(self):
        ...

class PMPause(_PMRequest):
    _enable: Any
    def __init__(self, personalMission, enable, branch):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _getMessagePrefix(self):
        ...

class PMActivateSeason(_PMRequest):
    __eventsCache: Any
    __pmCache: Any
    __activeCampaigns: Any
    _season: Any
    def __init__(self, branch):
        ...
    def _request(self, callback):
        ...
    def _getMessagePrefix(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class _PMGetReward(Processor):
    __quest: Any
    __nationID: Any
    __inNationID: Any
    __role: Any
    __needTankman: Any
    def __init__(self, personalMission, needTankman, nationID, inNationID, role):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class PMGetTankwomanReward(_PMGetReward):
    def __init__(self, personalMission, nationID, inNationID, role):
        ...
    def _getMessagePrefix(self):
        ...

class PMGetReward(_PMGetReward):
    def __init__(self, personalMission):
        ...

class PMGetQuestRewards(Processor):
    __quest: Any
    __branchName: Any
    def __init__(self, quest, branchName):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class PMPawn(Processor):
    eventsCache: Any
    __quest: Any
    def __init__(self, personalMission):
        ...
    def _getMessagePrefix(self):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
