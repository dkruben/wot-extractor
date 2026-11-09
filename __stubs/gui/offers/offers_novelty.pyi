# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/offers/offers_novelty.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
from account_helpers.AccountSettings import AccountSettings as AccountSettings, VIEWED_OFFERS as VIEWED_OFFERS
from helpers import dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersNovelty as IOffersNovelty, IOffersDataProvider as IOffersDataProvider

class OffersNovelty(IOffersNovelty):
    _offersProvider: Any
    _lobbyContext: Any
    _connMgr: Any
    onUpdated: Any
    __newOffers: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def setAsSeen(self):
        ...
    def saveAsSeen(self, offerId):
        ...
    @property
    def showNovelty(self):
        ...
    @property
    def noveltyCount(self):
        ...
    @property
    def _serverSettings(self):
        ...
    def _onConnected(self, *args, **kwargs):
        ...
    def _onServerSettingsChanged(self, *args, **kwargs):
        ...
    def __updateNovelty(self, *args, **kwargs):
        ...
    def __updateNewOffers(self):
        ...
    def __clearNotActiveOffers(self):
        ...
    @staticmethod
    def __setViewedOffers(viewedOffers):
        ...
    @staticmethod
    def __getViewedOffers():
        ...
