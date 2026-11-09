# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/personalreserves/boosters_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from account_helpers import AccountSettings as AccountSettings
from goodies.goodie_constants import GOODIE_RESOURCE_TYPE as GOODIE_RESOURCE_TYPE
from goodies.goodie_helpers import GoodieExpirationData as GoodieExpirationData
from gui import makeHtmlString as makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.lobby.personal_reserves.personal_reserves_utils import findNearestExpiryTimeInBoostersList as findNearestExpiryTimeInBoostersList
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import createStorageDefVO as createStorageDefVO, isStorageSessionTimeout as isStorageSessionTimeout
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPersonalReservesUrl as getBuyPersonalReservesUrl
from gui.Scaleform.daapi.view.meta.StorageCategoryPersonalReservesViewMeta import StorageCategoryPersonalReservesViewMeta as StorageCategoryPersonalReservesViewMeta
from gui.Scaleform.genConsts.STORE_CONSTANTS import STORE_CONSTANTS as STORE_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, TimerNotifier as TimerNotifier
from gui.goodies.goodie_items import BOOSTERS_ORDERS as BOOSTERS_ORDERS, MAX_ACTIVE_BOOSTERS_COUNT as MAX_ACTIVE_BOOSTERS_COUNT
from gui.impl import backport as backport
from gui.impl.common.personal_reserves.personal_reserves_shared_constants import PREMIUM_BOOSTER_IDS as PREMIUM_BOOSTER_IDS
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showShop as showShop, showPersonalReservesInfomationScreen as showPersonalReservesInfomationScreen, showBoostersActivation as showBoostersActivation
from gui.shared.formatters import text_styles as text_styles, getItemPricesVO as getItemPricesVO
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from helpers.i18n import makeString as _ms
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.server_events import IEventsCache as IEventsCache
_TYPE_BIT_TO_RESOURCE_TYPE_MAP: dict
_TYPE_BIT_TO_CRITERIA: dict
_TYPE_FILTER_ITEMS: list

class _FilterBit(CONST_CONTAINER):
    XP = 1
    CREW_XP = 2
    FREE_XP = 4
    CREDITS = 8
    ONE = 16
    TWO = 32
    FOUR = 64
    SIX = 128
    FREE_XP_CREW_XP = 256
    EXPIRABLE = 512
    NON_EXPIRABLE = 1024
    PREMIUM = 2048

class StorageCategoryPersonalReservesView(StorageCategoryPersonalReservesViewMeta):
    _eventsCache: Any
    _goodiesCache: Any
    _epicCtrl: Any
    _boosters: Any
    __filterMask: Any
    __notificatorManager: Any
    def __init__(self):
        ...
    def navigateToStore(self):
        ...
    def resetFilter(self):
        ...
    def onFiltersChange(self, filters):
        ...
    def onInfoClicked(self):
        ...
    def activateReserve(self, boosterId):
        ...
    def _getClientSectionKey(self):
        ...
    def _loadFilters(self):
        ...
    def _saveFilters(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self, *args):
        ...
    def __getBoosters(self):
        ...
    def __timeTillNextNotification(self):
        ...
    def __onGoodiesCacheUpdate(self, *args):
        ...
    def __onUpdateBoosters(self, *args):
        ...
    def __onQuestsUpdate(self, *args):
        ...
    def __sortKey(self, expirationData):
        ...
    def __initFilter(self):
        ...
    def __updateFilterCounter(self, count, total):
        ...

def getCriteriaFromFilterMask(filterMask):
    ...
