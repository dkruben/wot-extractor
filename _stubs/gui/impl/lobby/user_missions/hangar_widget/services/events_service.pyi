# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/services/events_service.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
import json as json
import logging as logging
from itertools import chain as chain
from future.utils import viewvalues as viewvalues
from typing import List as List
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg import umgEventsConfigSchema as umgEventsConfigSchema
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.impl.lobby.personal_missions_30.views_helpers import isPM4BannerAvailable as isPM4BannerAvailable
from gui.impl.lobby.stronghold_event.stronghold_event_banner import StrongholdEventBanner as StrongholdEventBanner
from gui.impl.lobby.stronghold_event.stronghold_event_helpers import isStrongholdEventBannerAvailable as isStrongholdEventBannerAvailable
from gui.impl.lobby.user_missions.hangar_widget.event_banners.challenges_event_banner import ChallengesEventBanner as ChallengesEventBanner, isChallengesBannerAvailable as isChallengesBannerAvailable
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.pm4_event_banner import PM4EventBunner as PM4EventBunner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.integrated_auction.auction_event_banner import IntegratedAuctionEventBanner as IntegratedAuctionEventBanner, isAuctionEventBannerAvailable as isAuctionEventBannerAvailable
from gui.shared.system_factory import registerBannerEntryPointValidator as registerBannerEntryPointValidator, collectBannerEntryPointValidator as collectBannerEntryPointValidator
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, ONE_DAY as ONE_DAY
from helpers.time_utils import getTimestampByStrDate as getTimestampByStrDate
from skeletons.gui.game_control import IEventsNotificationsController as IEventsNotificationsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.lobby.user_missions.hangar_widget.services.service_events import ServiceEvents as ServiceEvents
_HANGAR_ENTRY_POINTS = 'hangarEntryPoints'
_SECONDS_BEFORE_UPDATE = 2
_logger: Any

class _EntryPointData(object):
    __slots__: list
    data: Any
    id: Any
    weight: Any
    __isValidData: Any
    startDate: Any
    endDate: Any
    def __init__(self, entryData):
        ...
    def updateValidData(self):
        ...
    def isValidData(self):
        ...
    def isValidDateForCreation(self):
        ...
    def isExpiredDate(self):
        ...
    def isEarlyDate(self):
        ...
    def isEnabledByValidator(self):
        ...

class EventsService(IEventsService, Notifiable, ServiceEvents):
    __notificationsCtrl: Any
    __lobbyContext: Any
    __itemsCache: Any
    __slots__: list
    onEventsListChanged: Any
    __entries: Any
    __visibleEntries: Any
    __serverSettings: Any
    def __init__(self):
        ...
    @property
    def isAvailable(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def getEntries(self):
        ...
    def getEntryData(self, id):
        ...
    def updateEntries(self):
        ...
    def startListening(self):
        ...
    def stopListening(self):
        ...
    def finalize(self):
        ...
    def _isQueueEnabled(self):
        ...
    def __isQueueSelected(self, queueType):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onUpdateSettings(self, _):
        ...
    def __onEventNotification(self, added, removed):
        ...
    def __onCacheResync(self, _, __):
        ...
    def __onStrongholdEventUpdated(self, *_):
        ...
    def __handleNotifications(self, notifications):
        ...
    def __onUpdateNotify(self):
        ...
    def __getCooldownForUpdate(self):
        ...
    def __updateEntries(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...

def getWeightByEventName(eventName):
    ...
