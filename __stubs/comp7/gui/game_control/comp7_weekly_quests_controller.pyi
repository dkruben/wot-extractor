# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/game_control/comp7_weekly_quests_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from Event import Event as Event, EventManager as EventManager
from PlayerEvents import g_playerEvents as g_playerEvents
from comp7_common_const import Comp7QuestType as Comp7QuestType
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import Comp7ParsedQuestID as Comp7ParsedQuestID, isWeeklyRewardClaimed as isWeeklyRewardClaimed
from comp7.skeletons.gui.game_control import IComp7WeeklyQuestsController as IComp7WeeklyQuestsController
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency, time_utils as time_utils
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Callable as Callable, List as List, Optional as Optional, Tuple as Tuple, Union as Union
from comp7.gui.game_control.comp7_controller import Comp7Controller as Comp7Controller
from gui.server_events import EventsCache as EventsCache
from gui.server_events.event_items import Quest as Quest, TokenQuest as TokenQuest
from gui.shared.items_cache import ItemsCache as ItemsCache
from gui.offers import OffersDataProvider as OffersDataProvider
_logger: Any

class Comp7WeeklyQuestsController(IComp7WeeklyQuestsController, IGlobalListener):
    __comp7Controller: Any
    __eventsCache: Any
    __itemsCache: Any
    __offersProvider: Any
    __quests: Any
    __timer: Any
    __eventsManager: Any
    onWeeklyQuestsUpdated: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def getQuests(self):
        ...
    def onConnected(self):
        ...
    def onDisconnected(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def __onPrbDispatcherCreated(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onEventsCacheSyncCompleted(self):
        ...
    def __onComp7StatusUpdated(self, _):
        ...
    def __onOffersUpdated(self):
        ...
    def __updateQuests(self):
        ...
    @classmethod
    def __getUpdatedQuests(cls):
        ...
    def __setNewQuestsCallback(self):
        ...

class _Comp7WeeklyQuests(object):
    __slots__: tuple
    sortedBattleQuests: Any
    sortedTokenQuests: Any
    oldQuest: Any
    newQuest: Any
    numBattleQuests: Any
    numCompletedBattleQuests: Any
    numBattleQuestsToCompleteByTokenQuestIdx: Any
    timeOfNewQuests: Any
    def __init__(self, battleQuests, tokenQuests, oldQuest, newQuest, numBattleQuests, numCompletedBattleQuests, timeOfNewQuests):
        ...
    def getTimeToNewQuests(self):
        ...
    def __repr__(self):
        ...

class _Comp7WeeklyQuestsInErrorState(_Comp7WeeklyQuests):
    def __init__(self):
        ...

def _filterAndAppend(appendToBattle, appendToToken, quest, battleQuestType=..., tokenQuestType=...):
    ...
