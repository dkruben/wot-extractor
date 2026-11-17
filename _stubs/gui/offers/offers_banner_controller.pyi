# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/offers/offers_banner_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from functools import partial as partial
import BigWorld as BigWorld
import Event as Event
from adisp import adisp_process as adisp_process
from gui.impl.lobby.offers.offer_banner_window import OfferBannerWindow as OfferBannerWindow
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.app_loader import GuiGlobalSpaceID as GuiGlobalSpaceID, IAppLoader as IAppLoader
from skeletons.gui.game_control import ILimitedUIController as ILimitedUIController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersBannerController as IOffersBannerController, IOffersDataProvider as IOffersDataProvider
from web.cache.web_cache import CachePrefetchResult as CachePrefetchResult
_logger: Any

class OffersBannerController(IOffersBannerController):
    _appLoader: Any
    _offersProvider: Any
    _lobbyContext: Any
    _connMgr: Any
    __limitedUIController: Any
    __sync: Any
    onShowBanners: Any
    onHideBanners: Any
    def __init__(self):
        ...
    @property
    def _serverSettings(self):
        ...
    def isEnabled(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def __subscribeLui(self):
        ...
    def __unsubscribeLui(self):
        ...
    def showBanners(self, *args, **kwargs):
        ...
    def hideBanners(self, *args, **kwargs):
        ...
    # decorador original: @adisp_process
    def _loadBanners(self, *args, **kwargs):
        ...
    def _onConnected(self, *args, **kwargs):
        ...
    def _onServerSettingsChanged(self, *args, **kwargs):
        ...
    def __hasNotSeenOffers(self):
        ...
    def __iNotSeenOffers(self):
        ...
    @property
    def __isHangarViewLoaded(self):
        ...
