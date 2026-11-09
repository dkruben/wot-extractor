# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/offers/data_provider.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import wraps as wraps
import typing as typing
import adisp as adisp
from BWUtil import AsyncReturn as AsyncReturn
from Event import Event as Event, EventManager as EventManager
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import OFFERS_DISABLED_MSG_SEEN as OFFERS_DISABLED_MSG_SEEN
from account_helpers.offers import events_data as events_data
from account_helpers.offers.cache import CdnResourcesCache as CdnResourcesCache
from constants import EVENT_CLIENT_DATA as EVENT_CLIENT_DATA, OFFERS_ENABLED_KEY as OFFERS_ENABLED_KEY, OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.server_events.events_helpers import getEventsData as getEventsData
from gui.shared.gui_items.processors import makeI18nError as makeI18nError
from gui.shared.utils.requesters.offers_requester import OffersRequester as OffersRequester
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.cache.web_cache import CachePrefetchResult as CachePrefetchResult
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Callable as Callable, Optional as Optional, Set as Set, Union as Union
_logger: Any
_CDN_SYNC_TIMEOUT = 60.0

class OffersDataProvider(IOffersDataProvider):
    _connMgr: Any
    _itemsCache: Any
    _lobbyContext: Any
    _em: Any
    _states: Any
    _ready: Any
    _pendingNotify: Any
    _cache: Any
    _lastAvailableOffers: Any
    _cdnCache: Any
    _getOffersData: Any
    onOffersUpdated: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def update(self, diff):
        ...
    @property
    def isSynced(self):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def getReceivedGifts(self, offerID):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def isBannerSeen(self, offerID):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    # decorador original: @adisp.adisp_async
    def isCdnResourcesReady(self, callback=None, timeout=...):
        ...
    def getCdnResourcePath(self, cdnRelativePath, relative=True):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def getOffer(self, offerID):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def getOfferByToken(self, token):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def iAvailableOffers(self, onlyVisible=True):
        ...
    def getAvailableOffers(self, onlyVisible=True):
        ...
    def getAvailableOffersByToken(self, token):
        ...
    def isOfferAvailable(self, tokenID):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def iUnlockedOffers(self, onlyVisible=True, includeAllOffers=True):
        ...
    def getUnlockedOffers(self, onlyVisible=True, includeAllOffers=True):
        ...
    def isOfferUnlocked(self, tokenID):
        ...
    def getAmountOfGiftsGenerated(self, tokenID, mainTokenCount):
        ...
    def _onDisconnected(self):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def _makeOffer(self, offerID, offerData):
        ...
    @property
    def _readyToNotify(self):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @wg_async
    def _notify(self):
        ...
    def _onConnected(self, *args, **kwargs):
        ...
    def _onServerSettingsChanged(self, *args, **kwargs):
        ...
    def _onServerSettingsChange(self, *args, **kwargs):
        ...
    def _ioffers(self):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def _checkAvailableOffersChanged(self):
        ...
    # decorador original: @_ifFeatureDisabled(...)
    # decorador original: @_ifNotSynced(...)
    def __iAvailableOffersByToken(self, token):
        ...

def _getEventsOffersData():
    ...
def _ifFeatureDisabled(result):
    ...
def _ifNotSynced(result):
    ...
