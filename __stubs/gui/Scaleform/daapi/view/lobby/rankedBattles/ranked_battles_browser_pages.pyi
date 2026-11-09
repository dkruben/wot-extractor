# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_browser_pages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.components.browser_view_page import BrowserPageComponent as BrowserPageComponent
from gui.Scaleform.daapi.view.lobby.hangar.BrowserView import BrowserView as BrowserView
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView as WebView
from gui.ranked_battles.constants import SeasonResultTokenPatterns as SeasonResultTokenPatterns
from gui.ranked_battles.ranked_helpers import getRankedBattlesSeasonRatingUrl as getRankedBattlesSeasonRatingUrl, getRankedBattlesInfoPageUrl as getRankedBattlesInfoPageUrl, getRankedBattlesSeasonGapUrl as getRankedBattlesSeasonGapUrl, getRankedBattlesYearRatingUrl as getRankedBattlesYearRatingUrl, getRankedBattlesShopUrl as getRankedBattlesShopUrl
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_MAIN_PAGE_SOUND_SPACE as RANKED_MAIN_PAGE_SOUND_SPACE, RANKED_OVERLAY_SOUND_SPACE as RANKED_OVERLAY_SOUND_SPACE, Sounds as Sounds, AmbientType as AmbientType
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from web.web_client_api.ranked_battles import createRankedBattlesWebHandlers as createRankedBattlesWebHandlers, createRankedOverlayHandlers as createRankedOverlayHandlers

class RankedBrowserPage(BrowserPageComponent, IResetablePage):
    __rankedController: Any
    __ctx: Any
    __isInited: Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def _isForcedRefresh(self):
        ...
    def _getWebHandlers(self):
        ...
    def _getUrl(self):
        ...
    def _getBaseUrl(self, **kwargs):
        ...
    def _updateSounds(self, soundManager):
        ...
    def __getClientParams(self):
        ...
    def __patchUrlByCtx(self):
        ...

class RankedSeasonGapPage(RankedBrowserPage):
    __rankedController: Any
    __previousSeasonID: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getBaseUrl(self, **kwargs):
        ...
    def __onTokensUpdate(self, diff):
        ...

class RankedShopPage(RankedBrowserPage):
    def _isForcedRefresh(self):
        ...
    def _getBaseUrl(self, **kwargs):
        ...
    def _updateSounds(self, soundManager):
        ...
    def _getWebHandlers(self):
        ...

class RankedRatingPage(RankedBrowserPage):
    def _getBaseUrl(self, **kwargs):
        ...
    @classmethod
    def _isRightClickAllowed(cls):
        ...

class RankedYearRatingPage(RankedBrowserPage):
    def _getBaseUrl(self, **kwargs):
        ...
    def _updateSounds(self, soundManager):
        ...

class RankedBattlesInfoPage(RankedBrowserPage):
    def _getBaseUrl(self, **kwargs):
        ...

class RankedLandingView(BrowserView):
    _BROWSER_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE
    __rankedController: Any
    def onEscapePress(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _populateSoundEnv(self, soundManager):
        ...
    def _disposeSoundEnv(self, soundManager):
        ...
    def _checkDestroy(self):
        ...

class RankedShopLandingView(RankedLandingView):
    __rankedController: Any
    def _populateSoundEnv(self, soundManager):
        ...
    def _checkDestroy(self):
        ...

class RankedYearLBLandingView(RankedLandingView):
    __rankedController: Any
    def _checkDestroy(self):
        ...

class RankedWebOverlay(WebView):
    _COMMON_SOUND_SPACE = RANKED_OVERLAY_SOUND_SPACE
    __rankedController: Any
    def webHandlers(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __destroy(self):
        ...
