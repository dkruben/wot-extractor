# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/offers/offer_gift_dialog.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
from account_helpers.offers.events_data import OfferGift as OfferGift, OfferEventData as OfferEventData
from constants import RentType as RentType
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl import backport as backport
from gui.impl.dialogs.builders import SimpleDialogBuilder as SimpleDialogBuilder, PureDialogBuilder as PureDialogBuilder
from gui.impl.gen import R as R
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.pub.pure_dialog_window import PureDialogWindow as PureDialogWindow
from gui.impl.pub.simple_dialog_window import SimpleDialogWindow as SimpleDialogWindow
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from gui.impl.lobby.dialogs.contents.prices_content import DialogPricesContent as DialogPricesContent
_logger: Any
RENT_VALUE_DESCR_BY_TYPE: dict

class OffersDialogWindowMixin(object):
    _lobbyContext: Any
    _offersProvider: Any
    _offerID: Any
    _price: Any
    def __init__(self, offerID, price, *args, **kwargs):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __close(self):
        ...
    def __onServerSettingsChange(self, *args, **kwargs):
        ...
    def _onOffersUpdated(self):
        ...
    def __updatePrice(self):
        ...
    def _getResultData(self):
        ...

class OffersSimpleDialogWindow(OffersDialogWindowMixin, SimpleDialogWindow):
    def __init__(self, offerID, price, *args, **kwargs):
        ...

class OffersPureDialogWindow(OffersDialogWindowMixin, PureDialogWindow):
    def __init__(self, offerID, price, *args, **kwargs):
        ...

class _OffersSimpleDialogBuilder(SimpleDialogBuilder):
    _offersProvider: Any
    _offer: Any
    _gift: Any
    _windowClass: Any
    def __init__(self, offerID, giftID):
        ...
    @property
    def title(self):
        ...
    @property
    def description(self):
        ...

class _OffersPureDialogBuilder(PureDialogBuilder):
    _offersProvider: Any
    _offer: Any
    _gift: Any
    _windowClass: Any
    _cdnTitle: Any
    def __init__(self, offerID, giftID, cdnTitle=''):
        ...
    @property
    def title(self):
        ...

def makeOfferGiftDialog(offerID, giftID, cdnTitle=''):
    ...
