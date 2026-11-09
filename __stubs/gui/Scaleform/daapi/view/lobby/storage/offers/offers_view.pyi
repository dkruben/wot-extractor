# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/offers/offers_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ResMgr as ResMgr
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import createStorageDefVO as createStorageDefVO
from gui.Scaleform.daapi.view.meta.StorageCategoryOffersViewMeta import StorageCategoryOffersViewMeta as StorageCategoryOffersViewMeta
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.date_time_formats import DateTimeFormatsEnum as DateTimeFormatsEnum
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow, showShop as showShop
from gui.shared.formatters import text_styles as text_styles
from gui.shared.formatters.date_time import getRegionalDateTime as getRegionalDateTime
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersNovelty as IOffersNovelty, IOffersDataProvider as IOffersDataProvider
from web.cache.web_cache import CachePrefetchResult as CachePrefetchResult

class StorageCategoryOffersView(StorageCategoryOffersViewMeta):
    _offersProvider: Any
    _offersNovelty: Any
    _lobbyContext: Any
    _currentOffersCount: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self):
        ...
    def _onOffersUpdated(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _syncOffers(self, callback=None):
        ...
    # decorador original: @adisp_process
    def _updateData(self):
        ...
    def _getVoList(self):
        ...
    def _getVO(self, offer):
        ...
    def scrolledToBottom(self):
        ...
    def openOfferWindow(self, offerID):
        ...
    def navigateToStore(self):
        ...
    def __onServerSettingsChange(self, *args, **kwargs):
        ...
