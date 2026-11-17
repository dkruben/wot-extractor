# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/rest_bonus_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import Event as Event
from future.utils import viewvalues as viewvalues
from constants import ARENA_BONUS_TYPE_TO_QUEUE_TYPE as ARENA_BONUS_TYPE_TO_QUEUE_TYPE, EVENT_CLIENT_DATA as EVENT_CLIENT_DATA, EVENT_TYPE as EVENT_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from skeletons.gui.game_control import IRestBonusController as IRestBonusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Optional as Optional
from gui.server_events.event_items import Quest as Quest
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_logger: Any
REST_BONUS_PREFIX = 'rest_bonus'
SEPARATOR = ':'
REST_BONUS_ACCESS_TOKEN: Any
REST_BONUS_XP_FACTOR_BONUS = 'xpFactor'
REST_BONUS_BASE_FACTOR = 1

class RestBonusController(IRestBonusController, IGlobalListener):
    __slots__: tuple
    __lobbyContext: Any
    __itemsCache: Any
    __eventsCache: Any
    _questsCache: Any
    __expiryTime: Any
    onUpdated: Any
    def __init__(self):
        ...
    @property
    def dailyXPFactor(self):
        ...
    @property
    def restBonusQuests(self):
        ...
    @staticmethod
    def isRestBonusQuestID(quest):
        ...
    def getXpFactor(self, vehicle):
        ...
    def getRestBonusExpiryTime(self):
        ...
    def getActualXPFactor(self, vehicle):
        ...
    def getDailyResetTime(self):
        ...
    def fini(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onDisconnected(self):
        ...
    def hasActiveBattleQuest(self, vehicle):
        ...
    def __getActiveBattleQuests(self, vehicle):
        ...
    def __isQuestAvailable(self, quest, queueType, vehicle):
        ...
    @staticmethod
    def __hasQuestQueueType(quest, queueType):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __validateBattleQuests(self):
        ...
    def __clear(self):
        ...
    def __initQuestsCache(self, *args, **kwargs):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onItemsCacheUpdated(self, reason, diff):
        ...
