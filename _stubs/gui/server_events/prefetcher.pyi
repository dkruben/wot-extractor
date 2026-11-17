# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/prefetcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import itertools as itertools
import weakref as weakref
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import ResMgr as ResMgr
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback, AsyncScope as AsyncScope, AsyncSemaphore as AsyncSemaphore
from constants import DailyQuestDecorationMap as DailyQuestDecorationMap, EVENT_TYPE as EVENT_TYPE, GF_RES_PROTOCOL as GF_RES_PROTOCOL
from debug_utils import LOG_WARNING as LOG_WARNING
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl.gen import R as R
from gui.impl import backport as backport
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES, DECORATION_SIZES as DECORATION_SIZES, parseComplexToken as parseComplexToken
from gui.server_events.events_helpers import isMarathon as isMarathon, isDailyQuest as isDailyQuest, isPremium as isPremium
from gui.shared.image_helper import getTextureLinkByID as getTextureLinkByID
from gui.shared.utils import mapTextureToTheMemory as mapTextureToTheMemory, getImageSize as getImageSize, removeTextureFromMemory as removeTextureFromMemory
from helpers import getClientLanguage as getClientLanguage, dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from soft_exception import SoftException as SoftException
from gui.server_events.event_items import Quest as Quest
_DEFAULT_TOKENS_STYLES: list
_DEFAULT_DECORATIONS: list
_TokenInfoData: Any

class SubRequester(object):
    _eventsCache: Any
    _semaphore: Any
    _storage: Any
    def __init__(self, eventsCache, semaphore):
        ...
    def pickup(self, ticket):
        ...
    def clear(self):
        ...
    def ask(self, filecache, fileserver):
        ...
    def demand(self, filecache, fileserver):
        ...
    # decorador original: @wg_async
    def _run(self, url, headers, ticket, filecache):
        ...
    def _handler(self, ticket, content):
        ...
    def _tickets(self):
        ...
    @staticmethod
    def _urlGetter(fileserver):
        ...
    @staticmethod
    def _headers():
        ...
    def __contains__(self, ticket):
        ...

class ImagesSubRequester(SubRequester):
    _textures: Any
    def __init__(self, eventsCache, semaphore):
        ...
    def clear(self):
        ...
    def _handler(self, ticket, content):
        ...
    def _getTextureLink(self, ticket, protocol):
        ...
    def _releaseTexture(self, ticket):
        ...

class TokenImagesSubRequester(ImagesSubRequester):
    def pickup(self, styleID, size, protocol=...):
        ...
    def _tickets(self):
        ...
    @staticmethod
    def _urlGetter(fileserver):
        ...

class TokenInfoSubRequester(SubRequester):
    def pickup(self, styleID):
        ...
    def _handler(self, ticket, content):
        ...
    def _tickets(self):
        ...
    @staticmethod
    def _urlGetter(fileserver):
        ...
    def __contains__(self, _):
        ...

class DecorationRequester(ImagesSubRequester):
    def pickup(self, decorationID, size, protocol=...):
        ...
    def _tickets(self):
        ...
    @staticmethod
    def _urlGetter(fileserver):
        ...

class TokenSaleSubRequester(SubRequester):
    def pickup(self, tokenWebID):
        ...
    def _tickets(self):
        ...
    def _handler(self, ticket, content):
        ...
    @staticmethod
    def _urlGetter(_):
        ...
    @staticmethod
    def _headers():
        ...
    def __contains__(self, ticket):
        ...

class Prefetcher(object):
    lobbyContext: Any
    _eventsCache: Any
    _asyncScope: Any
    _semaphore: Any
    _requesters: Any
    def __init__(self, eventsCache):
        ...
    def getTokenImage(self, styleID, size, protocol=...):
        ...
    def getMissionDecoration(self, decorationID, size, protocol=...):
        ...
    def getTokenInfo(self, styleID):
        ...
    def getTokenDetailedInfo(self, styleID):
        ...
    def isTokenOnSale(self, tokenWebID):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def clear(self):
        ...
    def ask(self):
        ...
    # decorador original: @wg_async
    def demand(self):
        ...

def _getTokensFromAccountReqs(quest):
    ...
def _getTokensFromBonuses(quest):
    ...
