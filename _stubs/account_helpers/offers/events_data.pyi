# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/offers/events_data.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import time as time
import typing as typing
from future.utils import viewitems as viewitems
from constants import PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS, RentType as RentType
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.server_events.bonuses import getOfferBonuses as getOfferBonuses, VehiclesBonus as VehiclesBonus
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency, getClientLanguage as getClientLanguage, time_utils as time_utils
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
CDN_KEY = 'cdn'
OFFER_BONUSES_PRIORITY: tuple
DEFAULT_PRIORITY: Any

class OfferEventData(object):
    __slots__: tuple
    _itemsCache: Any
    _offersProvider: Any
    _langCode: Any
    _id: Any
    _data: Any
    def __init__(self, itemID, data):
        ...
    @property
    def id(self):
        ...
    @property
    def token(self):
        ...
    @property
    def giftToken(self):
        ...
    @property
    def giftTokenCount(self):
        ...
    @property
    def showBanner(self):
        ...
    @property
    def priority(self):
        ...
    @property
    def showPrice(self):
        ...
    @property
    def showInGUI(self):
        ...
    @property
    def showWhenZeroCurrency(self):
        ...
    @property
    def cdnLocFilePath(self):
        ...
    @property
    def cdnBannerLogoPath(self):
        ...
    @property
    def cdnLogoPath(self):
        ...
    @property
    def cdnGiftsBackgroundPath(self):
        ...
    @property
    def cdnGiftsTokenImgPath(self):
        ...
    @property
    def cdnSignSmallImgPath(self):
        ...
    @property
    def cdnSignBigImgPath(self):
        ...
    @property
    def availableGifts(self):
        ...
    def getGift(self, giftID):
        ...
    def getGiftAvailableCount(self, giftID):
        ...
    def getAllGifts(self):
        ...
    def getFirstGift(self):
        ...
    @property
    def clicksCount(self):
        ...
    @property
    def availableTokens(self):
        ...
    @property
    def availableGiftsCount(self):
        ...
    @property
    def isOutOfLimit(self):
        ...
    @property
    def expiration(self):
        ...
    @property
    def isOfferAvailable(self):
        ...
    @property
    def isOfferUnlocked(self):
        ...
    @property
    def isOutOfDate(self):
        ...
    def getFinishTime(self):
        ...
    def getFinishTimeLeft(self):
        ...
    @property
    def _tokensCache(self):
        ...
    @property
    def _receivedGifts(self):
        ...

class OfferGift(object):
    _langCode: Any
    _id: Any
    _data: Any
    _bonus: Any
    _bonuses: Any
    def __init__(self, giftID, giftData):
        ...
    @property
    def id(self):
        ...
    @property
    def cdnLocFilePath(self):
        ...
    @property
    def cdnImagePath(self):
        ...
    @property
    def cdnIconPath(self):
        ...
    @property
    def fromCdn(self):
        ...
    @property
    def title(self):
        ...
    @property
    def description(self):
        ...
    @property
    def icon(self):
        ...
    @property
    def price(self):
        ...
    def limit(self):
        ...
    @property
    def nationFlag(self):
        ...
    @property
    def highlight(self):
        ...
    @property
    def giftCount(self):
        ...
    @property
    def inventoryCount(self):
        ...
    @property
    def rentType(self):
        ...
    @property
    def rentValue(self):
        ...
    @property
    def isDisabled(self):
        ...
    @property
    def rawBonuses(self):
        ...
    @property
    def bonuses(self):
        ...
    @property
    def bonus(self):
        ...
    @property
    def isWithSlotBonus(self):
        ...
    @property
    def buttonLabel(self):
        ...
    @property
    def isVehicle(self):
        ...
    @property
    def bonusType(self):
        ...
