# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/offers/offer_gifts_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import ResMgr as ResMgr
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from constants import RentType as RentType, PREMIUM_ENTITLEMENTS as PREMIUM_ENTITLEMENTS
from PlayerEvents import g_playerEvents as g_playerEvents
from gui import SystemMessages as SystemMessages
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items.processors.offers import ReceiveOfferGiftProcessor as ReceiveOfferGiftProcessor
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency, time_utils as time_utils
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen.view_models.views.lobby.offers.gift_model import GiftModel as GiftModel
from gui.impl.gen.view_models.views.lobby.offers.offer_model import OfferModel as OfferModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from shared_utils import awaitNextFrame as awaitNextFrame
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider, IOffersNovelty as IOffersNovelty
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from web.cache.web_cache import CachePrefetchResult as CachePrefetchResult
_logger: Any
RENT_TYPE_TO_MODEL_CONSTANT: dict
BONUSES_WITHOUT_COUNTER: set

class OfferGiftsWindow(WindowImpl):
    def __init__(self, layer, *args, **kwargs):
        ...

class OfferGiftsView(ViewImpl):
    _lobbyContext: Any
    _eventsCache: Any
    _itemsCache: Any
    _offersProvider: Any
    _offersNovelty: Any
    _externalBrowser: Any
    _offerID: Any
    __overrideSuccessCallback: Any
    __overrideOnBackCallback: Any
    def __init__(self, offerID, layoutID=..., overrideSuccessCallback=None, overrideOnBackCallback=None):
        ...
    @property
    def _serverSettings(self):
        ...
    @property
    def _viewModel(self):
        ...
    @property
    def _offerItem(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @adisp_process
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def syncOfferResources(self, callback=None):
        ...
    def _setDynamicInfo(self, offerModel):
        ...
    def _generateGifts(self, model):
        ...
    def _getGiftResources(self, gift):
        ...
    def _onGiftClicked(self, args):
        ...
    # decorador original: @adisp_process
    def _onGiftConfirm(self, offerID, giftID, cdnTitle='', cdnDescription='', cdnIcon=''):
        ...
    def _onItemsCacheResync(self, *args, **kwargs):
        ...
    def _onOffersUpdated(self):
        ...
    def _onBecomeNonPlayer(self, *args, **kwargs):
        ...
    def _onServerSettingsRecync(self, *args, **kwargs):
        ...
    def _onBack(self, _=None):
        ...
    def _onLearnMore(self):
        ...
