# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/store/browser/shop_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView as WebView
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getShopURL as getShopURL
from gui.Scaleform.daapi.view.lobby.store.browser.sound_constants import SHOP_SOUND_SPACE as SHOP_SOUND_SPACE
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.shop.loggers import ShopMetricsLogger as ShopMetricsLogger
from uilogging.shop.logging_constants import ShopLogKeys as ShopLogKeys
_logger: Any

class _ShopOverlayBase(WebView):
    def _onError(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def webHandlers(self):
        ...

class ShopBase(_ShopOverlayBase):
    _COMMON_SOUND_SPACE = SHOP_SOUND_SPACE
    def __init__(self, ctx=None):
        ...

class ShopView(LobbySubView, ShopBase):
    lobbyContext: Any
    itemsCache: Any
    __uiLogger: Any
    def __init__(self, ctx=None):
        ...
    def onCloseBtnClick(self):
        ...
    def onEscapePress(self):
        ...
    def _dispose(self):
        ...
    def __onShopResync(self):
        ...

class ShopOverlay(_ShopOverlayBase):
    __uiLogger: Any
    def __init__(self, ctx=None):
        ...
    def _dispose(self):
        ...
    def onEscapePress(self):
        ...
