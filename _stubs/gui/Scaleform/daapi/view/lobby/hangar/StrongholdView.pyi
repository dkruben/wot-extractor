# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/StrongholdView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.event_dispatcher import showHangar as showHangar
from helpers import dependency as dependency
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.clans.clan_helpers import getStrongholdUrl as getStrongholdUrl
from gui.Scaleform.daapi import LobbySubView as LobbySubView
from gui.Scaleform.daapi.view.lobby.shared.web_view import WebView as WebView
from gui.Scaleform.daapi.view.meta.StrongholdViewMeta import StrongholdViewMeta as StrongholdViewMeta
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.strongholds.web_handlers import createStrongholdsWebHandlers as createStrongholdsWebHandlers
from gui.Scaleform.daapi.view.lobby.strongholds.sound_constants import STRONGHOLD_SOUND_SPACE as STRONGHOLD_SOUND_SPACE, STRONGHOLD_ADS_SOUND_SPACE as STRONGHOLD_ADS_SOUND_SPACE
from skeletons.gui.game_control import IBrowserController as IBrowserController
from typing import Optional as Optional, Dict as Dict

class StrongholdView(LobbySubView, StrongholdViewMeta):
    __background_alpha__ = 1.0
    _COMMON_SOUND_SPACE = STRONGHOLD_SOUND_SPACE
    browserCtrl: Any
    __browser: Any
    __hasFocus: Any
    __browserId: Any
    __url: Any
    def __init__(self, ctx=None):
        ...
    def onEscapePress(self):
        ...
    def onFocusChange(self, hasFocus):
        ...
    def viewSize(self, width, height):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _onUnregisterFlashComponent(self, viewPy, alias):
        ...
    # decorador original: @adisp_process
    def __loadBrowser(self, width, height):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __close(self):
        ...
    def __updateSkipEscape(self, skipEscape):
        ...
    def __onError(self):
        ...
    def __showBrowser(self):
        ...

class StrongholdAdsView(WebView):
    _COMMON_SOUND_SPACE = STRONGHOLD_ADS_SOUND_SPACE
    def webHandlers(self):
        ...
