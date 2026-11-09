# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/links_handlers/external.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
import typing as typing
import logging as logging
from future.moves.urllib.parse import urlparse as urlparse, parse_qs as parse_qs
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import BigWorld as BigWorld
from constants import DISTRIBUTION_PLATFORM as DISTRIBUTION_PLATFORM
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.Scaleform.daapi.view.lobby.store.browser import shop_helpers as shop_helpers
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency
from helpers.http.url_formatters import addParamsToUrlQuery as addParamsToUrlQuery
from skeletons.gui.login_manager import ILoginManager as ILoginManager
_PLATFORM_PARAM = 'platform'
_WOT_PLATFORM_PARAM = 'wot_platform'
_INGAME_SHOP_PARAM = 'ingame_shop'
_PATH_TO_CHECK_ARGS = '/id/signin/token'
_URL_ARGS_TO_CHECK: tuple
_logger: Any
CheckHandleResult: Any

class ILinksHandler(object):
    def checkHandle(self, url):
        ...
    def handle(self, url):
        ...

class OpenBrowserHandler(ILinksHandler):
    def checkHandle(self, url):
        ...
    def handle(self, url):
        ...

class AddPlatformTagLinksHandler(OpenBrowserHandler):
    __loginManager: Any
    def checkHandle(self, url):
        ...
    def handle(self, url):
        ...
    def _getPlatform(self):
        ...
    def _hasWotPlatformTags(self, url):
        ...
    def _addPlatformParamToUrl(self, url, param):
        ...

class AddPlatformTagLinksToArgsUrlHandler(AddPlatformTagLinksHandler):
    def _hasWotPlatformTags(self, url):
        ...
    def handle(self, url):
        ...

class PremShopLinksHandler(ILinksHandler):
    def checkHandle(self, url):
        ...
    def handle(self, url):
        ...
    def __getIngameShopArgs(self, url):
        ...

class PremShopLinksForArgsUrlHandler(PremShopLinksHandler):
    def checkHandle(self, url):
        ...
    def handle(self, url):
        ...

def _getUrlsMapFromLinkArgs(url):
    ...
