# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/offers/offer_banner_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.offers.offer_banner_model import OfferBannerModel as OfferBannerModel
from gui.impl.lobby.offers import getGfImagePath as getGfImagePath
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow
from helpers import dependency as dependency, getClientLanguage as getClientLanguage, isPlayerAccount as isPlayerAccount
import ResMgr as ResMgr
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider

class OfferBannerWindowView(ViewImpl):
    _offersProvider: Any
    _offerID: Any
    _langCode: Any
    def __init__(self, offerID):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def offerID(self):
        ...
    def destroyAsSeen(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onSelect(self):
        ...
    def _onClose(self):
        ...

class OfferBannerWindow(WindowImpl):
    _appLoader: Any
    _uiLoader: Any
    _offersProvider: Any
    _lobbyContext: Any
    _loaded: Any
    offerID: Any
    controller: Any
    def __init__(self, offerID, controller):
        ...
    @property
    def serverSettings(self):
        ...
    @classmethod
    def isLoaded(cls, offerID):
        ...
    @classmethod
    def tryLoad(cls, offerID, controller):
        ...
    @classmethod
    def destroyBannerWindow(cls, offerID):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _onOffersUpdated(self):
        ...
    def _updateVisibility(self, *args, **kwargs):
        ...
