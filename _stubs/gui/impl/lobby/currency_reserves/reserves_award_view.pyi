# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/currency_reserves/reserves_award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from frameworks.wulf import ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl, getWotPlusShopUrl as getWotPlusShopUrl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.currency_reserves.reserves_award_view_model import ReservesAwardViewModel as ReservesAwardViewModel
from gui.impl.lobby.currency_reserves.sounds import RESERVES_AWARD_SOUND_SPACE as RESERVES_AWARD_SOUND_SPACE
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.logging_constants import WotPlusKeys as WotPlusKeys, ReservesKeys as ReservesKeys
from uilogging.wot_plus.loggers import WotPlusEventLogger as WotPlusEventLogger

class ReservesAwardView(ViewImpl):
    _itemsCache: Any
    _lobbyContext: Any
    _wotPlusCtrl: Any
    __slots__: tuple
    _COMMON_SOUND_SPACE = RESERVES_AWARD_SOUND_SPACE
    _wotPlusUILogger: Any
    def __init__(self, layoutID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, creditsEarned, goldEarned):
        ...
    def _isPremiumPlusActive(self):
        ...
    def _isPiggyBankEnabled(self):
        ...
    def _isGoldReserveEnabled(self):
        ...
    def _onPremiumAccountExtend(self):
        ...
    def _onSubscriptionExtend(self):
        ...
    def _onClose(self):
        ...

class ReservesAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, creditsEarned, goldEarned):
        ...
